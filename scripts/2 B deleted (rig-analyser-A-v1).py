import bpy
import json
import os
import traceback
from mathutils import Vector, Euler, Quaternion, Matrix

# Enhanced serializer to handle all Blender specific types
def serialize_value(val):
    """Convert Blender-specific types to JSON-serializable types"""
    if val is None:
        return None
    elif isinstance(val, (int, float, bool, str)):
        return val
    elif isinstance(val, (Vector, Euler, Quaternion)):
        return [round(float(x), 6) for x in val]
    elif isinstance(val, Matrix):
        return [[round(float(x), 6) for x in row] for row in val]
    elif hasattr(val, "__iter__") and not isinstance(val, str):
        return [serialize_value(x) for x in val]
    elif hasattr(val, "name"):
        return val.name
    elif hasattr(val, "__str__"):
        return str(val)
    else:
        return f"Unserializable: {type(val).__name__}"

def get_custom_properties(obj):
    """Extract custom properties from an object that supports them"""
    props = {}
    if obj is None:
        return props
    
    # Only ID, Bone and PoseBone support custom properties
    if not isinstance(obj, (bpy.types.ID, bpy.types.Bone, bpy.types.PoseBone)):
        return props
    
    for key in obj.keys():
        if key != "_RNA_UI":
            try:
                props[key] = serialize_value(obj[key])
            except:
                props[key] = "Unable to access"
    
    return props

def get_bone_tree(pose_bones):
    """Build a hierarchical tree of bones"""
    if not pose_bones:
        return {}
    
    # Find root bones (no parent)
    root_bones = [bone for bone in pose_bones if not bone.parent]
    bone_tree = {}
    
    # Process each root bone
    for bone in root_bones:
        bone_tree[bone.name] = build_bone_subtree(bone)
    
    return bone_tree

def build_bone_subtree(bone):
    """Recursively build a subtree for a bone"""
    subtree = {"children": {}}
    
    for child in bone.children:
        subtree["children"][child.name] = build_bone_subtree(child)
    
    return subtree

def get_rig_structure(obj):
    """Extract detailed information about an armature object"""
    output = {}
    
    try:
        # Basic armature info
        armature = obj.data
        output["armature_name"] = armature.name
        output["bones"] = []
        output["bone_collections"] = []
        
        # Get pose bones first - they contain the animation state
        pose_bones = []
        if obj.pose and obj.pose.bones:
            pose_bones = obj.pose.bones
            output["bone_tree"] = get_bone_tree(pose_bones)
        else:
            output["bone_tree"] = {}
            output["warning"] = "No pose bones found - object may not be in Pose mode"
        
        # Get bone collections
        if hasattr(armature, "collections"):
            for collection in armature.collections:
                collection_info = {
                    "name": collection.name,
                    "is_visible": serialize_value(collection.is_visible) if hasattr(collection, "is_visible") else True,
                    "bones": [],
                    "custom_properties": get_custom_properties(collection)
                }
                
                # Get bones in this collection
                if hasattr(collection, "bones"):
                    collection_info["bones"] = [bone.name for bone in collection.bones]
                
                output["bone_collections"].append(collection_info)
        
        # Process pose bones
        for pose_bone in pose_bones:
            # Get the actual bone data from pose_bone.bone
            actual_bone = pose_bone.bone if hasattr(pose_bone, "bone") else None
            
            bone_info = {
                "name": pose_bone.name,
                "parent": pose_bone.parent.name if pose_bone.parent else None,
                "children": [child.name for child in pose_bone.children],
                "custom_properties": get_custom_properties(pose_bone),
                "constraints": [],
                "drivers": [],
                
                # Add data from the actual bone
                "bone_data": {
                    "name": actual_bone.name if actual_bone else None,
                    "use_deform": actual_bone.use_deform if actual_bone and hasattr(actual_bone, "use_deform") else False,
                    "layers": serialize_value(actual_bone.layers) if actual_bone and hasattr(actual_bone, "layers") else [],
                    "use_connect": actual_bone.use_connect if actual_bone and hasattr(actual_bone, "use_connect") else False,
                    "custom_properties": get_custom_properties(actual_bone)
                },
                
                # Transform data from pose bone
                "transform": {
                    "head": serialize_value(pose_bone.head),
                    "tail": serialize_value(pose_bone.tail),
                    "length": round(float(pose_bone.length), 6) if hasattr(pose_bone, "length") else None,
                    "location": serialize_value(pose_bone.location),
                    "rotation_mode": pose_bone.rotation_mode,
                    "rotation_euler": serialize_value(pose_bone.rotation_euler),
                    "rotation_quaternion": serialize_value(pose_bone.rotation_quaternion),
                    "scale": serialize_value(pose_bone.scale)
                },
                
                # Lock data
                "locks": {
                    "location": serialize_value(pose_bone.lock_location),
                    "rotation": serialize_value(pose_bone.lock_rotation),
                    "scale": serialize_value(pose_bone.lock_scale),
                    "rotation_w": pose_bone.lock_rotation_w,
                    "rotations_4d": pose_bone.lock_rotations_4d
                }
            }
            
            # Get constraints
            for constraint in pose_bone.constraints:
                constraint_info = {
                    "name": constraint.name,
                    "type": constraint.type,
                    "influence": serialize_value(constraint.influence) if hasattr(constraint, "influence") else 1.0,
                    "mute": constraint.mute if hasattr(constraint, "mute") else False,
                    "properties": {}
                }
                
                # Get target if available
                if hasattr(constraint, "target") and constraint.target:
                    constraint_info["target"] = constraint.target.name
                    if hasattr(constraint, "subtarget") and constraint.subtarget:
                        constraint_info["subtarget"] = constraint.subtarget
                
                # Get constraint properties dynamically
                for prop in dir(constraint):
                    if (not prop.startswith("_") and 
                        prop not in ["target", "subtarget", "name", "type", "influence", "mute", "rna_type"]):
                        try:
                            attr = getattr(constraint, prop)
                            constraint_info["properties"][prop] = serialize_value(attr)
                        except:
                            pass
                
                bone_info["constraints"].append(constraint_info)
            
            # Categorize bone type based on name
            bone_info["appears_to_be_ik"] = "ik" in pose_bone.name.lower()
            bone_info["appears_to_be_fk"] = "fk" in pose_bone.name.lower()
            bone_info["appears_to_be_control"] = any(word in pose_bone.name.lower() for word in 
                                                    ["ctrl", "control", "master"])
            bone_info["appears_to_be_special"] = any(word in pose_bone.name.lower() for word in 
                                                    ["tweak", "cloth", "face", "sternum", "fold", "panel", 
                                                     "cyborg", "attach"])
            
            output["bones"].append(bone_info)
        
        # Get driver information
        if obj.animation_data and obj.animation_data.drivers:
            for driver in obj.animation_data.drivers:
                driver_info = {
                    "data_path": driver.data_path,
                    "array_index": driver.array_index,
                    "expression": driver.driver.expression if hasattr(driver.driver, "expression") else "",
                    "variables": []
                }
                
                # Extract bone name from data path
                bone_name = None
                if 'pose.bones["' in driver.data_path:
                    parts = driver.data_path.split('pose.bones["')
                    if len(parts) > 1:
                        bone_name = parts[1].split('"]')[0]
                
                # Get variables
                for var in driver.driver.variables:
                    var_info = {
                        "name": var.name,
                        "type": var.type,
                        "targets": []
                    }
                    
                    for target in var.targets:
                        target_info = {
                            "data_path": target.data_path
                        }
                        
                        if hasattr(target, "id") and target.id:
                            target_info["id"] = target.id.name
                            target_info["id_type"] = target.id_type if hasattr(target, "id_type") else "Unknown"
                        
                        var_info["targets"].append(target_info)
                    
                    driver_info["variables"].append(var_info)
                
                # Add driver to bone
                if bone_name:
                    for bone in output["bones"]:
                        if bone["name"] == bone_name:
                            bone["drivers"].append(driver_info)
                            break
        
        # Add analysis section
        output["analysis"] = {
            "deform_bones": [bone["name"] for bone in output["bones"] 
                             if bone.get("bone_data", {}).get("use_deform", False)],
            "control_bones": [bone["name"] for bone in output["bones"] 
                              if bone.get("appears_to_be_control", False)],
            "ik_bones": [bone["name"] for bone in output["bones"] 
                         if bone.get("appears_to_be_ik", False)],
            "fk_bones": [bone["name"] for bone in output["bones"] 
                         if bone.get("appears_to_be_fk", False)],
            "special_bones": [bone["name"] for bone in output["bones"] 
                              if bone.get("appears_to_be_special", False)],
            "constrained_bones": [bone["name"] for bone in output["bones"] 
                                 if bone.get("constraints", [])]
        }
        
        return output
    
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }

def main():
    active_obj = bpy.context.active_object
    if active_obj and active_obj.type == 'ARMATURE':
        try:
            # Get the rig structure
            structure = get_rig_structure(active_obj)
            
            # Convert to JSON - ensure all values are serialized properly
            try:
                json_str = json.dumps(structure, indent=2)
                
                # Create output directory
                blend_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.path.expanduser("~")
                output_dir = os.path.join(blend_dir, "console_outputs")
                os.makedirs(output_dir, exist_ok=True)
                
                # Save to file
                file_path = os.path.join(output_dir, "structure.json")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(json_str)
                
                print(f"Rig structure analysis saved to: {file_path}")
                print(f"Total bones analyzed: {len(structure.get('bones', []))}")
                print(f"Bone collections found: {len(structure.get('bone_collections', []))}")
                
            except TypeError as e:
                print(f"JSON serialization error: {e}")
                print("This usually means a Blender-specific type wasn't properly converted.")
                
        except Exception as e:
            print(f"Error: {e}")
            print(traceback.format_exc())
    else:
        print("No armature selected. Please select an armature object.")

# Run the script
main()
