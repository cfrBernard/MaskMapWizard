import shutil
import subprocess
import sys
import tomllib  # Python 3.11+
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent
PYPROJECT_PATH = PROJECT_ROOT / "pyproject.toml"
SRC_ENTRY = PROJECT_ROOT / "src" / "MaskMapWizard" / "__main__.py"
HOOKS_DIR = PROJECT_ROOT / "hooks"
ICON_PATH = PROJECT_ROOT / "assets" / "icon.ico"
BUILD_DIR = PROJECT_ROOT / "build"
DIST_DIR = PROJECT_ROOT / "dist"
SPEC_DIR = BUILD_DIR / "specs"

ONEFILE = True  # Set to False for debugging


def read_project_metadata():
    """Read project name and version from pyproject.toml"""
    try:
        with PYPROJECT_PATH.open("rb") as f:
            data = tomllib.load(f)
        name = data["project"]["name"]
        version = data["project"]["version"]
        return name, version
    except Exception as e:
        print(f"❌ Failed to read metadata from pyproject.toml: {e}")
        sys.exit(1)


def clean_previous_builds():
    """Remove build/ and dist/ directories before a new build"""
    for folder in [BUILD_DIR, DIST_DIR]:
        if folder.exists():
            print(f"🗑️ Removing {folder}")
            shutil.rmtree(folder)


def build():
    """Run PyInstaller build command"""
    cmd = [
        "pyinstaller",
        "--name",
        BUILD_NAME,
        "--additional-hooks-dir",
        str(HOOKS_DIR),
        "--icon",
        str(ICON_PATH),
        "--noconsole",
        f"--specpath={SPEC_DIR}",
        f"--distpath={DIST_DIR}",
        f"--workpath={BUILD_DIR / 'work'}",
        str(SRC_ENTRY),
    ]

    cmd.append("--onefile" if ONEFILE else "--onedir")

    print("🔨 Building with:")
    print("   " + " ".join(cmd))
    subprocess.run(cmd, check=True)

    print(f"\n✅ Build completed: dist/{BUILD_NAME}/")


if __name__ == "__main__":
    # Read project name + version
    name, version = read_project_metadata()
    BUILD_NAME = f"{name}_v{version}"

    # Validate important files
    if not HOOKS_DIR.exists() or not (HOOKS_DIR / "hook-tkinterdnd2.py").exists():
        print("❌ Missing hook: ./hooks/hook-tkinterdnd2.py")
        sys.exit(1)

    if not ICON_PATH.exists():
        print("❌ Missing icon file: ./assets/icon.ico")
        sys.exit(1)

    # Clean and build
    clean_previous_builds()
    build()
