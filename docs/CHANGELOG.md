## [v0.1.1] - 2025-08-01
### Fixed

- **Drag & Drop with spaces in file paths**
  - Fixed an issue where files dragged into the dropzones were not recognized
    if their paths contained spaces or special characters.
  - Cause: `tkinterdnd2` wraps such paths in curly braces `{}` (Tcl/Tk behavior),
    breaking `os.path.exists()`.
  - Fix: Paths are now cleaned before validation, allowing drag & drop from
    any folder (Desktop, Downloads, etc.), not just Unity project folders.

### Removed
- Obsolete troubleshooting note about "only using Unity PNG files" (no longer relevant).

---

## [v0.2.0] - 2025-08-05
### Refactor

- **Project Restructure**
  - Moved from flat `main.py` to modular package `src/MaskMapWizard/`.
  - Separated logic into `core/`, `gui/`, and `utils/` folders.
  - Introduced `build.py` to replace direct `pyinstaller` calls.

### Build System
- Simplified executable creation via `python build.py` (no more manual command).
- Added automatic version detection from `pyproject.toml`.

### Misc
- Updated docs (`README`, `build_instructions`) to reflect new workflow.

---
