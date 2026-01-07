# ###################################################
# Name: Alexander Katrompas
# Assignment: Commenting Demonstration
# Purpose: A demonstration of a properly
#           constructed and commented functions file
# ###################################################

from square import Square

def compareSquares(sq1, sq2):
    """
    Compare two Square objects by side length.

    :param sq1: the first square to compare
    :param sq2: the second square to compare
    :return: (int)
        0 if both squares are equal in size,
        1 if the first square is larger,
        2 if the second square is larger.
    :raises TypeError: If either argument is not a Square instance.
    :note: This function strictly compares Square objects
    """

    if not isinstance(sq1, Square) or not isinstance(sq2, Square):
        raise TypeError("must be Square type")
    
    len1 = sq1.getLength()
    len2 = sq2.getLength()

    result = 0    
    if len1 > len2:
        result = 1
    elif len1 < len2:
        result = 2
    
    return result
    
def reportSquares(sq1, sq2):
    """
    Accepts two square objects, compares them
    and prints the answer.

    :param sq1: the first square to compare
    :param sq2: the second square to compare
    :return: na
    :raises: na.
    :note: function handles TypeErrors from compareSquares.
    """

    try:
        compare = compareSquares(sq1, sq2)
    except TypeError:
        compare = -1

    if compare == 0:
        print("squares are equal")
    elif compare == 1:
        print("square1 is bigger")
    elif compare == 2:
        print("square2 is bigger")        
    else:
        print("Type Error: compareSquares must be passed two Squares.")

