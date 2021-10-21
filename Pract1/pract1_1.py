class Rectangle():

    def __init__(self, lenth=1, width=1):
        if isinstance(lenth, (int, float)) and isinstance(width, (int, float)):
            if not(lenth > 0 and width > 0):
                raise ValueError("should be > 0")
            self.__length = lenth
            self.__width = width    
        else:
            raise TypeError("should be integer or float")

    def __str__(self):
        return f"Rectangle({self.__length}, {self.__width})"

    @property
    def lenght(self):
        return self.__length

    @staticmethod
    def check_if_valid(value):
        if not (isinstance(value, float)):
            raise TypeError("Wrong type of value, must be float")
        if not (value > 0.0 and value < 20.0):
            raise ValueError("Wrong value, should be >0.0 and <20.0")
        return True

    @lenght.setter
    def lenght(self, value):
        if Rectangle.check_if_valid(value):
            self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if Rectangle.check_if_valid(value):
            self.__width = value

    def get_area(self):
        return self.__width * self.__length

    def get_perimetr(self):
        return 2 * (self.__width + self.__length)


a = Rectangle(12, 12)
print(a.lenght)
a.lenght = 1.2
print(a.lenght)
# print(a)

# c = Rectangle("dsadas",12)
# print(c)
