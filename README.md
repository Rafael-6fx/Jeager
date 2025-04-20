# UJAPI - Universal Jaeger Armature Proxy Interface for blender

A toolkit for transferring animations from Mixamo to custom Blender armatures.

![Project Banner](https://via.placeholder.com/800x200?text=Universal+Jaeger+Armature+Interface)

## 🚀 Overview

This project provides a comprehensive workflow and tools for:

- Analyzing and mapping rig structures
- Creating a universal proxy armature for Mixamo animations
- Transferring animations between different rig types
- Creating a standardized interface for animation retargeting
- Supporting custom rigging workflows

## 📋 Project Phases

### Phase 1: Analyze and Prepare
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

## 💻 Requirements

- Blender 2.93 or later
- Mixamo account for animations

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ujapi.git

# Navigate to project directory
cd ujapi
```

## 📖 Documentation

Detailed documentation is available in the [docs](./docs) directory:

- [Setup Guide](./docs/setup.md)
- [Workflow Documentation](./docs/workflow.md)
- [Troubleshooting](./docs/troubleshooting.md)

## 📁 Repository Structure

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [Mixamo](https://www.mixamo.com/) for providing animations
- [Blender](https://www.blender.org/) for the 3D creation suite
