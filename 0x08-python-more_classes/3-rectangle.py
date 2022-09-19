class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize """
        self.width = width
        self.height = height

    def __str__(self):
        """ returns set of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]
