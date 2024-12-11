import numpy as np
colors = ["r", "b", "y", "m", "g"]

class MyVector:
    def __init__(self, name_id: int|str, colour: str, type: int, values: list):
        if not isinstance(values, list) and colour in colors and isinstance(type, int) and isinstance(name_id, int|str):
            raise ValueError("The introduced vector is not valid!")
        self.__name_id = name_id
        self.__colour = colour
        self.__type = type
        self.__values = np.array(values)

    def get_name_id(self) -> int|str:
        return self.__name_id

    def get_colour(self):
         return self.__colour

    def get_type(self):
         return self.__type

    def get_values(self):
         return self.__values

    def set_name_id(self, name_id: int|str):
        if isinstance(name_id, str) or isinstance(name_id, int):
            self.__name_id = name_id
        else:
            raise ValueError('Name id must be of type int or str')

    def set_colour(self, colour: str):
        if isinstance(colour, str) and colour in colors:
            self.__colour = colour
        else:
            raise ValueError("Colour must be of type str")

    def set_type(self, type: int):
        if isinstance(type, int):
            self.__type = type
        else:
            raise ValueError("Type must be an integer")

    def set_values(self, values: list):
        if len([v for v in values if isinstance(v, int)]) == len(values):
            self.__values = np.array(values)
        else:
            raise ValueError('Values must be of type int')

    def __eq__(self, other):
        if isinstance(other, MyVector):
            if not self.__name_id == other.get_name_id():
                return False
            if not self.__colour == other.get_colour():
                return False
            if not self.__type == other.get_type():
                return False
            if not self.__values == other.get_values():
                return False
            return True

    def __str__(self):
        return str(self.__values)

    def add_scalar(self, value: int):
        """
        Adds a scalar value to each element in the vector.

        Parameters:
            value (int): The scalar value to be added to each element.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise ValueError("Value must be of type int")
        self.__values += value

    def add_vectors(self, other: 'MyVector'):
        """
        Adds the elements of another vector to this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be added.

        Returns:
            None
        """
        if len(self.__values) != len(other.get_values()):
            raise ValueError("Values must have same length")
        self.__values += other.get_values()

    def substract_vector(self, other: 'MyVector'):
        """
        Subtracts the elements of another vector from this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be subtracted.

        Returns:
            None
        """
        if len(self.__values) != len(other.get_values()):
            raise ValueError("Values must have same length")
        self.__values -= other.get_values()

    def multiply_vector(self, other: 'MyVector'):
        """
        Multiplies the elements of another vector with this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be multiplied.

        Returns:
            None
        """
        self.__values = np.dot(self.get_values(), other.get_values())


    def sum_elements(self) -> int:
        """
        Calculates the sum of all elements in the vector.

        Parameters:
            s (int): The sum of all elements in the vector.
        Returns:
            int: The sum of all elements in the vector.
        """
        return np.sum(self.__values)

    def multiply_elements(self):
        """
        Calculates the product of all elements in the vector.

        Parameters:
            s (int): The product of all elements in the vector.

        Returns:
            int: The product of all elements in the vector.
        """
        return np.prod(self.__values)

    def avg_elements(self):
        """
        Calculates the average of all elements in the vector.

        Parameters:

        Returns:
            float: The average of all elements in the vector.
        """
        return np.mean(self.__values)

    def min_elements(self) -> int:
        """
        Finds the minimum element in the vector.

        Parameters:
            None

        Returns:
            int: The smallest element in the vector.
        """
        return np.min(self.__values)

    def max_elements(self) -> int:
        """
        Finds the maximum element in the vector.

        Parameters:
            None

        Returns:
            int: The largest element in the vector.
        """
        return np.max(self.__values)












