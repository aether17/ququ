#!/usr/bin/env python3
import os
import sys
import platform
import ctypes
from pathlib import Path

# ==========================================
# Configuration Area
# Format: {"New_Link_Name": "Source_File_Name"}
# All paths are relative to the project root.
# ==========================================
LINK_MAP = {
    "CLAUDE.md": "AGENTS.md",
    # Extensible: Add more links here in the future
    # "GEMINI.md": "AGENTS.md",
    # "COPILOT.md": "AGENTS.md",
}
# ==========================================

def get_project_root():
    """
    Resolve the project root directory.
    Assumes this script is located in the 'scripts/' subdirectory.
    """
    current_file = Path(__file__).resolve()
    # .parent is 'scripts/', .parent.parent is the project root
    return current_file.parent.parent

def is_admin():
    """Check if the script has administrative privileges (Windows only)."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_symlink(root_path: Path, link_name: str, source_name: str):
    """
    Create a symbolic link at the root directory.
    
    :param root_path: Path object for the project root.
    :param link_name: The name of the link to create (e.g., CLAUDE.md).
    :param source_name: The existing source file (e.g., AGENTS.md).
    """
    link_path = root_path / link_name
    source_path = root_path / source_name

    # 1. Verify source existence
    if not source_path.exists():
        print(f"[Error] Source file not found: {source_name}")
        return

    # 2. Check if target exists
    if link_path.exists() or link_path.is_symlink():
        # If it is already a symlink, check if it points to the correct source
        if link_path.is_symlink():
            try:
                target = os.readlink(link_path)
                # Compare filenames to handle potential path separators differences
                if Path(target).name == Path(source_name).name:
                    print(f"[Skip] Link already exists and is correct: {link_name} -> {source_name}")
                    return
            except OSError:
                pass
        
        # If it exists but is incorrect (or a regular file), remove it
        print(f"[Update] Removing old file/link: {link_name}")
        try:
            if link_path.is_dir():
                os.rmdir(link_path)
            else:
                os.unlink(link_path)
        except OSError as e:
            print(f"[Error] Could not remove old {link_name}: {e}")
            return

    # 3. Create the symbolic link
    try:
        # Use relative path for the source so the link remains valid if the project moves
        os.symlink(source_name, link_path)
        print(f"[Success] Created symlink: {link_name} -> {source_name}")
    except OSError as e:
        print(f"[Failure] Could not create link {link_name}")
        print(f"          Error details: {e}")
        
        # Windows-specific guidance
        if platform.system() == "Windows":
            print("\n[Windows Hint]")
            print("Creating symlinks on Windows usually requires:")
            print("1. Running this terminal as 'Administrator'.")
            print("2. Or enabling 'Developer Mode' in Windows Settings.")

def main():
    root = get_project_root()
    print(f"Project Root: {root}")
    print("-" * 40)

    # Windows Permission Check
    if platform.system() == "Windows" and not is_admin():
        print("[Note] Running on Windows without Admin privileges.")
        print("If the script fails, try running as Administrator or enable Developer Mode.\n")

    for link_name, source_name in LINK_MAP.items():
        create_symlink(root, link_name, source_name)

    print("-" * 40)
    print("Done.")

if __name__ == "__main__":
    main()