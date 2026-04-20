#!/usr/bin/env python3
# ataribasconvert v1.02
# Converts a plain text Atari BASIC .txt file by:
#   1. Appending a 0x0A (Unix line feed) byte if the file doesn't end with one
#   2. Replacing all 0x0A (Unix line feed) bytes with 0x9B (Atari EOL bytes)

import sys
import os

def convert(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = bytearray(f.read())

    # Ensure file ends with 0x0A before conversion
    if not data or data[-1] != 0x0A:
        data.append(0x0A)
        print("Note: Appended missing trailing newline (0x0A) to source data.")

    # Replace all 0x0A with 0x9B
    count = data.count(0x0A)
    data = data.replace(b'\x0A', b'\x9B')

    with open(output_path, 'wb') as f:
        f.write(data)

    print(f"Converted {count} byte(s) from 0x0A to 0x9B.")
    print(f"Output written to: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ataribasconvert INPUTFILE.txt OUTPUTFILE.BAS")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    convert(input_path, output_path)
