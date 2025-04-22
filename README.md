# UJAPI  _[ooh•jah•pee]_
### Universal Jaeger Armature Proxy Interface for Blender
> A toolkit for transferring animations from things like Mixamo to custom Blender armatures.
<br>

I noticed tons of users are struggling to.. align various models existing armature with something workable. Your choice is labour or "pay to win". I think there's no point gatekeeping useful stuff so I am making anything I made public - maybe someone can chip in on the code implementation/compatibillity since the way I look at code is very design-centric and I acknowledge my limitations.

if you found this useful we can have a chat, even just virtual one.
I would rather network with likeminded people than expect monetary value from general contribution.
<br>
>[!IMPORTANT]
> I am not sure if this project will gravitate into estabilished Blender workflows 
> or end up being more of a standalone abstraction layer - your thoughts welcome

>[!NOTE]
> This is my first ever repo so please forgive me any teething related issues
<br>
<br>
<br>
<br>

___

## Overview
This project aims to provide a comprehensive workflow and tools for:

- Analyzing and mapping rig structures
- Creating a universal proxy armature (for Mixamo animations and similar)
- Transferring animations between different rig types
- Creating a standardized interface for animation retargeting
- Supporting custom rigging workflows

## Implementation Phasing
### Phase 1: Analyze and Prepare target model, 
- Get the example animation rig files from Mixamo
- Dump the structure of the target rig into JSON
- Download binary FBX from Mixamo for animation

### Phase 2: Build Universal Proxy Armature
- Create a standardized proxy armature that works as a universal interface
- Import and analyze target rig for mapping
- Configure bone mappings between systems

### Phase 3: Connection System
- Create bone animation transfer system 
- Set up constraints between proxy and target rigs
- Verify connection with test poses

### Phase 4: Animation Transfer
- Import Mixamo animation to the proxy armature
- Test animation playback on proxy
- Transfer and bake animation to target rig

### Phase 5: Export and Finalization
- Optimize animation for performance
- Cleanup and bake final animation
- Export in compatible formats

### Phase 6: Future Extensions
- Additional rig support
- Custom animation tools
- Expanding the proxy interface capabilities


<br>
<br>
<br>
<br>


---

## Requirements
- Blender 4.2 or later
- .FBX animation format (Mixamo for now)

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ujapi.git

# Navigate to project directory
cd ujapi
```

---
## 📖 Documentation (let's hope)
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

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

##  License
This project is licensed under Apache 2.0 - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments
- [Mixamo](https://www.mixamo.com/) for providing animations
- [Blender](https://www.blender.org/) for the 3D creation suite that provides so many people with creative freedom
