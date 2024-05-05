import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "PIL", "numpy", "modules_tk", "ultralytics", "scipy"], 
    "include_files": [("wizard-pic.ico", "wizard-pic.ico")]
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Image Wizard",
    version="1.0",
    description="Human Image Segmentor Application using Yolo",
    options={"build_exe": build_exe_options},
    executables=[Executable("Tk_app.py", base=base, icon="wizard-pic.ico")]
)
