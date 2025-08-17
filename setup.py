from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Для скрытия консоли

build_options = {
    "packages": ["tkinter"],
    "excludes": [],
    "include_files": []
}

setup(
    name="SystemLocker",
    version="1.0",
    description="Computer Lock Utility",
    options={"build_exe": build_options},
    executables=[
        Executable(
            "locker.py",
            base=base,
            target_name="SystemLocker.exe",
            icon=None  # Можно указать путь к иконке
        )
    ]
)