# pyScriptStats
A simple Python script that counts the number of total lines, blank lines, lines containing just comments, and lines containing actual code in a given Python script. Accepts command line arguments, takes a filename and can take flags for printing version information or a help screen. Blindly assumes whatever you give it is a valid Python script. If you give it anything else, the results will be meaningless. Furthermore, it doesn't account for the possibility of compound statements.

Created and tested using Python 3.13.5, on Debian 13. It should work the same on Windows or any other OS for that matter.
