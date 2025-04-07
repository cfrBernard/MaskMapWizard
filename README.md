# MaskMapWizard

This is a simple Python app, designed to help you create Mask Maps by combining multiple textures (such as Metallic, AO, Detail, and Smoothness) into a single RGBA image. It’s a powerful solution for optimizing textures in Unity HDRP, where these maps are commonly used to improve material performance.

[**Download the latest version here**](https://github.com/cfrBernard/MaskMapWizard/releases)

## Features:
- Drag and drop support for texture files (Metallic, AO, Detail, Smoothness).
- Automatically resizes and merges the maps into a single RGBA image.
- Supports Unity HDRP conventions (Metallic in Red, AO in Green, Detail in Blue, and Smoothness in Alpha).
- Roughness inversion to Smoothness (in the future, this will be more customizable).
- Path selection for output files.

## Requirements:
- Python 3.x
- Pillow for image processing
- tkinterdnd2 for drag and drop
- tkinter for the GUI

**Note**: `tkinter` comes pre-installed with Python on most systems.

## 🛠️ Installation:
1. Clone this repository or download the script:
    ```bash
    git clone https://github.com/cfrBernard/MaskMapWizard.git
    cd MaskMapWizard
    ```
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    python main.py
    ```

## How to Use:
- Drag and Drop the Metallic, AO, Detail, and Smoothness textures into their respective fields.
- Select the Export Path where you want the final Mask Map to be saved.
- Hit Build to create your combined Mask Map.
- Check the Console for messages and updates.

## 🔮 What's Coming:
- ### Support for other engines:
  - I plan to introduce presets for different game engines, like Unreal Engine and custom engines, allowing users to configure the channel order (e.g., Roughness in Red, Metallic in Green).

- ### Customizable Mask Map settings:
  - Users will be able to invert Smoothness to Roughness, select channel order, and tweak other settings for greater flexibility.

- ### Advanced Mapping Options:
  - Support for defining exactly which maps go into which RGBA channels.

- ### Future versions with improved UI:
  - A more polished user interface with intuitive features and better error handling.

## Notes:
- This tool is currently Unity HDRP-focused, but it will evolve to support more engines.
- Feel free to contribute by adding engine-specific presets, new features, or bug fixes!

## 🤝 Contact:
For issues, suggestions, or contributions, feel free to open an issue on the GitHub repository.
