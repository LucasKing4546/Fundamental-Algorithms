colors = ["r", "b", "y", "m", "g"]

class MyVector:
    def __init__(self, name_id: int|str, colour: str, type: int, values: list):
        if not isinstance(values, list) and colour in colors and isinstance(type, int) and isinstance(name_id, int|str):
            raise ValueError("The introduced vector is not valid!")
        self.__name_id = name_id
        self.__colour = colour
        self.__type = type
        self.__values = values

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
            self.__values = values
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

    def __repr__(self):
        return str(self.__values)

    def add_scalar(self, value: int):
        """
        Adds a scalar value to each element in the vector.

        Parameters:
            value (int): The scalar value to be added to each element.

        Returns:
            None
        """
        new_values = []
        for elem in self.__values:
            new_values.append(elem + value)
        self.__values = new_values

    def add_vectors(self, other: 'MyVector'):
        """
        Adds the elements of another vector to this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be added.

        Returns:
            None
        """
        first_values = self.__values
        second_values = other.get_values()
        final_values = []
        for i in range(len(first_values)):
            final_values.append(first_values[i] + second_values[i])
        self.__values = final_values

    def substract_vector(self, other: 'MyVector'):
        """
        Subtracts the elements of another vector from this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be subtracted.

        Returns:
            None
        """
        first_values = self.__values
        second_values = other.get_values()
        final_values = []
        for i in range(len(first_values)):
            final_values.append(first_values[i] - second_values[i])
        self.__values = final_values

    def multiply_vector(self, other: 'MyVector'):
        """
        Multiplies the elements of another vector with this vector element-wise.

        Parameters:
            other (MyVector): The other vector whose elements will be multiplied.

        Returns:
            None
        """
        first_values = self.__values
        second_values = other.get_values()
        final_values = []
        for i in range(len(first_values)):
            final_values.append(first_values[i] * second_values[i])
        self.__values = final_values

    def sum_elements(self) -> int:
        """
        Calculates the sum of all elements in the vector.

        Parameters:
            s (int): The sum of all elements in the vector.
        Returns:
            int: The sum of all elements in the vector.
        """
        s = 0
        for elem in self.__values:
            s += elem
        return s

    def multiply_elements(self) -> int:
        """
        Calculates the product of all elements in the vector.

        Parameters:
            s (int): The product of all elements in the vector.

        Returns:
            int: The product of all elements in the vector.
        """
        s = 1
        for elem in self.__values:
            s *= elem
        return s

    def avg_elements(self) -> float:
        """
        Calculates the average of all elements in the vector.

        Parameters:
            average (float): The average of all elements in the vector.

        Returns:
            float: The average of all elements in the vector.
        """
        average = 0
        for elem in self.__values:
            average += elem
        average /= len(self.__values)
        return average

    def min_elements(self) -> int:
        """
        Finds the minimum element in the vector.

        Parameters:
            None

        Returns:
            int: The smallest element in the vector.
        """
        return min(self.__values)

    def max_elements(self) -> int:
        """
        Finds the maximum element in the vector.

        Parameters:
            None

        Returns:
            int: The largest element in the vector.
        """
        return max(self.__values)












