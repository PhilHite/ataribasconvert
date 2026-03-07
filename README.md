# ataribasconvert

A command line tool that converts a plain text Atari BASIC `.BAS` file by replacing all `0x0A` (Unix line feed) bytes with `0x9B` (Atari EOL bytes), making the file compatible with Atari BASIC on emulators such as Atari800MacX.

## Usage

```bash
ataribasconvert INPUTFILE.BAS OUTPUTFILE.BAS
```

Example:

```bash
ataribasconvert PROGRAM.BAS PROGRAMA.BAS
```

The tool will report how many bytes were converted and where the output was written.

## Installation
macOS & Linux
1. Download the `ataribasconvert` file.
2. Open Terminal and run:

```bash
chmod +x ataribasconvert
sudo mv ataribasconvert /usr/local/bin/
```
Windows
1. Download both `ataribasconvert.bat` and `ataribasconvert.py`.
2. Place both files in the same folder. For system-wide access from any directory, copy both files to a folder that is on your system PATH, for example `C:\Windows\System32`.

The tool is now available from anywhere on the command line.

## Loading the converted file in Atari800MacX

Once converted, load the file into Atari800MacX using:

```
ENTER "H1:PROGRAMA.BAS"
```

The emulator will respond with `READY`. You can then:

- `LIST` — display the program (use **Control+S** to pause scrolling)
- `LIST 100` — list from line 100 onwards
- `LIST 100,200` — list lines 100 through 200
- `RUN` — run the program

> **Note:** Before saving, ensure that under **Settings... > Hard Drives** the **'Hard Drives Read Only'** checkbox is unticked.

- `SAVE "H1:PROGRAMA.BAS"` — save the program back to disk

## How it works

Atari BASIC uses `0x9B` as its end-of-line character, whereas files created or edited on macOS/Unix use `0x0A` (standard Unix line feed). This tool performs a binary find-and-replace to make the file readable by Atari BASIC.

