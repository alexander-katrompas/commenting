# Python Commenting Demonstration

## Description

This repository demonstrates the Python commenting, documentation, naming, and type-hinting standards used in programming courses. The program itself is intentionally small: it defines a `Square` class, provides functions that compare and report on `Square` objects, and uses `main()` to demonstrate the modules.

The primary purpose of the project is not the square calculations. It is to provide a complete example of how Python modules, classes, functions, docstrings, type hints, naming conventions, and comments should be organized.

## Requirements

- Python 3.10 or later
- No external libraries are required

## Run

From the repository root, run:

```bash
python3 main.py
```

No build step is required because Python is interpreted.

## Usage

The program creates `Square` objects, compares their side lengths, and reports which square is larger.

It also displays the `Square` class docstring to demonstrate that Python docstrings are part of the program's runtime metadata and can be accessed through `__doc__`.

Example output includes:

```text
Information about the Square class...

squares are equal
square1 is bigger
square2 is bigger
```

The exact sequence depends on the demonstration values used in `main.py`.

## Project Structure

```text
.
├── main.py
├── functions.py
├── square.py
└── README.md
```

- `main.py` — application driver that demonstrates the project
- `functions.py` — functions that compare and report on `Square` objects
- `square.py` — definition of the `Square` class
- `README.md` — project documentation

## Academic Purpose

This repository demonstrates Python documentation and coding standards while also including several deliberate teaching conventions. Some parts are intentionally more explicit than typical production Python so that students must think about function behavior rather than merely copy a format.

### Module Docstrings

Each Python file begins with a module docstring:

```python
"""
Name: Alexander Katrompas
Assignment: Commenting Demonstration
Purpose: Demonstrates a properly constructed and
         documented module.
"""
```

A module docstring is the normal Python mechanism for documenting a module. Unlike a decorative block of `#` comments, it becomes part of the module's runtime metadata and can be accessed through `__doc__`.

### Function and Method Docstrings

Functions and methods use triple-quoted docstrings placed immediately inside the function definition.

The documentation follows a reStructuredText/Sphinx-style field format:

```python
"""
Describe what the function does.

:param value: meaning of the input
:raises ValueError: condition that causes the exception
:return: meaning of the returned value
:note: additional information
"""
```

The purpose is to document the function's contract: what it receives, what it returns, what can go wrong, and anything unusual a caller should know.

### Required Fields, Including `none`

Course documentation explicitly addresses:

- parameters;
- exceptions;
- return values; and
- notes.

When a category does not apply, it is still written explicitly:

```python
:param: none
:raises: none
:return: None
:note: none
```

Professional Python documentation often omits fields that do not apply. This course intentionally requires them.

The goal is to force the programmer to consider four questions for every function:

- What information enters the function?
- What information leaves the function?
- Can the function raise an exception?
- Is there anything unusual that should be documented?

Writing `none` shows that the category was considered rather than accidentally forgotten.

For Python functions that do not explicitly return a value, the documentation uses:

```text
:return: None
```

because Python actually returns the singleton value `None`.

### Type Hints

Functions and methods use Python type hints:

```python
def compare_squares(sq1: Square, sq2: Square) -> int:
```

and:

```python
def set_length(self, length: float) -> None:
```

Type hints make the expected interface explicit and improve readability, static analysis, editor assistance, and documentation.

Because the type is already expressed in the function signature, the docstring should explain what a value **means** rather than redundantly repeating its type.

For example:

```python
def get_area(self) -> float:
```

is documented with:

```text
:return: the area of the square
```

rather than repeating `float` in the documentation.

### Python Naming Conventions

Python code follows PEP 8 naming conventions.

Functions and methods use `snake_case`:

```python
compare_squares()
report_squares()
get_area()
get_length()
set_length()
```

Constants use uppercase names:

```python
DEFAULT_LENGTH
```

These conventions differ from naming styles that may be used in C++ or generic object-oriented examples. The purpose is to follow the conventions of the language being used rather than impose one naming style across every language.

### Parameter Names Matter in Python

Unlike C++ function declarations, Python does not separate a prototype from its implementation. Parameter names appear directly in the callable function definition:

```python
def set_length(self, length: float) -> None:
```

Those names can also be used by callers as keyword arguments:

```python
square.set_length(length=10)
```

For that reason, Python parameter names are part of the practical interface and should be descriptive.

The implicit instance parameter `self` is not documented as a normal input parameter because callers do not supply it explicitly.

### Public Behavior Versus Implementation Details

Class and function documentation should describe the public behavior of the software rather than simply repeat the source code.

For example, the `Square` class docstring explains what a square represents and how invalid construction values are handled. It does not reproduce a list of every method or narrate the implementation.

The class stores its length in:

```python
self._length
```

A single leading underscore is the normal Python convention indicating that an attribute is non-public and intended for internal use.

This is a convention rather than enforced access control. Python relies heavily on programmer discipline and clear interfaces rather than strict private-member enforcement.

### Comments Should Add Information

Required documentation does not mean that more comments are always better.

Do not leave:

- debug statements;
- commented-out code;
- trivial comments that merely repeat obvious syntax; or
- excessive comments that make the code harder to read.

Additional comments should explain information that is not already clear from the code, such as:

- non-obvious behavior;
- an unusual design choice;
- a necessary assumption; or
- information relevant to grading.

Good comments explain **intent and behavior**, not obvious syntax.

### Documentation and Code Must Agree

Documentation is part of the software and must remain accurate.

If a function's behavior, parameter meaning, exception behavior, or return value changes, its docstring must be updated at the same time.

Type hints, names, comments, and docstrings should all describe the same current program.

## Summary

This project demonstrates several Python engineering habits expected throughout the course:

- use module, class, function, and method docstrings appropriately;
- document parameters, exceptions, return values, and notes explicitly;
- use type hints to make interfaces clearer;
- follow PEP 8 naming conventions;
- use descriptive Python parameter names;
- distinguish public behavior from implementation details;
- use `_name` for non-public attributes by convention;
- write comments that explain meaning rather than obvious syntax; and
- keep documentation accurate and synchronized with the software.

Some documentation requirements are intentionally more explicit than typical production Python. Those differences are instructional scaffolding designed to make students reason deliberately about interfaces, behavior, and software structure.
