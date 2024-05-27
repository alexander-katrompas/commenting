# Proper Commenting / Committing / Architecture Examples

In this repository, you will find two complete code examples. One in Python within the python/ folder, one in C/C++ in the c++/ folder. The logic and functionality for each example is the same, only the language and syntax is different. Both examples include main, a stand-alone functions module, and a stand-alone class. Another README explaining each set of code and is included with each example.

The purpose of this repo is to demonstrate proper...

## Use of .gitignore and README.md Files

 - the .gitignore is in the root of the project and applies to the entire project.
 - The global README (this file) applies to the project as a whole. Local README are in each sub-folder explaining each subproject

## Commenting

 - All files have a proper file comment header.
 - Functions are commented properly.
 - Classes are commented properly.
 - Header files (C++) are commented properly.
 - [commenting](https://katrompas.accprofessors.com/commenting)

## Committing

 - Commits are made small, smart, and often.
 - Read the commits to get an idea of how proper committing is done.
 - [committing](https://katrompas.accprofessors.com/committing)


## Modularity
This example code also demonstrates proper modularity. In particular:

 - main() stands alone. Never place other functions, classes, or other code in main.
 - Classes stand alone. One class, one file (Python). One class two, files (c++), a cpp and a header.
 - Functions are contained within a single file (in this case), and functions should always be grouped into related functions per file.
 - Each module (main, class, functions) stands alone, and contains what it needs, and only what it needs, to stand alone and be portable.
 - Header files (C++) conform strictly to the separation of interface (no code logic) and implementation (code).
 - Do not repeat yourself.
- [best practices in procedural code](https://katrompas.accprofessors.com/best-practice-procedural-programming)
- [best practices in OOP code](https://katrompas.accprofessors.com/best-practice-oop-programming)

## Exception Handling

 - If something can throw / raise and an exception, it must be handled by the caller within a try/catch (C++) or try/except block (Python).
 - Never throw and catch your own exception in the same block of code.
 - Never do more than one thing within a try/catch (C++) or try/except block (Python).
 - [exception handling](https://github.com/alexander-katrompas/exception-handling-cplusplus)


