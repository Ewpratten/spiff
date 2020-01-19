import argparse
import re

from .parse.FNR_Defs import fnr

# Parse program args
ap = argparse.ArgumentParser()
ap.add_argument("src", help="Source file")
ap.add_argument("dst", help="Dest file")
args = ap.parse_args()

print(f"Compiling {args.src} -> {args.dst}")

# Load the input file
file = open(args.src, "r").read()

# Create an output file buffer
out_buf = file

# Pass file through parse chain
for parser in fnr:
    out_buf = parser[1](re.findall(parser[0], out_buf, re.M))
    
print(out_buf)