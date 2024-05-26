# Proper Commenting Examples

In this repository, you will find two complete commenting examples. One in Python within the python/ folder, one in C/C++ in the c++/ folder. The logic and functionality for each example is the same, only the language and commenting syntax is different. Both examples include main, stand-alone functions, and a stand-alone class. Another README explaining each set of code and commenting is included with each example.

Note that this example also demonstrates proper modularity. In particular:

1. main() stands alone. Never place other functions, classes, or other code in main.
2. Classes stand alone. One class, one file (Python). One class two, files (c++), a cpp and a header.
3. Functions are contained within a single file (in this case), and functions should always be grouped into related functions per file.
4. Each module (main, class, functions) stands alone, and contains what it needs, and only what it needs, to stand alone and be portable.
5. Header files (C++) conform strictly to the separation of interface (no code logic) and implementation (code).

