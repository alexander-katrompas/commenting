"""
Name: Alexander Katrompas
Assignment: Commenting Demonstration
Purpose: Demonstrates a properly constructed and
         documented class module.
"""

DEFAULT_LENGTH = 1.0


class Square:
    """
    Represent a square with a configurable side length.

    The area is calculated on demand rather than stored.
    A non-positive construction value leaves the square
    at the default side length.

    :note: none
    """

    def __init__(self, length: float) -> None:
        """
        Initialize a square with the specified side length.

        :param length: the initial side length of the square
        :raises: none
        :return: None
        :note: a non-positive value leaves the length set to
               DEFAULT_LENGTH
        """
        self._length: float = DEFAULT_LENGTH
        self.set_length(length)

    def get_area(self) -> float:
        """
        Return the area of the square.

        :param: none
        :raises: none
        :return: the area of the square
        :note: the area is calculated on demand
        """
        return self._length * self._length

    def get_length(self) -> float:
        """
        Return the side length of the square.

        :param: none
        :raises: none
        :return: the side length of the square
        :note: none
        """
        return self._length

    def set_length(self, length: float) -> None:
        """
        Set the side length of the square.

        :param length: the new side length of the square
        :raises: none
        :return: None
        :note: a non-positive value leaves the current length
               unchanged
        """
        if length > 0:
            self._length = length
