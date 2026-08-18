"""
Name: Alexander Katrompas
Assignment: Commenting Demonstration
Purpose: Demonstrates a properly constructed and
         documented main module.
"""

import functions as fn
from square import Square


def main() -> None:
    """
    Serve as the application driver and demonstrate the
    functions and Square modules.

    :param: none
    :raises: none
    :return: None
    :note: none
    """
    square1 = Square(10)  # Demonstration values; normally avoid literals.
    square2 = Square(5)

    print()
    print("Information about the Square class...")
    print(Square.__doc__)

    fn.report_squares(square1, square2)

    square2.set_length(20)
    fn.report_squares(square1, square2)

    square1.set_length(1)
    square2.set_length(-12)
    fn.report_squares(square1, square2)

    print()


if __name__ == "__main__":
    main()
