# Proper Commenting / Committing / Architecture Example in C/C++

See the general readme in the root of the project for a general description of what is in this sub-project.
This README focuses on proper commenting, committing, and architecture practices in C/C++.

Commenting notes:
- Use `//` for single-line comments.
- Use `/* ... */` for multi-line comments.
- Use Doxygen-style comments (`/** ... */`) for documenting functions, classes, and important structures.
- Keep comments concise and relevant to the code they describe.
- Use inline comments sparingly to explain complex logic.
- Each file has a comment header block at the top of the file.
- Each function and class has a comment block explaining its purpose and usage.
- Each function comment block includes information about parameters and return values.
- param values and return types are always listed.
- Note that if :param, :return, :note, or :except: are not used they are listed but marked as 'na'.
- C/C++ commenting is typically more verbose than, for example, Python, due to the nature of the language.

compilation: `g++ -I ./ *.cpp -o main`

usage: `main`
