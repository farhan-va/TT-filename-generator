# TT Filename Generator

This is a small desktop utility (Tkinter GUI) that helps generate standardized "TT" file names for transactions and copy them to the clipboard.

## What the program does

- Presents a GUI where you can enter transaction details (Company, TT code, Division (for SQCC), Bank, Currency, Amount, Vendor/Customer, Bank reference, Transaction number, Details and Date).
- Validates and normalises the input (amount formatting, date formats DD-MM-YYYY or DD/MM/YYYY are accepted and converted).
- Builds a composed filename string using the entered fields (prefix `TT`, company + code, bank, currency, formatted amount, direction (to / Incoming from), transactee, bank reference, transaction number, details and date).
- Copies the generated filename to the system clipboard and shows it in the GUI.
- Persists a JSON record of the latest values under the key `Company+TTcode` in `TT records.json` inside the user's Documents folder (e.g. `%USERPROFILE%\Documents\TT records.json`).
- Lets you search/load previously saved records by Company+TT code and reset the input fields.

The main program file is `main.py` (Tkinter-based) in this same directory.

### Requirements

- Windows
- Python 3.7+ (a Python installation with tkinter/tcltk support)
- Optional: PyInstaller (to compile to a single .exe)

### Run from source (development)

1. Open PowerShell and (optionally) create/activate a virtual environment from the `src` folder:

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

2. Run the program:

    ```powershell
    python main.py
    ```

The GUI should open. Fill the fields and click "Generate and copy to clipboard".

### Build a single-file Windows .exe with a custom icon (PyInstaller)

These instructions create a single executable and embed the icon located at `icons/ico.ico`.

1. From the `src` folder (where `main.py` and the `icons/` folder live) install PyInstaller in your environment if needed:

   ```powershell
   pip install pyinstaller
   ```

2. Build the executable (PowerShell example):

   ```powershell
   # Create a one-file, windowed (no console) executable and embed the .ico file
   pyinstaller --onefile --windowed --icon=icons\ico.ico --name "TT Filename Generator" main.py
   ```

Notes:

- Use the relative path `icons\ico.ico` when running from the `src` folder. If you run PyInstaller from the repository root, point to `src\icons\ico.ico` instead.
- The `--windowed` flag prevents a console window from appearing. Remove it if you want a console for debugging.
- After a successful build the executable will be in `dist\` (for example `dist\TT Filename Generator.exe`).

1. Test the produced exe by running the file from `dist`.

### Troubleshooting and tips

- If the app fails to start after building, run it from a console (without `--windowed`) to see errors.
- Ensure your Python installation includes tkinter (on Windows the official installer usually includes it). If tkinter import fails, reinstall Python with Tcl/Tk support or use the official Windows installer.
- If the icon doesn't appear on the compiled exe, confirm the `.ico` file is a valid Windows icon and that the `--icon` path is correct when invoking PyInstaller.
- If your antivirus flags the single-file exe, add an exception for the built executable or distribute the `dist` folder contents.

### Files of interest

- `main.py` — main application source (this file)
- `icons/ico.ico` — recommended icon to use when building the exe
- `old/` — older versions of the script (kept for reference)
