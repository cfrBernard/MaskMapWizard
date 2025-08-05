## 1. Build the executable using build.py

This project now includes a build script that wraps PyInstaller with all required options.

Run:

    python build.py


This will:
- Clean previous `build/` and `dist/` directories.
- Build a single-file executable with the correct icon and hooks.
- Output the `.exe` in `dist/MaskMapWizard_vX.Y.Z/`.

---

## 2. Additional Notes

- `tkinterdnd2-universal` requires the `hook-tkinterdnd2.py` file (already included in `hooks/`).
- The icon is located in `assets/icon.ico`.

For manual builds (not recommended):

    pyinstaller src/MaskMapWizard/__main__.py -F -w --icon=assets/icon.ico --additional-hooks-dir=hooks

---

>## Source:  
> - https://pypi.org/project/tkinterdnd2-universal/  
> - Hook: https://github.com/pmgagne/tkinterdnd2/blob/master/hook-tkinterdnd2.py
