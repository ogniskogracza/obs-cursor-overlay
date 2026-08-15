import asyncio
import json
import threading
import time
import platform
from pathlib import Path

import websockets
from pynput import mouse


# ============================================================
# FILE LOCATIONS
# ============================================================

# Everything is relative to the folder containing pointer.py.
BASE_DIR = Path(__file__).resolve().parent

CURSOR_CONFIG_FILE = BASE_DIR / "cursor_config.json"
POINTER_CONFIG_FILE = BASE_DIR / "pointer_config.json"


# ============================================================
# LOAD CONFIGURATION
# ============================================================

def load_json_file(path):

    try:

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:

        print()
        print("ERROR: Configuration file not found:")
        print(path)
        print()

        raise

    except json.JSONDecodeError as error:

        print()
        print("ERROR: Invalid JSON configuration file:")
        print(path)
        print()
        print(error)
        print()

        raise


cursor_config = load_json_file(CURSOR_CONFIG_FILE)
pointer_config = load_json_file(POINTER_CONFIG_FILE)


# ============================================================
# SETTINGS
# ============================================================

HOST = "127.0.0.1"
PORT = 8765

# How frequently to send mouse coordinates.
UPDATE_INTERVAL = 1 / 60

OUTPUT_WIDTH = pointer_config["output_width"]
OUTPUT_HEIGHT = pointer_config["output_height"]


# ============================================================
# OPERATING SYSTEM
# ============================================================

OPERATING_SYSTEM = platform.system()


# ============================================================
# SCREEN DIMENSIONS
# ============================================================

def get_screen_dimensions():

    # --------------------------------------------------------
    # Windows
    # --------------------------------------------------------

    if OPERATING_SYSTEM == "Windows":

        try:

            import ctypes

            user32 = ctypes.windll.user32

            # Tell Windows that this process understands DPI scaling.
            # This prevents Windows from returning virtualised
            # dimensions on scaled displays.
            try:
                user32.SetProcessDPIAware()
            except Exception:
                pass

            width = user32.GetSystemMetrics(0)
            height = user32.GetSystemMetrics(1)

            return width, height

        except Exception as error:

            print()
            print("WARNING: Windows screen detection failed:")
            print(error)
            print()
            print("Falling back to tkinter.")
            print()


    # --------------------------------------------------------
    # macOS
    # --------------------------------------------------------

    if OPERATING_SYSTEM == "Darwin":

        try:

            import tkinter

            root = tkinter.Tk()
            root.withdraw()

            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()

            root.destroy()

            return width, height

        except Exception as error:

            print()
            print("WARNING: macOS screen detection failed:")
            print(error)
            print()
            print("Falling back to tkinter.")
            print()


    # --------------------------------------------------------
    # Linux / fallback
    # --------------------------------------------------------

    try:

        import tkinter

        root = tkinter.Tk()
        root.withdraw()

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        root.destroy()

        return width, height

    except Exception as error:

        print()
        print("ERROR: Could not determine screen dimensions.")
        print(error)
        print()

        raise RuntimeError(
            "OBS Pointer could not determine the screen dimensions."
        )


SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()

SCALE_X = OUTPUT_WIDTH / SCREEN_WIDTH
SCALE_Y = OUTPUT_HEIGHT / SCREEN_HEIGHT


# ============================================================
# MOUSE POSITION
# ============================================================

mouse_controller = mouse.Controller()

mouse_x = 0
mouse_y = 0

running = True


def read_mouse():

    global mouse_x, mouse_y

    while running:

        position = mouse_controller.position

        mouse_x = int(position[0] * SCALE_X)
        mouse_y = int(position[1] * SCALE_Y)

        time.sleep(UPDATE_INTERVAL)


# ============================================================
# WEBSOCKET
# ============================================================

async def send_mouse_position(websocket):

    # --------------------------------------------------------
    # Reload configuration from disk on every new connection.
    #
    # This means editing cursor_config.json or pointer_config.json
    # and then refreshing the OBS Browser Source is enough to see
    # the change -- pointer.py itself no longer needs restarting.
    # --------------------------------------------------------

    current_cursor_config = load_json_file(CURSOR_CONFIG_FILE)
    current_pointer_config = load_json_file(POINTER_CONFIG_FILE)

    await websocket.send(json.dumps({
        "type": "config",
        "cursor": current_cursor_config,
        "pointer": current_pointer_config
    }))


    # --------------------------------------------------------
    # Continuously send mouse coordinates.
    # --------------------------------------------------------

    while True:

        await websocket.send(json.dumps({
            "type": "mouse",
            "x": mouse_x,
            "y": mouse_y
        }))

        await asyncio.sleep(UPDATE_INTERVAL)


async def client_handler(websocket):

    try:

        # Send configuration and mouse coordinates
        # to the local Browser Source.
        await send_mouse_position(websocket)

    except websockets.exceptions.ConnectionClosed:
        pass


# ============================================================
# SERVER
# ============================================================

async def main():

    print()
    print("========================================")
    print(" OBS Pointer Mouse Server")
    print("========================================")
    print()

    print(f"Operating system: {OPERATING_SYSTEM}")
    print()

    print(f"Screen: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")
    print(f"OBS output: {OUTPUT_WIDTH} x {OUTPUT_HEIGHT}")
    print()

    print(f"Scale X: {SCALE_X:.4f}")
    print(f"Scale Y: {SCALE_Y:.4f}")
    print()

    print(f"Listening ONLY on: {HOST}:{PORT}")
    print()

    print("Authentication: DISABLED")
    print()

    print("Server is restricted to localhost.")
    print("It is NOT accessible from other")
    print("computers on your network.")
    print()

    print("Configuration:")
    print(f"  Cursor: {cursor_config['active_cursor']}")
    print(f"  Cursor config: {CURSOR_CONFIG_FILE}")
    print(f"  Pointer config: {POINTER_CONFIG_FILE}")
    print()

    print("Press Ctrl+C to stop.")
    print()

    async with websockets.serve(
        client_handler,
        HOST,
        PORT
    ):
        await asyncio.Future()


# ============================================================
# START
# ============================================================

mouse_thread = threading.Thread(
    target=read_mouse,
    daemon=True
)

mouse_thread.start()


try:

    asyncio.run(main())

except KeyboardInterrupt:

    running = False

    print()
    print("Server stopped.")