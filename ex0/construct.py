import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        venv_path: str | None = os.environ.get("VIRTUAL_ENV")
        if venv_path:
            print(f"Virtual Environment: {os.path.basename(venv_path)}")
            print(f"Environment Path: {venv_path}")
        print(
            "\nSUCCESS: You're in an isolated environment! Safe to install packages without affecting the global system.\n"
        )
        print(f"Package installation path:\n{site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You're in the global environment! The machines can see everything you install.\n"
        )
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
        )
        print("Then run this program again.")
