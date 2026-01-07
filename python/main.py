# ###########################################
# Name: Alexander Katrompas
# Assignment: Commenting Demonstration
# Purpose: A demonstration of a properly
#          constructed and commented main.py
# ###########################################

import functions as fn
from square import Square

def main():
    """
    This function is the application driver. It uses
    and tests the functions.py and Square.py modules.

    @param na : na

    @return na

    @exception na : na

    @note na
    """

    square1 = Square(10) # normally, DO NOT use literals
    square2 = Square(5)  # these are used only for demonstation
    
    print()
    print("Information about the Square class...")
    print(square1.__doc__)
    
    fn.reportSquares(square1, square2)

    square2.setLength(20)
    fn.reportSquares(square1, square2)
    
    square1.setLength(1)
    square2.setLength(-12)
    fn.reportSquares(square1, square2)
    
    fn.reportSquares(square1, 3)

    print()

main()

