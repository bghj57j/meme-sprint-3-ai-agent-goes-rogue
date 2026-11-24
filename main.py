# Copies the meme image to /output/entry.png, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
shutil.copyfile(SRC, os.path.join(out, "entry.png"))  # byte-identical copy
