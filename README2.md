# J E Λ G Ξ R $$\thinspace{\tiny \color{gray}{[\textit{yeah•guh}]\space/\textit{\negthinspaceˈjɛː\thinspaceɡɐ}/}}$$
### Universal Armature Mocapped Animation Transfer Proxy Interface for Blender 3.0+
> _A toolkit for transferring animations from free mocaps like Mixamo to Blender armature through baking animations into NLA subsystem._

---

**Why did I even bother?** 

You might think that there's loads of plugins that do the same thing but... <br>
Jeager is different enough to be valid because 
- it doesn't rely on estabilished workflows and preconceptions
- it has a cooler name
- made from an "outsider" designer's perspective with the personal motto "_listen to everyone but follow no one_"
- it will likely support wide array of situations/rigs/models regardless of their origin
- built from the foundation up, not from the center to the edge ensuring exandability
- incorporates few ideas author is proud of despite of almost **never** being proud of his own ideas

**The holy WHY beind the project**

I noticed tons of users like myself are struggling to.. align various models existing armature with something workable. 
The choices seem to be narrowed down to hardcode manual labour or "pay to win". 
I think there's always room to improve on therefore I am making my work public - 
this way I get to work on the code with someone more advanced and improve implementation/compatibillity since the way I look at code tend to naturally be very design-centric and I acknowledge my limitations.

<br>
>[!IMPORTANT]
> I am not sure if this project will gravitate into estabilished Blender workflows 
> or end up being more of a standalone abstraction layer - your thoughts welcome

>[!NOTE]
> This is my first repo so apologies for mistakes in advance
<br>
<br>
<br>

___

# Overview
This project aims to provide a comprehensive workflow and tools for:
- Analyzing and mapping rig structures of the humanoid input model
- Creating a universal proxy armature (for Mixamo animations and similar mocaps)
- Transferring animations between different rig types through spatialisation and proximity
- Creating a standardized interface for animation retargeting/transfering that would be specific-bone agnostic
- Supporting custom rigging workflows through deterministic importance evaluation


## Implementation Phasing
### Phase 1: Analyze and evaluate the target humanoid rig
- Evaluate potential vert influence problems
- Run analyzer to determine the "real-effectors" 
- Spatialise the rig and dump it into retrievable format
- Dump the bone hierarchy and determine P.O.I.
- Determine armature complexity (hands, feet, face, vertebrae etc. bone presence)
- Determine proportion classification (dave, munchkin, chibi, enderman, waifu, beefcake, tank, potato, spider)
- 2DO(future): WhereIsHam: body bone<>mesh classification evaluator
- bonus(future): Mesh based armature's meta-volume system
- bonus(future): ray-tracing based smart bone rejection system  

### Phase 2: Build Universal Proxy Armature Scaffolding
- Create a standardized proxy armature that works as a universal interface
- Determine complexity of the mocapped rig (hands, feet, face, vertebrae etc. bone rejections)
- Import Riggify humanoid rig of matching complexity
- First pass scale matching to the target (height only)
- Determinee initial resting T-pose difference
- Determine initial differences between spatial properties

### Phase 3: Connection System
- Create bone animation transfer system 
- Set up low-level access influence between proxy and target rigs
- Verify scaling, alignment and offsets
- Reorganise the 

### Phase 4: User interfacing
- Separate screen for diagnostics and control
- Resolving issues with organisation and information density displaying
- Preparing custom views for Jeager specific debugging
- New 3D viewport overlay to view the armature that doesn't require mode change
- 

### Phase 5: Animation/Pose Transfer
- Download and import mocapped animation to the Blender
- Evaluate the target<>jeager<>mocap fit
- Test animation playback on proxy
- Transfer and bake animation to target rig animation system

### Phase 6: Export and Finalization
- Cleanup and bake final animation
- bonus: Optimize animation for performance (interpolation
- bonus: Export simplification for minimal-load max-compatibility formats

- ### Phase 7: Wishful thinking
- Additional rig support
- Custom animation tools
- Expanding the proxy interface capabilities
- Expanding toolkits as Riggidy alternative?


<br>
<br>
<br>
<br>


---

## Requirements
- Blender 3.0 or later
- Blender Riggify Plugin wouldn't hurt (since it comes with blander... why not!)
>[!WARNING]
> Theoretically the way the data is built and captured should make it usable for 3.0+ however I have not done any testing and it was made using Blender 4.3 
- Blender supported .FBX skeletal animation format (Mixamo for now) as the source
- understanding of NLA animation framework

## Installation

It is served as a plugin so the procedure of installation is the same

---
## Documentation (only sketch of the structure for now)
Detailed documentation will be available in the [docs](./docs) directory:

- [Setup Guide](./docs/setup.md)
- [Workflow Documentation](./docs/workflow.md)
- [Troubleshooting](./docs/troubleshooting.md)

## Repository Structure
- `scripts/`: Python scripts for rig analysis, proxy creation, and animation transfer
- `configs/`: Configuration files for bone mappings and export settings
- `examples/`: Example files demonstrating the workflow
- `docs/`: Detailed documentation
- `tests/`: Test files for verifying functionality

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under Apache 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Mixamo](https://www.mixamo.com/) for providing animations
- [Blender](https://www.blender.org/) for the 3D creation suite that provides so many people with creative freedom. Please consider supporting the Blender Foundation, contributions is exactly what is keeping forward momentum!✊
