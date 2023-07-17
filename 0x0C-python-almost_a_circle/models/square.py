#!/usr/bin/python3

"""models/Square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Width."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Width."""
        return self.__size

    @size.setter
    def size(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Width."""
        if args:
            attribute_names = ['id', 'size', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def __str__(self) -> str:
        """Width."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
