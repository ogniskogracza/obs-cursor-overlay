======================================================================
                         OBS POINTER
                 Custom Mouse Cursor for OBS
======================================================================

Copyright (c) 2026 Rafał Modzelewski
Licensed under — see LICENSE.txt
Author: Rafal Modzelewski
Contact: ogniskogracza@gmail.com
Version: 1.0
Supported: Windows, macOS and Linux
OBS: Windows / macOS / Linux
Designed for: OBS Studio
Python: 3.10+
Connection: Localhost WebSocket
Authentication: Disabled
======================================================================


1. WHAT IS OBS POINTER?
======================================================================

OBS Pointer is a small local application that displays a custom mouse
cursor inside an OBS Browser Source.

It is useful when recording or streaming:

    - PlayStation gameplay
    - PC gameplay
    - tutorials
    - desktop applications
    - presentations
    - software demonstrations
    - educational content
    - any other content where you want the viewer to clearly see
      where the mouse is pointing


The system works by:

    1. Detecting the operating system.

    2. Reading the computer's mouse position.

    3. Detecting the computer's desktop dimensions.

    4. Converting the mouse coordinates to the configured OBS
       output resolution.

    5. Sending the coordinates through a local WebSocket connection.

    6. OBS Browser Source receives those coordinates.

    7. pointer.html displays the selected SVG cursor.

    8. The cursor automatically disappears after the mouse stops
       moving.


The cursor shown to the viewer is completely independent from the
normal operating-system mouse cursor.

Changing the SVG file therefore does NOT change the normal Windows,
macOS or Linux mouse cursor.


======================================================================
2. CROSS-PLATFORM SUPPORT
======================================================================

OBS Pointer is designed to work on:

    Windows
    macOS
    Linux


The same pointer.py file is used on all supported operating systems.

The application detects the operating system automatically.

The Python code does NOT require separate versions such as:

    pointer_windows.py
    pointer_macos.py
    pointer_linux.py


Instead, pointer.py selects the appropriate operating-system-specific
method when it starts.


----------------------------------------------------------------------
2.1 MOUSE INPUT
----------------------------------------------------------------------

Mouse input is handled using:

    pynput


pynput provides a cross-platform interface for reading the mouse
position.

The main mouse-tracking code is therefore shared between Windows,
macOS and Linux.


----------------------------------------------------------------------
2.2 SCREEN DETECTION
----------------------------------------------------------------------

The computer's screen dimensions are detected using an
operating-system-appropriate method.

Windows uses the Windows display API.

macOS uses the available macOS desktop information.

Linux uses the available desktop/display information with a
cross-platform fallback.


The detected screen dimensions are then used to convert the mouse
position to the OBS output resolution.


----------------------------------------------------------------------
2.3 macOS RETINA DISPLAYS
----------------------------------------------------------------------

macOS Retina displays can expose a distinction between logical
display points and physical pixels.

Because of this, certain Retina configurations may require additional
testing or adjustment.

The application is designed to use the coordinate system exposed by
the operating system rather than applying Windows-specific DPI logic
to macOS.


If a particular Retina configuration produces incorrect scaling or
offsets, this can be addressed in the macOS-specific screen detection
code without changing the overall architecture.


======================================================================
3. HOW THE SYSTEM IS STRUCTURED
======================================================================

The project consists of several separate parts.


    pointer.py
        The cross-platform mouse tracking server.

        It detects the operating system, reads the mouse position,
        determines the screen dimensions, converts the coordinates
        to the OBS output resolution and sends them to the Browser
        Source.

        Normally you should NOT need to edit this file.


    pointer.html
        The visual cursor displayed by OBS.

        It receives mouse coordinates and configuration from
        pointer.py and displays the selected SVG cursor.

        Normally you should NOT need to edit this file.


    cursor_config.json
        USER CURSOR CONFIGURATION.

        This is the main file you edit when you want to:

            - change the active cursor
            - change the glow colour
            - change glow intensity
            - change glow speed
	    - change glow style (default is "blur", can also be set as "halo"), if param is omitted it considers selection is "blur"
            - configure glow behaviour for individual cursors

Example:
"pointers/skeleton_hand.svg": {
    "color": "rgba(49, 239, 44, 0.9)",
    "min": "40px",
    "max": "250px",
    "speed": "5s",
    "style": "halo",
    "trough": 0.55,
    "trough_opacity": 0
}


    pointer_config.json
        GENERAL POINTER CONFIGURATION.

        This controls:

            - pointer width
            - pointer height
            - fade duration
            - automatic hide delay
            - OBS output width
            - OBS output height
            - cursor tip X position
            - cursor tip Y position


    start_pointer.py
        OBS Python helper script.

        OBS loads this script automatically and it starts
        pointer.py.

        This means you do not normally need to manually start
        pointer.py before opening OBS.


    README.txt
        This documentation.


    pointers/
        Folder containing the SVG cursor files.


======================================================================
4. REQUIRED FOLDER STRUCTURE
======================================================================

The entire project should be kept together in one folder.

Example:

    OBS-Pointer/


Inside that folder:

    OBS-Pointer/
    |
    +-- pointer.py
    |
    +-- pointer.html
    |
    +-- cursor_config.json
    |
    +-- pointer_config.json
    |
    +-- start_pointer.py
    |
    +-- README.txt
    |
    +-- pointers/
         |
         +-- crystal_blue_sword.svg
         +-- arrow.svg
         +-- staff.svg
         +-- skeleton_hand.svg


IMPORTANT:

Do not move individual files out of this folder unless you also
understand which configuration references them.

The project is designed to be PORTABLE.


----------------------------------------------------------------------
4.1 PORTABLE PATHS
----------------------------------------------------------------------

The Python application does not contain a hard-coded path to the
project directory.

The configuration files are located relative to pointer.py.

For example, the complete project can be placed at:

    C:\OBS-Pointer\

or:

    D:\Streaming\OBS-Pointer\

or:

    C:\Users\Someone\Desktop\OBS-Pointer\


On macOS:

    /Users/Someone/OBS-Pointer/


On Linux:

    /home/someone/OBS-Pointer/


The complete folder can be copied to another computer.

The project files themselves do not need to be edited just because
the project directory has moved.


NOTE:

The OBS Browser Source still needs to point to the correct location
of pointer.html on the new computer.


======================================================================
5. INSTALLING PYTHON
======================================================================

OBS Pointer requires Python 3.10 or newer.

Python can be downloaded from:

    https://www.python.org/


A recent Python 3 release is recommended.


----------------------------------------------------------------------
5.1 WINDOWS
----------------------------------------------------------------------

Download Python for Windows.

During installation, enable:

    Add Python to PATH


if this option is offered.


----------------------------------------------------------------------
5.2 macOS
----------------------------------------------------------------------

Install a current Python 3 version appropriate for your Mac.

After installation, open Terminal and check:

    python3 --version


Depending on the Python installation, the command may also be:

    python --version


----------------------------------------------------------------------
5.3 LINUX
----------------------------------------------------------------------

Install Python 3 using your Linux distribution's normal package
manager if it is not already installed.

Then check:

    python3 --version


======================================================================
6. CHECKING PYTHON
======================================================================

The command used to check Python depends on the operating system.


Windows:

    python --version


If that does not work:

    py --version


macOS:

    python3 --version


Linux:

    python3 --version


You should see something similar to:

    Python 3.10.x

or:

    Python 3.11.x

or:

    Python 3.12.x


Python 3.10 or newer is recommended.


======================================================================
7. INSTALLING REQUIRED PYTHON PACKAGES
======================================================================

OBS Pointer requires two external Python packages:

    pynput
    websockets


----------------------------------------------------------------------
7.1 WINDOWS
----------------------------------------------------------------------

Open Command Prompt.

Go to the OBS-Pointer folder.

Example:

    cd C:\OBS-Pointer


Then install:

    python -m pip install pynput websockets


Alternatively:

    python -m pip install pynput

    python -m pip install websockets


----------------------------------------------------------------------
7.2 macOS
----------------------------------------------------------------------

Open Terminal.

Go to the OBS-Pointer folder.

Example:

    cd /Users/Someone/OBS-Pointer


Install:

    python3 -m pip install pynput websockets


----------------------------------------------------------------------
7.3 LINUX
----------------------------------------------------------------------

Open Terminal.

Go to the OBS-Pointer folder.

Example:

    cd /home/someone/OBS-Pointer


Install:

    python3 -m pip install pynput websockets


======================================================================
8. TESTING THE POINTER SERVER
======================================================================

Before configuring OBS, it is recommended to test the server
manually.

This confirms that Python, pynput, websockets and the mouse/screen
detection are working correctly.


----------------------------------------------------------------------
8.1 WINDOWS
----------------------------------------------------------------------

Open Command Prompt.

Go to the project folder:

    cd C:\OBS-Pointer


Run:

    python pointer.py


----------------------------------------------------------------------
8.2 macOS / LINUX
----------------------------------------------------------------------

Open Terminal.

Go to the project folder:

    cd /path/to/OBS-Pointer


Run:

    python3 pointer.py


----------------------------------------------------------------------
8.3 EXPECTED OUTPUT
----------------------------------------------------------------------

You should see something similar to:

    ========================================
     OBS Pointer Mouse Server
    ========================================

    Operating system: Windows

    Screen: 1920 x 1080
    OBS output: 1920 x 1080

    Scale X: 1.0000
    Scale Y: 1.0000

    Listening ONLY on: 127.0.0.1:8765

    Authentication: DISABLED

    Server is restricted to localhost.
    It is NOT accessible from other
    computers on your network.

    Configuration:
      Cursor: pointers/crystal_blue_sword.svg
      Cursor config: ...
      Pointer config: ...

    Press Ctrl+C to stop.


The exact operating-system name, screen dimensions and scaling values
will depend on the computer.


If you see this, the server is running correctly.


To stop the server:

    Press Ctrl+C


======================================================================
9. SECURITY / LOCAL CONNECTION
======================================================================

The WebSocket server listens on:

    127.0.0.1:8765


127.0.0.1 means:

    "this computer"


The server is NOT listening on:

    0.0.0.0


and therefore is not intended to accept connections from other
computers on the network.


Authentication is intentionally disabled.

This is acceptable because the service is restricted to localhost.


The Browser Source connects to:

    ws://127.0.0.1:8765


The WebSocket is used only for communication between:

    pointer.py

and:

    pointer.html


No external server is required.


======================================================================
10. HOW THE MOUSE POSITION WORKS
======================================================================

OBS Pointer automatically detects the computer's operating system.


The general process is:

    Physical desktop
          |
          v
    Operating system
          |
          v
    pynput mouse position
          |
          v
    Coordinate conversion
          |
          v
    OBS output resolution
          |
          v
    Browser Source


For example, the physical desktop might be:

    2560 x 1440


while OBS might use:

    1920 x 1080


The application proportionally converts:

    Desktop X -> OBS X

    Desktop Y -> OBS Y


This allows the cursor to reach the correct edges and corners of the
OBS canvas.


The target OBS resolution is controlled by:

    pointer_config.json


For example:

    "output_width": 1920,
    "output_height": 1080


The conversion is performed automatically.

Users should NOT manually compensate for Windows display scaling.


======================================================================
11. POINTER CONFIGURATION
======================================================================

General pointer behaviour is controlled through:

    pointer_config.json


The default file is:

    {
        "pointer_width": 90,
        "pointer_height": 90,

        "fade_duration": "0.45s",

        "hide_delay": 5.0,

        "output_width": 1920,
        "output_height": 1080,

        "tip_x": 8,
        "tip_y": 8
    }


The values are described below.


----------------------------------------------------------------------
11.1 POINTER WIDTH
----------------------------------------------------------------------

Example:

    "pointer_width": 90


This controls the width of the cursor container in pixels.


For example:

    "pointer_width": 120


creates a wider pointer container.


The SVG artwork is scaled to fill this container.


----------------------------------------------------------------------
11.2 POINTER HEIGHT
----------------------------------------------------------------------

Example:

    "pointer_height": 90


This controls the height of the cursor container.


For example:

    "pointer_height": 120


creates a taller pointer container.


Normally:

    pointer_width

and:

    pointer_height


should be kept equal unless you deliberately want to stretch the
cursor.


----------------------------------------------------------------------
11.3 FADE DURATION
----------------------------------------------------------------------

Example:

    "fade_duration": "0.45s"


This controls how quickly the cursor fades in and out.


Faster:

    "fade_duration": "0.2s"


Slower:

    "fade_duration": "1s"


The value uses CSS time notation.


----------------------------------------------------------------------
11.4 HIDE DELAY
----------------------------------------------------------------------

Example:

    "hide_delay": 5.0


This is the number of seconds after the last mouse movement before
the cursor disappears.


For example:

    "hide_delay": 3.0


means the cursor disappears after approximately 3 seconds.


A value of:

    "hide_delay": 10.0


keeps it visible for approximately 10 seconds.


----------------------------------------------------------------------
11.5 OUTPUT WIDTH
----------------------------------------------------------------------

Example:

    "output_width": 1920


This specifies the width of the OBS output/canvas coordinate system.


For a standard Full HD OBS setup:

    1920


is normally appropriate.


----------------------------------------------------------------------
11.6 OUTPUT HEIGHT
----------------------------------------------------------------------

Example:

    "output_height": 1080


For a standard Full HD OBS setup:

    1080


is normally appropriate.


IMPORTANT:

The Browser Source dimensions should match these values.


For example:

    pointer_config.json:

        "output_width": 1920,
        "output_height": 1080


OBS Browser Source:

        Width: 1920
        Height: 1080


----------------------------------------------------------------------
11.7 TIP X / TIP Y
----------------------------------------------------------------------

Example:

    "tip_x": 8,
    "tip_y": 8


These values define the location of the actual mouse pointer tip
inside the SVG artwork.


The system positions the SVG container so that:

    tip_x
    tip_y


lands exactly on the real mouse coordinate.


For the supplied cursor artwork the standard convention is:

    X = 8
    Y = 8


This allows different cursor designs to be swapped without changing
the mouse tracking system.


======================================================================
12. CURSOR CONFIGURATION
======================================================================

Cursor selection and glow settings are controlled through:

    cursor_config.json


Example:

    {
        "active_cursor": "pointers/crystal_blue_sword.svg",

        "default_glow": {
            "color": "rgba(70, 190, 255, 0.8)",
            "min": "3px",
            "max": "10px",
            "speed": "2.6s"
        },

        "cursors": {
            ...
        }
    }


======================================================================
13. CHANGING THE ACTIVE CURSOR
======================================================================

Open:

    cursor_config.json


Look for:

    "active_cursor"


Example:

    "active_cursor": "pointers/crystal_blue_sword.svg"


To use the arrow:

    "active_cursor": "pointers/arrow.svg"


To use the staff:

    "active_cursor": "pointers/staff.svg"


To use the skeleton hand:

    "active_cursor": "pointers/skeleton_hand.svg"


Save the file.


======================================================================
14. APPLYING A CURSOR CHANGE
======================================================================

You do NOT need to:

    - restart OBS
    - restart pointer.py
    - restart start_pointer.py


After changing cursor_config.json:

    1. Save cursor_config.json.

    2. Return to OBS.

    3. Right-click the OBS Pointer Browser Source.

    4. Select:

           Refresh


The Browser Source reloads pointer.html.

The new configuration is then loaded.


The cursor configuration is deliberately loaded with cache-busting
and cache disabled so OBS/Chromium is not expected to reuse an old
version of the JSON configuration.


======================================================================
15. CHANGING THE GLOW
======================================================================

Glow settings are also controlled through:

    cursor_config.json


Each cursor can have its own:

    color
    min
    max
    speed


Example:

    "pointers/crystal_blue_sword.svg": {

        "color": "rgba(70, 190, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


======================================================================
16. GLOW COLOR
======================================================================

The colour is written using CSS rgba notation.


Example:

    rgba(70, 190, 255, 0.8)


The first three numbers represent:

    Red
    Green
    Blue


The last number represents:

    Opacity


Examples:


Blue:

    rgba(70, 190, 255, 0.8)


Red:

    rgba(255, 60, 60, 0.8)


Green:

    rgba(80, 255, 120, 0.8)


White:

    rgba(255, 255, 255, 0.8)


Purple:

    rgba(180, 80, 255, 0.8)


======================================================================
17. MINIMUM GLOW
======================================================================

Example:

    "min": "3px"


This is the smallest glow during the animation.


Smaller:

    "min": "1px"


means a subtler starting glow.


Larger:

    "min": "6px"


means the cursor always has a stronger glow.


======================================================================
18. MAXIMUM GLOW
======================================================================

Example:

    "max": "10px"


This controls how large the glow becomes at the peak of the
animation.


Example:

    "max": "5px"


creates a very subtle effect.


Example:

    "max": "15px"


creates a much stronger effect.


======================================================================
19. GLOW SPEED
======================================================================

Example:

    "speed": "2.6s"


This controls the length of one complete glow pulse.


Smaller:

    "speed": "1.5s"


means faster pulsing.


Larger:

    "speed": "4s"


means slower pulsing.


For a calm, subtle effect, approximately:

    2.5 - 4 seconds


is recommended.


======================================================================
20. DEFAULT GLOW
======================================================================

cursor_config.json also contains:

    "default_glow"


Example:

    "default_glow": {

        "color": "rgba(70, 190, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


This configuration is used when an individual cursor does not have
its own glow configuration.


This allows new cursors to work without requiring a dedicated glow
entry.


======================================================================
21. ADDING A NEW CURSOR
======================================================================

To add a new cursor:


    1. Create or obtain an SVG file.


    2. Put the SVG inside:

           pointers/


    3. Make sure the SVG follows the pointer requirements.


    4. Add its path to cursor_config.json.


Example:

    pointers/my_new_cursor.svg


Then add:

    "pointers/my_new_cursor.svg": {

        "color": "rgba(255, 255, 255, 0.8)",
        "min": "3px",
        "max": "10px",
        "speed": "2.6s"

    }


Then make it active:

    "active_cursor": "pointers/my_new_cursor.svg"


Save the file.


Refresh the Browser Source.


======================================================================
22. SVG CURSOR REQUIREMENTS
======================================================================

Every cursor SVG should follow the common coordinate convention.


The SVG should use:

    viewBox="0 0 90 90"


The pointer tip should normally be located at:

    X = 8
    Y = 8


This point is treated as the actual mouse position.


The rest of the artwork is drawn around that point.


For example, a sword pointing toward the upper-left should have its
blade/tip aligned with the (8,8) point.


This convention allows completely different cursor designs to be
swapped without changing pointer.py or pointer.html.


======================================================================
23. CURSOR SIZE
======================================================================

The default pointer container is:

    90 x 90 pixels


This is controlled through:

    pointer_config.json


For example:

    "pointer_width": 90,
    "pointer_height": 90


The SVG fills this container.


Therefore SVG artwork should normally be designed within:

    0 - 90 X
    0 - 90 Y


The mouse position is anchored to:

    (8,8)


unless tip_x and tip_y have deliberately been changed in
pointer_config.json.


======================================================================
24. SVG GLOW VS OUTER OBS POINTER GLOW
======================================================================

A cursor can have two different types of glow.


----------------------------------------------------------------------
24.1 BAKED-IN SVG GLOW
----------------------------------------------------------------------

The SVG itself can contain:

    gradients
    filters
    drop shadows
    glow effects


This glow belongs to the artwork.


For example, a crystal-blue sword may have a blue glow directly
around its blade.


----------------------------------------------------------------------
24.2 OUTER OBS POINTER GLOW
----------------------------------------------------------------------

pointer.html adds another animated glow around the cursor.


This is controlled by:

    cursor_config.json


The two effects can therefore work together.


For example:

    SVG:
        blue glow around the sword blade

    HTML:
        soft blue breathing glow around the whole sword


This allows each cursor to have its own visual character.


======================================================================
25. CONFIGURATION FILE RESPONSIBILITIES
======================================================================

The project deliberately separates configuration into two JSON files.


----------------------------------------------------------------------
25.1 cursor_config.json
----------------------------------------------------------------------

Controls:

    - active cursor
    - cursor-specific glow
    - default glow


This is the file most users will edit.


----------------------------------------------------------------------
25.2 pointer_config.json
----------------------------------------------------------------------

Controls:

    - pointer width
    - pointer height
    - fade duration
    - hide delay
    - output width
    - output height
    - cursor tip X
    - cursor tip Y


This file is intended for users who want to customise the general
pointer behaviour.


----------------------------------------------------------------------
25.3 WHY TWO FILES?
----------------------------------------------------------------------

The two configuration files have different responsibilities.


cursor_config.json answers:

    "What cursor should I display and how should it glow?"


pointer_config.json answers:

    "How should the pointer system itself behave?"


This prevents everyday visual configuration from becoming mixed with
the technical mouse-tracking code.


======================================================================
26. CONFIGURATION IS SENT THROUGH THE LOCAL WEBSOCKET
======================================================================

When pointer.html connects to pointer.py, the server first sends
configuration information.


The Browser Source receives:

    cursor configuration

and:

    pointer configuration


It then receives mouse coordinates continuously.


The general communication sequence is:

    Browser Source connects
             |
             v
        pointer.py
             |
             v
       configuration
             |
             v
       mouse coordinates
             |
             v
       pointer.html


This means pointer.html does not need to contain hard-coded
configuration values.


======================================================================
27. CONFIGURATION ERROR HANDLING
======================================================================

If cursor_config.json cannot be loaded correctly, pointer.html
reports a descriptive error to the Browser Source console.


Possible causes include:

    - missing JSON file
    - invalid JSON
    - missing active_cursor
    - incorrect cursor path
    - malformed glow configuration


The error is intentionally made visible in the Browser Source
console rather than failing silently.


======================================================================
28. CONFIGURING OBS PYTHON
======================================================================

OBS needs to know where Python is installed.


Open OBS Studio.


Go to:

    Tools
        ->
    Scripts


You should see the OBS scripting window.


Go to the Python Settings area.


Select the Python installation directory.


Example on Windows:

    C:\Users\USERNAME\AppData\Local\Programs\Python\Python310


IMPORTANT:

Select the Python installation folder, not the python.exe file,
unless your OBS version specifically asks for the executable.


OBS should report something similar to:

    Loaded Python version 3.10


The exact wording depends on the OBS version.


======================================================================
29. ADDING THE AUTOMATIC START SCRIPT TO OBS
======================================================================

In OBS:

    Tools
        ->
    Scripts


Click:

    +


Select:

    start_pointer.py


The script should produce messages similar to:

    ========================================
     OBS Pointer
    ========================================

    Python:
    C:\Users\USERNAME\AppData\Local\Programs\Python\Python310\python.exe

    Script:
    C:\OBS-Pointer\pointer.py

    OBS Pointer: pointer.py started


This means OBS successfully started pointer.py.


You should NOT manually run pointer.py at the same time.


If OBS is responsible for starting pointer.py, let OBS manage it.


======================================================================
30. AUTOMATIC STARTUP
======================================================================

Once start_pointer.py has been added to OBS, OBS will load the script
when OBS starts.


The helper script starts pointer.py automatically.


Therefore the normal workflow becomes:


    Start OBS
        |
        v
    OBS loads start_pointer.py
        |
        v
    start_pointer.py starts pointer.py
        |
        v
    pointer.py detects the operating system
        |
        v
    pointer.py starts mouse tracking
        |
        v
    Browser Source connects to localhost
        |
        v
    Configuration is sent
        |
        v
    Custom cursor appears when mouse moves


You should not need to open Command Prompt or Terminal and run
pointer.py manually during normal use.


======================================================================
31. ADDING THE BROWSER SOURCE
======================================================================

Open OBS Studio.


Select the scene where you want the custom cursor.


In the Sources panel:

    Add
        ->
    Browser


Create a new Browser Source.


Give it a name such as:

    OBS Pointer


Set the URL to the local pointer.html file.


Windows example:

    file:///C:/OBS-Pointer/pointer.html


Another Windows example:

    file:///D:/Streaming/OBS-Pointer/pointer.html


macOS example:

    file:///Users/Someone/OBS-Pointer/pointer.html


Linux example:

    file:///home/someone/OBS-Pointer/pointer.html


Use the correct path for your computer.


Set the Browser Source dimensions to match:

    pointer_config.json


For the default configuration:

    Width: 1920
    Height: 1080


The Browser Source background is transparent.


Therefore it should not cover your gameplay or camera.


======================================================================
32. BROWSER SOURCE POSITION
======================================================================

The Browser Source should normally be positioned at:

    X: 0
    Y: 0


and should fill the entire OBS canvas.


If your OBS canvas is:

    1920 x 1080


the Browser Source should also be:

    1920 x 1080


Do not resize the Browser Source to the size of your gameplay
window.


The pointer coordinates are based on the complete OBS canvas.


======================================================================
33. IMPORTANT: ADD THE POINTER ONLY TO RELEVANT SCENES
======================================================================

The OBS Pointer Browser Source is an overlay.


If the Browser Source is added to a scene showing the computer's
desktop, the normal operating-system mouse cursor may also be visible.


This can result in:

    normal OS cursor
           +
    OBS Pointer cursor


appearing at the same time.


This is expected.


For example, if OBS is being used to stream PlayStation 5 gameplay,
the PS5 itself does not have the computer's mouse cursor.


The OBS Pointer overlay therefore provides a useful custom cursor
inside the gameplay scene.


However, if a separate scene displays the Windows/macOS/Linux desktop,
the normal operating-system cursor may also be visible.


The simple solution is:

    Do not add the OBS Pointer Browser Source to scenes where you
    want to display the computer's normal desktop cursor.


For example:


    Scene - PS5 Gameplay
        |
        +-- Gameplay
        +-- Camera
        +-- OBS Pointer


    Scene - Desktop
        |
        +-- Desktop Capture
        +-- Camera
        |
        +-- NO OBS Pointer


This allows the custom pointer to be used only where it is useful.


======================================================================
34. TESTING THE CURSOR
======================================================================

Move the computer mouse.


The custom cursor should appear in OBS.


When the mouse stops moving for approximately:

    5 seconds


the custom cursor disappears.


When the mouse moves again, it appears again.


The exact delay is controlled by:

    pointer_config.json


using:

    "hide_delay"


The cursor should be able to reach:

    top-left
    top-right
    bottom-left
    bottom-right


of the OBS canvas.


======================================================================
35. CURSOR CHANGE WITHOUT RESTARTING OBS
======================================================================

You can change the active cursor while OBS is running.


Steps:


    1. Open cursor_config.json.


    2. Change:

           "active_cursor"


    3. Save the file.


    4. Return to OBS.


    5. Right-click the OBS Pointer Browser Source.


    6. Select:

           Refresh


The cursor should change immediately.


You do NOT need to:

    - restart OBS
    - restart pointer.py
    - reload start_pointer.py


======================================================================
36. CHANGING POINTER CONFIGURATION
======================================================================

pointer_config.json is also read when the Browser Source connects.


If you change:

    pointer_width
    pointer_height
    fade_duration
    hide_delay
    output_width
    output_height
    tip_x
    tip_y


save the file and refresh the Browser Source.


The Python mouse server does not normally need to be restarted for
these changes to be sent to a newly refreshed Browser Source.


NOTE:

Because output_width and output_height are used by pointer.py for
coordinate conversion, changing them while pointer.py is already
running may require restarting pointer.py so that the Python server
uses the new values.


Therefore after changing:

    output_width

or:

    output_height


restart pointer.py if necessary.


For ordinary visual changes such as:

    pointer_width
    pointer_height
    fade_duration
    hide_delay
    tip_x
    tip_y


refreshing the Browser Source is sufficient.


======================================================================
37. TROUBLESHOOTING
======================================================================


----------------------------------------------------------------------
37.1 CURSOR DOES NOT APPEAR
----------------------------------------------------------------------

Check:


    1. Is pointer.py running?


    2. Is start_pointer.py loaded in:

           Tools -> Scripts


    3. Does the OBS script log say:

           pointer.py started


    4. Is the Browser Source present?


    5. Is the Browser Source set to the same dimensions as
       pointer_config.json?


    6. Does the Browser Source point to:

           pointer.html


    7. Is the Browser Source visible in the current scene?


    8. Try:

           Right-click Browser Source -> Refresh



----------------------------------------------------------------------
37.2 CURSOR APPEARS BUT DOES NOT MOVE
----------------------------------------------------------------------

Check that pointer.py is running.


You can test manually.


Windows:

    cd C:\Your\Path\OBS-Pointer

    python pointer.py


macOS/Linux:

    cd /Your/Path/OBS-Pointer

    python3 pointer.py


You should see:

    Listening ONLY on: 127.0.0.1:8765


If pointer.py is running and the Browser Source still does not move,
refresh the Browser Source.


----------------------------------------------------------------------
37.3 CURSOR IS OFFSET FROM THE MOUSE
----------------------------------------------------------------------

Make sure:


    Browser Source width
        =
    pointer_config.json output_width


and:


    Browser Source height
        =
    pointer_config.json output_height


Also make sure:


    Browser Source position X = 0

    Browser Source position Y = 0


The OBS canvas should use the same output dimensions configured in
pointer_config.json.


Also check:

    tip_x
    tip_y


These values control where the actual cursor tip is located inside
the SVG artwork.


----------------------------------------------------------------------
37.4 CURSOR DOES NOT REACH THE EDGES
----------------------------------------------------------------------

Check that pointer.py is using the current cross-platform
coordinate scaling code.


The current version automatically detects the screen dimensions and
converts them to the configured OBS output resolution.


Do not manually add offsets unless you have deliberately changed
the architecture.


If the issue occurs only on a particular macOS Retina configuration,
the display coordinate system may need platform-specific adjustment.


----------------------------------------------------------------------
37.5 CURSOR CHANGE DOES NOT APPEAR
----------------------------------------------------------------------

After changing cursor_config.json:


    Right-click Browser Source
        ->
    Refresh


You do NOT need to restart OBS.


The Browser Source deliberately loads the current configuration
rather than relying on a previous cached copy.


----------------------------------------------------------------------
37.6 JSON ERROR
----------------------------------------------------------------------

If a JSON file contains invalid JSON, configuration loading may fail.


Common mistakes:


Missing comma:

    "speed": "2.6s"
    "other": "value"


Correct:

    "speed": "2.6s",
    "other": "value"


Using single quotes:

    'active_cursor': 'pointers/arrow.svg'


JSON requires double quotes:

    "active_cursor": "pointers/arrow.svg"


If the configuration cannot be loaded, pointer.py reports the
configuration error in the terminal.


Browser Source configuration errors are also reported in the
Browser Source console.


----------------------------------------------------------------------
37.7 PYTHON TAB / INDENTATION ERROR
----------------------------------------------------------------------

Python requires consistent indentation.


Do not mix tabs and spaces.


If you see:


    TabError: inconsistent use of tabs and spaces in indentation


replace the affected file with the official project version rather
than manually changing random indentation.


----------------------------------------------------------------------
37.8 PYTHON PACKAGE ERROR
----------------------------------------------------------------------

If you see:


    ModuleNotFoundError: No module named 'websockets'


install:

    python -m pip install websockets


or on macOS/Linux:

    python3 -m pip install websockets


If you see:


    ModuleNotFoundError: No module named 'pynput'


install:

    python -m pip install pynput


or:

    python3 -m pip install pynput


----------------------------------------------------------------------
37.9 PORT 8765 IS ALREADY IN USE
----------------------------------------------------------------------

If pointer.py reports that port 8765 cannot be opened, another
application may already be using the port.


Normally this means another copy of pointer.py is already running.


Check that you have not:

    - manually started pointer.py
    - while OBS is already running its automatic copy


Stop the extra copy.


Only one pointer.py server should normally run at a time.


----------------------------------------------------------------------
37.10 POINTER.PY STARTS THEN IMMEDIATELY STOPS
----------------------------------------------------------------------

Check the terminal or OBS script log for the error.


Common causes include:


    - missing Python package
    - invalid JSON
    - missing configuration file
    - unavailable screen information
    - port 8765 already being used
    - incorrect Python installation


Run pointer.py manually to see the complete error message.


======================================================================
38. TESTING WITHOUT OBS
======================================================================

You can test the Python server independently.


Windows:

    cd C:\Folder\OBS-Pointer

    python pointer.py


macOS/Linux:

    cd /Folder/OBS-Pointer

    python3 pointer.py


If the server starts successfully, Python, the required packages,
configuration files and screen/mouse detection are working.


The server will continue running until:

    Ctrl+C


======================================================================
39. NORMAL DAILY WORKFLOW
======================================================================

Once everything has been configured, normal usage is simple.


    1. Start OBS.


    2. OBS automatically starts pointer.py through
       start_pointer.py.


    3. Select the scene containing the OBS Pointer Browser Source.


    4. Move the mouse.


    5. The custom cursor appears.


    6. Stop moving the mouse.


    7. The cursor disappears after the configured delay.


No Command Prompt or Terminal is normally required.


======================================================================
40. CHANGING CURSORS DURING A STREAM / RECORDING
======================================================================

You can change the cursor while OBS is running.


Steps:


    1. Open cursor_config.json.


    2. Change:

           "active_cursor"


    3. Save the file.


    4. Return to OBS.


    5. Right-click the Browser Source.


    6. Select Refresh.


The cursor should change immediately.


The Python mouse server does not need to be restarted.


======================================================================
41. MOVING THE PROJECT TO ANOTHER COMPUTER
======================================================================

The project is designed to be portable.


Copy the entire folder:

    OBS-Pointer/


to the other computer.


Install:

    Python 3.10+


and:

    pynput
    websockets


Then configure OBS Python scripting to use the Python installation
on that computer.


Add:

    start_pointer.py


to OBS.


Finally add:

    pointer.html


as a Browser Source.


The Python application does not contain a hard-coded project path.


The application automatically detects the operating system.


======================================================================
42. WHAT YOU SHOULD NORMALLY EDIT
======================================================================

For everyday use:


    EDIT:

        cursor_config.json


    POSSIBLY EDIT:

        pointer_config.json


    POSSIBLY EDIT:

        pointers/*.svg


    DO NOT NORMALLY EDIT:

        pointer.py
        pointer.html
        start_pointer.py


The project deliberately separates user configuration from program
code.


======================================================================
43. QUICK REFERENCE
======================================================================

START OBS:

    OBS automatically starts pointer.py.


CHANGE CURSOR:

    Edit:

        cursor_config.json


    Change:

        "active_cursor"


APPLY CURSOR CHANGE:

    OBS:

        Right-click Browser Source
            ->
        Refresh


CHANGE GLOW:

    Edit the cursor's:

        color
        min
        max
        speed


CHANGE POINTER SIZE:

    Edit:

        pointer_config.json


    Change:

        pointer_width
        pointer_height


CHANGE HIDE DELAY:

    Edit:

        hide_delay


CHANGE FADE:

    Edit:

        fade_duration


CHANGE CURSOR TIP:

    Edit:

        tip_x
        tip_y


ADD CURSOR:

    Put SVG in:

        pointers/


    Add its configuration to:

        cursor_config.json


TEST PYTHON:

    Windows:

        python pointer.py


    macOS/Linux:

        python3 pointer.py


INSTALL PACKAGES:

    Windows:

        python -m pip install pynput websockets


    macOS/Linux:

        python3 -m pip install pynput websockets


STOP MANUAL SERVER:

    Ctrl+C


WEBSOCKET:

    ws://127.0.0.1:8765


DEFAULT OBS BROWSER SOURCE:

    Width: 1920
    Height: 1080


DEFAULT POINTER:

    Width: 90
    Height: 90


DEFAULT HIDE DELAY:

    5 seconds


DEFAULT SVG:

    viewBox:

        0 0 90 90


DEFAULT SVG MOUSE TIP:

    (8,8)


======================================================================
44. CURRENT PROJECT ARCHITECTURE
======================================================================

The final system is intentionally split into independent layers:


                         OPERATING SYSTEM
                       /        |        \
                      /         |         \
                 Windows      macOS      Linux
                      \         |         /
                       \        |        /
                        +-------+-------+
                                |
                                v
                         pynput mouse
                                |
                                v
                           pointer.py
                                |
                                |
                                | WebSocket
                                | 127.0.0.1:8765
                                |
                                v
                           pointer.html
                                |
                  +-------------+-------------+
                  |                           |
                  v                           v
          cursor_config.json         pointer_config.json
                  |                           |
                  |                           |
                  +-------------+-------------+
                                |
                                v
                         SVG cursor artwork
                                |
                                v
                         OBS Browser Source
                                |
                                v
                         STREAM / RECORDING


This separation is intentional.


The operating system provides the mouse and desktop information.


pynput provides cross-platform mouse access.


pointer.py:

    - detects the operating system
    - detects screen dimensions
    - reads the mouse position
    - converts coordinates
    - provides the WebSocket server
    - sends configuration


pointer.html:

    - receives configuration
    - receives coordinates
    - positions the cursor
    - applies the visual effects
    - handles automatic hiding


cursor_config.json:

    - controls which cursor is displayed
    - controls cursor glow


pointer_config.json:

    - controls pointer dimensions
    - controls animation behaviour
    - controls hide delay
    - controls output resolution
    - controls cursor tip position


SVG files:

    - contain the actual cursor artwork


OBS:

    - displays the Browser Source
    - combines it with gameplay, camera and other sources
    - sends the resulting scene to the stream or recording


======================================================================
45. IMPORTANT DESIGN RULES
======================================================================

When extending the project, try to preserve these principles:


    1. Keep pointer.py focused on mouse tracking,
       coordinate conversion and the local WebSocket server.


    2. Keep pointer.html focused on displaying the cursor.


    3. Keep cursor selection and glow settings in JSON.


    4. Keep general pointer behaviour in pointer_config.json.


    5. Keep SVG artwork inside the pointers/ folder.


    6. Keep the project portable.


    7. Avoid hard-coded computer-specific paths.


    8. Keep the WebSocket restricted to localhost.


    9. Keep all cursor SVGs aligned to the common tip convention.


    10. Keep operating-system-specific processing isolated inside
        pointer.py rather than creating separate application
        versions for each OS.


    11. Avoid adding unnecessary platform-specific dependencies
        when an existing cross-platform Python library can perform
        the required task.


    12. Keep user-editable settings outside the main program code.


======================================================================
46. FILE RESPONSIBILITY SUMMARY
======================================================================

    pointer.py
        Cross-platform mouse tracking and WebSocket server.

        Normally:
            DO NOT EDIT.


    pointer.html
        Browser Source visualisation.

        Normally:
            DO NOT EDIT.


    cursor_config.json
        Cursor selection and glow configuration.

        Normally:
            EDIT THIS.


    pointer_config.json
        General pointer behaviour and dimensions.

        Occasionally:
            EDIT THIS.


    start_pointer.py
        OBS automatic startup helper.

        Normally:
            DO NOT EDIT.


    pointers/*.svg
        Cursor artwork.

        Edit or add these when creating new cursor designs.


    README.txt
        Documentation.


======================================================================
47. LIMITATIONS / EXPECTATIONS
======================================================================

OBS Pointer is designed primarily for a standard OBS workflow where
the Browser Source and the OBS canvas use the same configured output
resolution.


The default configuration assumes:

    1920 x 1080


Other output resolutions can be configured through:

    pointer_config.json


The physical computer display can have a different resolution.


For example:

    Computer:
        2560 x 1440

    OBS:
        1920 x 1080


The application automatically scales the coordinates.


The normal operating-system mouse cursor is NOT hidden.


OBS Pointer is an additional visual cursor rendered by OBS.


Therefore, if the underlying desktop is visible in the stream, both
the normal OS cursor and the OBS Pointer may potentially be visible.


For scenes where this is undesirable, simply do not add the OBS
Pointer Browser Source to that scene.


======================================================================
48. EXAMPLE PLAYSTATION 5 STREAM SETUP
======================================================================

A typical PlayStation 5 streaming setup may look like:


    PS5
      |
      v
    HDMI Capture Device
      |
      v
    OBS
      |
      +---- Gameplay
      |
      +---- Camera
      |
      +---- Audio
      |
      +---- OBS Pointer
      |
      v
    YouTube / Twitch / Recording


The computer mouse is connected to the computer running OBS.


The PS5 itself does not provide the computer's mouse cursor.


OBS Pointer reads the computer mouse position and creates a visual
cursor inside the OBS scene.


This allows the streamer to use the mouse as a visual pointing tool
while the viewer sees a custom cursor.


======================================================================
49. EXAMPLE SCENE ORGANISATION
======================================================================

A useful OBS setup might be:


    Scene - PS5 Gameplay

        Gameplay
        Camera
        Game Audio
        Microphone
        OBS Pointer


    Scene - Camera

        Camera
        Microphone


    Scene - Desktop

        Display Capture
        Camera
        Microphone


The OBS Pointer does not need to be included in every scene.


This is particularly important for desktop scenes because the normal
operating-system cursor may already be visible there.


======================================================================
50. PROJECT PHILOSOPHY
======================================================================

OBS Pointer is intentionally designed to remain small and simple.


It does not require:

    - an external server
    - a cloud service
    - a database
    - an online account
    - an authentication system
    - a browser extension
    - a dedicated OBS plugin


The communication happens locally:


    pointer.py
         |
         | localhost WebSocket
         v
    pointer.html


The project is therefore lightweight and portable.


The visual appearance is separated from the mouse-tracking logic.


This makes it possible to create new cursor designs without rewriting
the Python application.


======================================================================
                         END OF README
======================================================================