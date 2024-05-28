# ###################################################
# Name: Alexander Katrompas
# Assignment: Commenting Demonstration
# Purpose: A demonstration of a properly
#           constructed and commented functions file
# ###################################################

from Square import Square

def compareSquares(sq1, sq2):
    """
    This function accepts two square objects,
    compares there area and will return 0, 1 ,2.
    0: they are equal
    1: the first square is bigger
    2: the second sqaure is bigger

    @param sq1 : a square object
    @param sq2 : a square object

    @return 0,1,2 : which square is bigger

    @exception (string) : one parameter or the other is not a square

    @note na
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
    This function accepts what are presumably two
    square objects, compares them by calling
    compareSquares() and prints the answer.
    Since is it a printing function, that is its
    only job.

    @param sq1 : a square object
    @param sq2 : a square object

    @return na : na

    @exception na : na

    @note na
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

