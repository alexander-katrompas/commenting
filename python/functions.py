"""
Name: Alexander Katrompas
Assignment: Commenting Demonstration
Purpose: Demonstrates a properly constructed and
         documented functions module.
"""

from square import Square


def compare_squares(sq1: Square, sq2: Square) -> int:
    """
    Compare two Square objects by side length.

    :param sq1: the first square to compare
    :param sq2: the second square to compare
    :raises TypeError: if either argument is not a Square
    :return: 0 if the squares are equal, 1 if the first
             square is larger, or 2 if the second square
             is larger
    :note: none
    """
    if not isinstance(sq1, Square) or not isinstance(sq2, Square):
        raise TypeError("both arguments must be Square objects")

    len1 = sq1.get_length()
    len2 = sq2.get_length()
    result = 0

    if len1 > len2:
        result = 1
    elif len1 < len2:
        result = 2

    return result


def report_squares(sq1: Square, sq2: Square) -> None:
    """
    Compare two Square objects and report which is larger.

    :param sq1: the first square to compare
    :param sq2: the second square to compare
    :raises: none
    :return: None
    :note: handles TypeError raised by compare_squares()
    """
    try:
        compare = compare_squares(sq1, sq2)
    except TypeError:
        compare = -1

    if compare == 0:
        print("squares are equal")
    elif compare == 1:
        print("square1 is bigger")
    elif compare == 2:
        print("square2 is bigger")
    else:
        print("Type Error: compare_squares() must be passed two Square objects.")
