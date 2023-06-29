#!/usr/bin/python3

"""Square Task"""


class Square:

    """ Empty """
    def __init__(self, size=0, position=(0, 0)):
        """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Attributes:
        size (int): Size of the Square.
        position (tuple): The position of the square.
    """
        self.size = size
        self.position = position

    def area(self):
        """Exceptions are documented in the same way as classes.

    The area method may be documented in either the class level
    docstring, or as a docstring on the area method itself.

    Attributes:
        self (obj): Area of the Square.
    """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method return The size value
    """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Exceptions are documented in the same way as classes.

    The size method may be documented in either the class level
    docstring, or as a docstring on the size method itself.

    Attributes:
        size (int): Size of the Square.
    """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    @property
    def position(self):
        """Method return The position of the square
    """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Exceptions are documented in the same way as classes.

    The position method may be documented in either the class level
    docstring, or as a docstring on the position method itself.

    Attributes:
        value (int): value of the Position.
    """
        if (isinstance(value, tuple) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(value[0], int) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(value[1], int) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Exceptions are documented in the same way as classes.

    The my_print method may be documented in either the class level
    docstring, or as a docstring on the my_print method itself.

    Attributes:
        self (obj): self object.
    """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
