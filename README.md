# Commenting Demonstration

## Description

This repository demonstrates the commenting, documentation, interface, and implementation standards used in programming courses. The program itself is intentionally small: it defines a `Square` class, provides functions that compare and report on `Square` objects, and uses `main()` to exercise those modules.

The primary purpose of the project is not the square calculations. It is to provide a complete example of how source files, header files, function documentation, class structure, and comments should be organized.

## Requirements

- C++ compiler with C++17 support or later
- `g++` or another standards-compliant C++ compiler
- A command-line environment capable of building and running a C++ program
- No external libraries are required

## Build and Run

From the repository root, compile the project with:

```bash
g++ -std=c++17 *.cpp -o square_demo
```

Run the program with:

```bash
./square_demo
```

## Usage

The program creates several `Square` objects, compares their side lengths, and reports which square is larger.

Expected output:

```text
square1 is bigger
square2 is bigger
squares are equal
```

The final comparison demonstrates the `Square` class's handling of a non-positive side length. A non-positive value is replaced with the default value defined by `DLENGTH`.

## Project Structure

```text
.
├── main.cpp
├── main.h
├── functions.cpp
├── functions.h
├── square.cpp
├── square.h
└── README.md
```

- `main.cpp` — application driver used to demonstrate the modules
- `main.h` — interface dependencies required by `main.cpp`
- `functions.cpp` — implementation of functions that operate on `Square` objects
- `functions.h` — public declarations for the functions module
- `square.cpp` — implementation of the `Square` class
- `square.h` — public class declaration for `Square`
- `README.md` — project documentation

## Academic Purpose

This repository demonstrates a commenting standard designed to develop professional documentation habits while also serving specific instructional goals. Some parts of the standard intentionally require more explicit documentation than would normally appear in professional production code.

### Doxygen-Style Documentation Blocks

File, class, and function documentation use the familiar Doxygen-style form:

```cpp
/**
 * Description
 *
 * @param ...
 * @exception ...
 * @return ...
 * @note ...
 */
```

The leading `*` characters are not required by C++ syntax, but they make multiline documentation blocks visually consistent and recognizable. Placing a documentation block immediately before the declaration or definition it describes also makes the relationship between the documentation and the code clear.

This style is compatible with documentation-generation tools such as Doxygen, but the primary goal in these courses is disciplined, readable source documentation.

### Required Fields, Including `none`

Function documentation explicitly includes:

- `@param`
- `@exception`
- `@return`
- `@note`

These fields remain present even when a category does not apply. In that case, the value is written as `none`.

For example:

```cpp
/**
 * Returns the side length of the square.
 *
 * @param none
 * @exception none
 * @return the side length of the square
 * @note none
 */
```

Professional documentation often omits fields that do not apply. This course intentionally does not. Requiring the field forces the programmer to consider each part of the function's behavior rather than leaving it unclear whether a category was considered or simply forgotten.

The purpose is analytical discipline:

- What information enters the function?
- What information leaves the function?
- Can the function raise an exception?
- Is there anything unusual that another programmer should know?

Writing `none` is therefore not filler. It records that the question was considered and that the answer is none.

### Interface Versus Implementation

A central engineering principle demonstrated in this repository is the separation of **interface** from **implementation**.

Header files describe the interface: what exists, what can be called, what goes in, and what comes out.

Source files contain the implementation: how the behavior is actually produced.

For that reason, function declarations in header files intentionally omit parameter names:

```cpp
void setLength(float);
int compareSquares(Square, Square);
```

rather than:

```cpp
void setLength(float length);
int compareSquares(Square sq1, Square sq2);
```

Parameter names are not part of a C++ function signature and are not compiler-enforced to remain consistent between a declaration and its definition. Repeating them in both places creates a second, independent description that can drift out of sync.

The parameter's meaning belongs in the function documentation. The implementation parameter name belongs in the function definition.

For example, the interface may contain:

```cpp
void setLength(float);
```

while the implementation contains:

```cpp
void Square::setLength(float length) {
    ...
}
```

This keeps the header focused on the callable interface and the source file focused on implementation.

### Explicit Class Sections

The class declaration also keeps structural sections visible even when a section is empty:

```cpp
// Printing Methods
// none
```

and:

```cpp
// Methods
// none
```

A professional codebase might normally omit an empty category. In this course, the empty section is deliberate. It requires the student to consider the complete structure of the class and decide whether that category is needed.

The goal is to make class design explicit rather than accidental.

### Comments Should Add Information

Required documentation does not mean that more comments are always better.

Do not leave:

- debug statements;
- commented-out code;
- trivial comments that merely repeat the code; or
- excessive comments that make the program harder to read.

Additional comments should be used only when they add information, such as explaining:

- non-obvious behavior;
- a non-standard solution or design choice; or
- information relevant to grading.

Good commenting explains intent, behavior, assumptions, and design decisions. It should not narrate obvious syntax.

### Consistency Is Part of the Standard

The required documentation format is intentionally standardized. Spacing, field order, and the overall structure of required comment blocks should remain consistent.

The purpose is not decorative uniformity. Consistency makes documentation easier to scan, easier to evaluate, and easier for another programmer to understand quickly.

## Summary

This project demonstrates more than C++ syntax. It models several engineering habits expected throughout the course:

- separate interface from implementation;
- document files, classes, and functions consistently;
- explicitly analyze inputs, outputs, exceptions, and special conditions;
- keep class structure deliberate and visible;
- avoid redundant or misleading interface information;
- use comments to explain meaning rather than obvious syntax; and
- keep documentation accurate, concise, and synchronized with the software.

The commenting standard is intentionally more explicit than typical production documentation in a few places. Those differences are teaching tools designed to make the reasoning behind software structure and interfaces visible.