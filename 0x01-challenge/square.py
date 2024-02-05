#!/usr/bin/python3
""" Module Square class """


class Square():
    """ Square class """

    def __init__(self, *args, **kwargs):
        """ Constructor of the class """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Test cases """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
