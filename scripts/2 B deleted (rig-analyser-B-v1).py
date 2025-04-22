""" 
IMPORTANT - for blender internal use only

Rig Analyzer for Universal Jaeger Armature Interface:
This script analyzes a Blender armature and dumps its structure to a JSON file.
It captures bone hierarchies, transformations, constraints, and other properties
essential for rig retargeting.

Usage:
    1. Open Blender file with target armature
    2. Select the armature
    3. Run this script
    4. JSON file will be created in the specified output directory
"""

import bpy
import json
import os
import math
from mathutils import Vector, Matrix, Quaternion

def get_selected_armature():
    """Get the currently selected armature."""
    selected = bpy.context.selected_objects
    for obj in selected:
        if obj.type == 'ARMATURE':
            return obj
    return None

def get_bone_info(bone, armature):
    """Extract detailed information about a bone."""
    pose_bone = armature.pose.bones.get(bone.name)
    
    # Get local rest transform
    loc, rot, scale = bone.matrix_local.decompose()
    
    # Get parent information
    parent_name = bone.parent.name if bone.parent else None
    
    # Get constraints
    constraints = []
    if pose_bone:
        for constraint in pose_bone.constraints:
            constraint_data = {
                "name": constraint.name,
                "type": constraint.type,
                "influence": constraint.influence,
                "enabled": constraint.enabled
            }
            
            # Add target information if available
            if hasattr(constraint, "target") and constraint.target:
                constraint_data["target"] = constraint.target.name
                if hasattr(constraint, "subtarget") and constraint.subtarget:
                    constraint_data["subtarget"] = constraint.subtarget
            
            constraints.append(constraint_data)
    
    # Build bone info dictionary
    bone_info = {
        "name": bone.name,
        "parent": parent_name,
        "head": [round(v, 6) for v in bone.head_local],
        "tail": [round(v, 6) for v in bone.tail_local],
        "length": round(bone.length, 6),
        "transform": {
            "location": [round(v, 6) for v in loc],
            "rotation": [round(v, 6) for v in rot],
            "scale": [round(v, 6) for v in scale]
        },
        "roll": round(bone.roll, 6),
        "use_connect": bone.use_connect,
        "use_deform": bone.use_deform,
        "layers": [bool(i) for i in bone.layers],
        "constraints": constraints,
        "children": []
    }
    
    return bone_info

def build_bone_hierarchy(armature_obj):
    """Build a hierarchical representation of the armature."""
    armature = armature_obj.data
    
    # Create bone info dictionary
    bones_dict = {}
    for bone in armature.bones:
        bones_dict[bone.name] = get_bone_info(bone, armature_obj)
    
    # Build hierarchy
    root_bones = []
    for bone in armature.bones:
        if not bone.parent:
            root_bones.append(bones_dict[bone.name])
        else:
            bones_dict[bone.parent.name]["children"].append(bones_dict[bone.name])
    
    return root_bones

def get_armature_info(armature_obj):
    """Get comprehensive information about an armature."""
    armature_data = armature_obj.data
    
    # Get armature properties
    armature_info = {
        "name": armature_obj.name,
        "bones_count": len(armature_data.bones),
        "scale": list(armature_obj.scale),
        "location": list(armature_obj.location),
        "rotation_euler": list(armature_obj.rotation_euler),
        "bone_hierarchy": build_bone_hierarchy(armature_obj),
        "bone_groups": [],
        "pose_position": armature_data.pose_position,
        "collections": [collection.name for collection in armature_obj.users_collection]
    }
    
    # Get bone groups
    for group in armature_obj.pose.bone_groups:
        bone_group = {
            "name": group.name,
            "color_set": group.color_set,
            "bones": [bone.name for bone in armature_obj.pose.bones if bone.bone_group and bone.bone_group.name == group.name]
        }
        armature_info["bone_groups"].append(bone_group)
    
    return armature_info

def get_flat_bone_list(armature_obj):
    """Get a flat list of all bones and their properties."""
    flat_bones = []
    for bone in armature_obj.data.bones:
        pose_bone = armature_obj.pose.bones.get(bone.name)
        bone_info = {
            "name": bone.name,
            "head": list(bone.head_local),
            "tail": list(bone.tail_local),
            "parent": bone.parent.name if bone.parent else None,
            "connected": bone.use_connect,
            "length": bone.length,
            "roll": bone.roll,
            "use_deform": bone.use_deform,
            "constraints": []
        }
        
        if pose_bone:
            for constraint in pose_bone.constraints:
                constraint_info = {
                    "name": constraint.name,
                    "type": constraint.type,
                    "influence": constraint.influence
                }
                bone_info["constraints"].append(constraint_info)
        
        flat_bones.append(bone_info)
    
    return flat_bones

def export_armature_to_json(armature_obj, output_dir="./configs/bone_mappings", filename=None):
    """Export armature information to a JSON file."""
    if not armature_obj:
        print("No armature selected.")
        return False
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Set filename
    if not filename:
        filename = f"{armature_obj.name}_structure.json"
    output_path = os.path.join(output_dir, filename)
    
    # Generate armature info
    armature_info = {
        "meta": {
            "exporter_version": "1.0.0",
            "blender_version": bpy.app.version_string,
            "export_date": bpy.context.scene.render.frame_current_final
        },
        "hierarchical_structure": get_armature_info(armature_obj),
        "flat_bone_list": get_flat_bone_list(armature_obj)
    }
    
    # Write to file
    with open(output_path, 'w') as f:
        json.dump(armature_info, f, indent=2)
    
    print(f"Armature structure exported to {output_path}")
    return True

def main():
    """Main function."""
    # Get selected armature
    armature = get_selected_armature()
    if not armature:
        print("Please select an armature.")
        return
    
    # Export to JSON
    export_armature_to_json(armature)

if __name__ == "__main__":
    main()
