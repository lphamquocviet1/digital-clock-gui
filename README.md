# MOMENT — Digital Clock

A desktop clock built with Python and PyQt6. The GUI uses a dark gradient card,
large time display, and warm accent colors.

## Features

- Shows your computer's local time, including seconds.
- Displays the current weekday and date.
- Starts in 24-hour format; use **Switch to 12-hour** to show AM/PM, then
  **Switch to 24-hour** to switch back.
- Refreshes automatically every 200 milliseconds.

## Setup and run

Install Python 3, then run these commands from the project directory.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install "PyQt6>=6.7,<7"
python3 main.py
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "PyQt6>=6.7,<7"
python main.py
```

PyQt6 is the only third-party dependency. The clock follows your computer's
date, time, and time zone settings.
>>>>>>> 60b0bc7 (Create the gui digital clock)
