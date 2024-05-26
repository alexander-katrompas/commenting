# ##############################################
# Name: Alexander Katrompas
# Assignment: Commenting Demonstration
# Purpose: A demonstration of a properly
#          constructed and commented class file
# ##############################################

class Square:
    """
    This class defines a Square. It must be passed
    a side length parameter which defaults to __MINL
    if an invalid a length is passed (i.e. <=0)

    @attrib (float) __length : the length of a side
    """

    def __init__(self, length):
        """
        Constructor. Pass in a posive (>0)
        float value to set the length.

        @param (float) length : the length of the sides
        @return na : na
        @exception na : na
        """
        self.__length = length

