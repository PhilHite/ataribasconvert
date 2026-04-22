# ataribasconvert v1.03

A macOS command line tool that converts a plain text Atari BASIC `.txt` file by replacing all `0x0A` (Unix line feed) bytes with `0x9B` (Atari EOL bytes), making the file compatible with Atari BASIC on emulators such as Atari800MacX. The output filename is automatically converted to uppercase. If the source file does not end with a `0x0A` (Unix line feed) byte, one is automatically appended before conversion, ensuring the last line is always processed correctly.

## Usage

```bash
ataribasconvert inputfile.txt outputfile.bas
```

Example:

```bash
ataribasconvert program.txt program.bas
```

The output file will be saved as `PROGRAM.BAS` (uppercase). The tool will report how many bytes were converted and where the output was written.

## Installation

1. Download both `ataribasconvert` and `ataribasconvert.py`.
2. Open Terminal and run:

```bash
chmod +x ataribasconvert
sudo cp ataribasconvert /usr/local/bin/
sudo cp ataribasconvert.py /usr/local/bin/
sudo chmod 644 /usr/local/bin/ataribasconvert.py
```

The tool is now available from anywhere on the command line.

## Loading the converted file in Atari800MacX

Once converted, load the file into Atari800MacX using:

```
ENTER "H1:PROGRAM_ATARI.BAS"
```

The emulator will respond with `READY`. You can then:

- `LIST` - display the program (use **Control+S** to pause scrolling)
- `LIST 100` - list from line 100 onwards
- `LIST 100,200` - list lines 100 through 200
- `RUN` - run the program

> **Note:** Before saving, ensure that under **Settings... > Hard Drives** the **'Hard Drives Read Only'** checkbox is unticked.

- `SAVE "H1:PROGRAM_ATARI.BAS"` - save the program back to disk

## How it works

Atari BASIC uses `0x9B` as its end-of-line character, whereas files created or edited on macOS/Unix use `0x0A` (standard Unix line feed). This tool performs the following steps:

**1. Trailing newline**
If the source `.txt` file does not end with a `0x0A` (Unix line feed) byte, one is automatically appended before conversion. This ensures the last line is always processed correctly regardless of how the file was saved.

**2. EOL conversion**
All `0x0A` bytes are replaced with `0x9B` (Atari EOL) via a binary find-and-replace, making the file readable by Atari BASIC.

**3. Output filename**
The output filename is automatically converted to uppercase (e.g. `program_atari.bas` becomes `PROGRAM_ATARI.BAS`).
