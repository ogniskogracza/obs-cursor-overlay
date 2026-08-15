import subprocess
import sys
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# Folder containing start_pointer.py
BASE_DIR = Path(__file__).resolve().parent

# pointer.py is expected to be in the same folder.
POINTER_SCRIPT = BASE_DIR / "pointer.py"

# Python installation configured in OBS.
PYTHON_EXE = Path(sys.prefix) / "python.exe"


process = None


# ============================================================
# OBS SCRIPT
# ============================================================

def script_description():
    return "Starts and stops the local OBS Pointer mouse server."


def script_load(settings):
    global process

    if process is not None:
        return

    # --------------------------------------------------------
    # Check Python
    # --------------------------------------------------------

    if not PYTHON_EXE.exists():

        print(
            "OBS Pointer: Python executable not found:"
        )

        print(PYTHON_EXE)

        return


    # --------------------------------------------------------
    # Check pointer.py
    # --------------------------------------------------------

    if not POINTER_SCRIPT.exists():

        print(
            "OBS Pointer: pointer.py not found:"
        )

        print(POINTER_SCRIPT)

        return


    # --------------------------------------------------------
    # Start pointer.py
    # --------------------------------------------------------

    print()
    print("========================================")
    print(" OBS Pointer")
    print("========================================")

    print(f"Python:  {PYTHON_EXE}")
    print(f"Script:  {POINTER_SCRIPT}")
    print()

    process = subprocess.Popen(
        [
            str(PYTHON_EXE),
            str(POINTER_SCRIPT)
        ],

        # Run pointer.py from its own project directory.
        cwd=str(BASE_DIR),

        # Don't open a Command Prompt window.
        creationflags=subprocess.CREATE_NO_WINDOW
    )

    print(
        f"OBS Pointer: pointer.py started "
        f"(PID {process.pid})"
    )

    print()


# ============================================================
# OBS UNLOAD
# ============================================================

def script_unload():

    global process

    if process is None:
        return


    print(
        "OBS Pointer: stopping pointer.py"
    )


    try:

        process.terminate()

        process.wait(
            timeout=3
        )


    except Exception:

        try:

            process.kill()

        except Exception:

            pass


    process = None


    print(
        "OBS Pointer: pointer.py stopped"
    )