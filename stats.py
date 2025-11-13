# Calculate some statistics about a Python script.
# Made by rainier39 (https://github.com/rainier39)

import sys
import os

# Constants.
VERSION = 1.0
HELPSCREEN = """Usage: python3 stats.py file [OPTIONS]...
Calculate some statistics about a Python script.
Disclaimer: not guarenteed to be accurate.

Arguments:
  -h, --help | Display this screen.
  -v, --version | Display the version.
  """

filename = None

# Handle command line flags.
for i in range(1, len(sys.argv)):
  if ((sys.argv[i] == "--help") or (sys.argv[i] == "-h")):
    print(HELPSCREEN)
    exit(0)
  elif ((sys.argv[i] == "--version") or (sys.argv[i] == "-v")):
    print(f"pyScriptStats version {VERSION}")
    exit(0)
  # Anything other than a recognized flag will be assumed to be the Python script.
  else:
    filename = sys.argv[i]

if (filename == None):
  filename = input("Please enter the filename of a Python script: ")

# Prompt the user until a valid file is given.
while not os.path.isfile(filename):
  filename = input("Specified file not found. Please try again: ")

lines = 0
commentlines = 0
blanklines = 0
codelines = 0

# Calculate the statistics via reading each line from the file.
with open(filename, "rt") as f:
  for line in f:
    lines += 1
    if line.strip().startswith("#"):
      commentlines += 1
    elif (line.strip() == ""):
      blanklines += 1
    else:
      codelines += 1

# Print the results.
print(f"""Total Lines: {lines}
Comment Lines: {commentlines}
Blank Lines: {blanklines}
Code Lines: {codelines}""")
