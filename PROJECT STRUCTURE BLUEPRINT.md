UJAPI Project Structure Plan
_slow down, this is a blueprint!_
```gitGraph
UJAPI/
├── LICENSE                     # MIT License
├── README.md                   # Project overview and documentation
├── .gitignore                  # Git ignore file
├── scripts/
│   ├── __init__.py             # Makes the directory a package
│   ├── rig_analyzer.py         # Script to analyze and dump rig structure
│   ├── proxy_creator.py        # Creates the universal proxy armature
│   ├── constraint_system.py    # Sets up the bone constraints
│   └── animation_transfer.py   # Handles animation transfer and baking
├── configs/
│   ├── bone_mappings/
│   │   ├── mixamo_to_universal.json  # Mapping from Mixamo to universal proxy
│   │   └── universal_to_custom.json  # Template for mapping universal to custom
│   └── export_presets/
│       └── standard.json       # Standard export settings
├── examples/
│   ├── proxy_armature.blend    # Example proxy armature
│   └── workflow_example.blend  # Complete example workflow
├── docs/
│   ├── getting_started.md      # Getting started guide
│   ├── bone_mapping_guide.md   # Guide for bone mapping
│   └── workflow.md             # Detailed workflow documentation
└── tests/                      # Test files and scripts
    └── test_bone_transfer.blend # Test file for bone transfer
```
Key Components
Scripts
Core Python scripts that implement the main functionality:

  rig_analyzer.py: Analyzes a rig and dumps its structure to JSON
  proxy_creator.py: Creates the universal proxy armature
  constraint_system.py: Sets up the bone constraints
  animation_transfer.py: Transfers animations between rigs

Configs
_Configuration files for bone mappings and export settings:_
  bone_mappings/: Contains JSON files defining bone mappings
  export_presets/: Contains export settings for various formats

Examples
Example files demonstrating the workflow:
  proxy_armature.blend: A pre-built proxy armature
  workflow_example.blend: A complete example workflow

Docs
_Documentation files:_
  getting_started.md: Guide to get started with UJAPI
  bone_mapping_guide.md: Guide for creating bone mappings
  workflow.md: Detailed workflow documentation

Tests
_Test files and scripts:_
test_bone_transfer.blend: Test file for the bone transfer system
