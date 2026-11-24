#!/usr/bin/env python3
"""Copy the bundled entry.png to the output directory.

The entry image is drawn once and shipped in this repository; the program
only copies it, so both runs write the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SRC, dest)
    with open(SRC, "rb") as f:
        source_bytes = f.read()
    with open(dest, "rb") as f:
        written_bytes = f.read()
    if written_bytes != source_bytes:
        raise SystemExit("entry.png copy mismatch: output differs from source")


if __name__ == "__main__":
    main()
