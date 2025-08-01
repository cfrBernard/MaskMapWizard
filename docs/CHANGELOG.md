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
