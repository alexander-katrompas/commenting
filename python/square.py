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

    :attributes:
        __length (float) : the length of a side of the square
    """

    def __init__(self, length):
        """
        Pass in a positive (>0) float value to set the length.

        :param length: the length of a side of the square
        :return: na
        :raises: na
        :note: if length is invalid (<=0) it is set to default value DLENGTH
        """
        self.__length = DLENGTH # default value
        self.setLength(length)
   
    def getArea(self):
        """
        Area is not stored as an attribute. It is calculated
        on demand through this method.

        :param: na
        :return: (float) the area of the square
        :raises: na
        :note: area = length * length
        """
        return __length*2

    def getLength(self):
        """
        returns the attribute self.__length

        :param: na
        :return: (float) the length of a side of the square
        :raises: na
        :note: na
        """
        return self.__length

    def setLength(self, l):
        """
        sets the length of a side of the square
        including error checking that the length
        is positive, or is set to default value DELNGTH        

        :param l: the length of a side of the square
        :return: na
        :raises: na
        :note: if length is invalid (<=0) it is not changed
        """
        if l > 0:
            self.__length = l
