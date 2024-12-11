colors = ['blue', 'red', 'green', 'yellow']

class MyPoint:
    def __init__(self, coord_x:int|float, coord_y:int|float, color):
        '''
        Initializes a point with x and y coordinates and a color.

        #parameters
        coord_x (int): The x coordinate.
        coord_y (int): The y coordinate.
        color (str): The color of the point.
        '''
        if not isinstance(coord_x, (int,float)) or not isinstance(coord_y, (int,float)) or color not in colors:
            raise ValueError("The coordinates or the color are incorrect!")
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color


    def get_x(self) -> int|float:
        return self.__coord_x

    def get_y(self) -> int|float:
        return self.__coord_y

    def get_color(self) -> str:
        return self.__color

    def set_x(self, value: int|float) -> None:
        if not isinstance(value, (int,float)):
            raise ValueError("The value is incorrect!")
        self.__coord_x = value

    def set_y(self, value: int|float) -> None:
        if not isinstance(value, (int,float)):
            raise ValueError("The value is incorrect!")
        self.__coord_y = value


    def set_color(self, value: str):
        if value not in colors:
            raise ValueError("The value is incorrect!")
        self.__color = value

    def __str__(self):
        '''
        Returns a string representation of the point.

        #return
        str: A string describing the point's coordinates and color.
        '''
        return f"Point ({self.__coord_x}, {self.__coord_y}) of color {self.__color}"

    def __eq__(self, other: 'MyPoint') -> bool:
        '''
        Returns true if the two points are equal.

        #param
        MyPoint: other
        :return: True if the points are equal, False otherwise.
        '''
        if self.__coord_x == other.get_x() and self.__coord_y == other.get_y():
            return True
        return False
