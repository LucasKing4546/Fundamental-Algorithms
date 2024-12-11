import math
import matplotlib.pyplot as plt

from My_Point import MyPoint

colors = ['blue', 'red', 'green', 'yellow']

class PointRepository:
    def __init__(self):
        '''
        Initializes an empty repository for storing points.
        '''
        self.__points = []

    def add(self, point) -> None:
        '''
        Adds a point to the repository.

        #parameters
        point (MyPoint): The point to add.
        '''
        self.__points.append(point)

    def get_all_points(self) -> list:
        '''
        Gets all points in the repository.

        #return
        list: A list of all points.
        '''
        return self.__points

    def get_point_by_index(self, index) ->  MyPoint:
        '''
        Gets a point by its index in the repository.

        #parameters
        index (int): The index of the point.

        #return
        MyPoint: The point at the specified index.
        '''
        return self.__points[index]

    def get_point_by_color(self, color: str) -> list:
        '''
        Gets all points with a specified color.

        #parameters
        color (str): The color to search for.

        #return
        list: A list of points with the specified color.
        '''
        values = []
        if color in colors:
            for point in self.__points:
                if point.get_color() == color:
                    values.append(point)
        return values

    def get_points_in_square(self, point, length: float) -> list:
        '''
        Gets all points within a square defined by a corner point and a side length.

        #parameters
        point (MyPoint): The bottom-left corner of the square.
        length (int): The side length of the square.

        #return
        list: A list of points within the square.
        '''
        square = []
        for elem in self.__points:
            if point.get_x() <= elem.get_x() <= point.get_x() + length and point.get_y() >= elem.get_y() >= point.get_y() - length:
                square.append(elem)
        return square

    def minimum_distance(self) -> float:
        '''
        Determines the minimum distance between any two points in the repository.

        #return
        float: The minimum distance between two points.
        '''
        minimum = None
        for i in range(len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                point1 = self.__points[i]
                point2 = self.__points[j]
                distance = math.sqrt((point1.get_x() - point2.get_x()) ** 2 + (point1.get_y() - point2.get_y()) ** 2)
                if minimum is None or distance < minimum:
                    minimum = distance
        return minimum

    def update(self, index: int, x: float, y: float, color: str) -> None:
        '''
        Updates the coordinates and color of a point by its index.

        #parameters
        index (int): The index of the point to update.
        x (int): The new x coordinate.
        y (int): The new y coordinate.
        color (str): The new color.
        '''

        self.__points[index].set_x(x)
        self.__points[index].set_y(y)
        self.__points[index].set_color(color)

    def delete(self, index: int) -> None:
        '''
        Deletes a point by its index.

        #parameters
        index (int): The index of the point to delete.
        '''
        if 0<=index<=self.__points.__len__():
            self.__points.pop(index)

    def delete_square(self, point, length: float) -> None:
        '''
        Deletes all points within a square defined by a corner point and a side length.

        #parameters
        point (MyPoint): The bottom-left corner of the square.
        length (int): The side length of the square.
        '''
        for elem in self.__points[:]:
            if point.get_x() <= elem.get_x() <= point.get_x() + length and point.get_y() >= elem.get_y() >= point.get_y() - length:
                self.__points.remove(elem)

    def show_points(self):
        '''
        Displays all points using matplotlib.
        '''
        for point in self.__points:
            plt.scatter(point.get_x(), point.get_y(), c=point.get_color())
        plt.show()

    def get_number_of_points_by_color(self, color : str) -> int:
        '''
        Gets the number of points that have a specified color.

        #parameters
        color (str): The color to count points for.

        #return
        int: The number of points with the specified color.
        '''
        return sum(1 for point in self.__points if point.get_color() == color)


    def shift_all_points_on_y_axis(self) -> None:
        '''
        Shifts all points in the repository by a specified value along the y-axis.

        #parameters
        shift_value (float): The amount to shift the y-coordinate of each point.
        '''
        for point in self.__points:
            point.set_x(0)


    def delete_points_within_distance(self, x : float, y : float, distance) -> None:
        '''
        Deletes all points that are within a specified distance from a given point.

        #parameters
        x (float): The x-coordinate of the reference point.
        y (float): The y-coordinate of the reference point.
        distance (float): The maximum distance from the reference point within which points should be deleted.
        '''
        self.__points = [
            point for point in self.__points
            if math.sqrt((point.get_x() - x) ** 2 + (point.get_y() - y) ** 2) >= distance
        ]
        #print([str(point) for point in self.__points])
