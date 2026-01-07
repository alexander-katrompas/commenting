# ##############################################
# Name: Alexander Katrompas
# Assignment: Commenting Demonstration
# Purpose: A demonstration of a properly
#          constructed and commented class file
# ##############################################

DLENGTH = 1

class Square:
    """
    This class defines a Square. It must be passed
    a side length parameter which defaults to __DLENGTH
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
        self.setLength(length)
   
    def getArea(self):
        """
        Returns the area of the square. The area is
        not stored as an attribute, and is calculated
        on demand through this method.

        @param na : the length of the sides
        
        @return (float) __length*2 : the area of the square
        
        @exception na : na
        """
        return __length*2

    def getLength(self):
        """
        returns the attribute self.__length

        @param na : na
        
        @return (float) self.__length  : the length of 1 side
        
        @exception na : na
        """
        return self.__length

    def setLength(self, l):
        """
        sets the length of a side of the square
        including error checking that the length
        is positive, or is set to default value DELNGTH        
        
        @param (float) l : the proposed length of 1 side

        @return na : na

        @exception na : na
        """
        if l > 0:
            self.__length = l
        else:
            self.__length = DLENGTH

