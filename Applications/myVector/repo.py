from My_Vector import MyVector
from My_Vector import colors
import matplotlib.pyplot as plt

class VectorRepository:

    def __init__(self):
        self.__vectors = []

    def add_vector(self, vector: 'MyVector'):
        """
        Adds a vector to the repository after validating its attributes.

        Parameters:
            vector (MyVector): The vector to add.

        Raises:
            TypeError: If the vector attributes do not meet the expected types or constraints.
        """
        if not isinstance(vector.get_name_id(), int | str):
            raise TypeError('Name id must be int|str')
        if vector.get_colour() not in colors:
            raise TypeError('Colour must be in colors')
        if not isinstance(vector.get_type(), int):
            raise TypeError('Type must be int')
        if not isinstance(vector.get_values(), list):
            raise TypeError('Values must be list')
        self.__vectors.append(vector)

    def get_vectors(self) -> list['MyVector']:
        """
        Retrieves all vectors in the repository.

        Returns:
            list[MyVector]: The list of vectors.
        """
        return self.__vectors

    def get_vector_by_index(self, index) -> MyVector:
        """
        Retrieves a vector by its index.

        Parameters:
            index (int): The index of the vector to retrieve.

        Returns:
            MyVector: The vector at the specified index.
        """
        return self.__vectors[index]

    def update_by_index(self, index: int, name_id: int | str, colour: str, type: int, values: list) -> None:
        """
        Updates the attributes of a vector at a specified index.

        Parameters:
            index (int): The index of the vector to update.
            name_id (int|str): The new name ID for the vector.
            colour (str): The new color for the vector.
            type (int): The new type for the vector.
            values (list): The new values for the vector.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If the attributes do not meet the expected types.
        """
        if index < 0 or index >= len(self.__vectors):
            raise IndexError('Index out of range')
        if isinstance(name_id, int | str):
            self.__vectors[index].set_name_id(name_id)
        else:
            raise TypeError('Name id must be int|str')
        if colour in colors:
            self.__vectors[index].set_colour(colour)
        else:
            raise TypeError('Colour must be in colors')
        if isinstance(type, int):
            self.__vectors[index].set_type(type)
        else:
            raise TypeError('Type must be int')
        if isinstance(values, list):
            self.__vectors[index].set_values(values)
        else:
            raise TypeError('Values must be list')

    def update_by_name(self, name_id: int | str, colour: str, type: int, values: list):
        """
        Updates the attributes of a vector identified by its name ID.

        Parameters:
            name_id (int|str): The name ID of the vector to update.
            colour (str): The new color for the vector.
            type (int): The new type for the vector.
            values (list): The new values for the vector.
        """
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                self.update_by_index(i, name_id, colour, type, values)

    def delete_by_index(self, index: int):
        """
        Deletes a vector at a specified index.

        Parameters:
            index (int): The index of the vector to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.__vectors):
            raise IndexError('Index out of range')
        self.__vectors.pop(index)

    def delete_by_name(self, name_id: int | str):
        """
        Deletes all vectors with a specified name ID.

        Parameters:
            name_id (int|str): The name ID of the vectors to delete.

        Raises:
            TypeError: If the name ID is not of the expected type.
        """
        if not isinstance(name_id, int | str):
            raise TypeError('Name_id must be int|str')
        for i in reversed(range(len(self.__vectors))):
            if self.__vectors[i].get_name_id() == name_id:
                self.delete_by_index(i)

    def max_sum_greater_than_value(self, value: int) -> MyVector | None:
        """
        Finds the vector with the maximum sum of elements, if the sum is greater than a given value.

        Parameters:
            value (int): The threshold value.

        Returns:
            MyVector|None: The vector with the maximum sum if it exceeds the value, otherwise None.

        Raises:
            ValueError: If the threshold value is negative.
        """
        if value < 0:
            raise ValueError('Value must be greater than zero')
        v = max(self.__vectors, key=lambda vector: vector.sum_elements())
        if v.sum_elements() > value:
            return v.sum_elements()
        return None

    def delete_product_greater_than_value(self, value: int):
        """
        Deletes all vectors whose product of elements is greater than a given value.

        Parameters:
            value (int): The threshold value.
        """
        for i in reversed(range(len(self.__vectors))):
            if self.__vectors[i].multiply_elements() > value:
                self.__vectors.pop(i)

    def update_by_type(self, type: int, color: str) -> None:
        """
        Updates the color of all vectors with a specified type.

        Parameters:
            type (int): The type of vectors to update.
            color (str): The new color to assign.

        Raises:
            TypeError: If the type or color do not meet expected constraints.
        """
        if not isinstance(type, int):
            raise TypeError('Type must be int')
        if color not in colors:
            raise TypeError('Colour must be in colors')

        for vector in self.__vectors:
            if vector.get_type() == type:
                vector.set_colour(color)

    def plot_vectors(self):
        """
        Plots all vectors in the repository on a 2D chart using matplotlib.

        The X and Y coordinates for each vector are derived from its first two values.
        The marker shape depends on the vector type, and the color is set based on the vector's color.
        """
        marker_map = {
            1: 'o',  # Circle
            2: 's',  # Square
            3: '^',  # Triangle
        }
        for vector in self.__vectors:
            marker = marker_map.get(vector.get_type(), 'D')  # Default to Diamond
            plt.scatter(
                vector.get_values()[0],
                vector.get_values()[1],
                color=vector.get_colour(),
                label=f'{vector.get_name_id()}',
                marker=marker,
                s=100  # Marker size
            )

        plt.title("Vector Plot")
        plt.legend(title="Vector ID")
        plt.grid(True)
        plt.show()
