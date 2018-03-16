from typing import Union, List


class Vector:
    """
    Class Vector emulates mathematical object vector in n-dimensional vector space,
    where n is the vector length.
    """

    def __init__(self, content: List[Union[int, float]]):
        """
        Constructs a new n-dimensional vector.

        :param content: list of numbers - vector coordinates
        """
        self.content = content
        self.__length = len(content)

    @staticmethod
    def zero(length: int):
        return Vector([0] * length)

    @staticmethod
    def empty():
        return Vector([])

    def __eq__(self, vector: 'Vector') -> bool:
        """
        Check if two vectors are equal. Vectors are considered equal if their lengths and contents are equal
        
        :param vector: vector
        :return: true if vectors are equal, false otherwise
        """
        return type(self) == type(vector) and \
               self.__length == vector.__length and \
               self.content == vector.content

    def __ne__(self, vector: 'Vector') -> bool:
        return not (self == vector)

    def __mul__(self, other: Union['Vector', float, int]) -> Union['Vector', float]:
        """
        Multiply vector by an element, which can be a scalar type (int, float) or a Vector
        In case of Vector instance dot product is performed.
        In of scalar type a new vector returned, constructed from the current one
        with each coordinate multiplied by the scalar passed.

        :param other: Vector or a scalar type (integer, float) - element to multiply by
        :return: float in case a Vector instance was passed. Vector in case a scalar was passed/
        :raises: TypeError in case an incompatible type was passed
        """
        if type(other) in [int, float]:
            return Vector(content=self.__mul_by_scalar(other))
        if type(other) == type(self):
            return self.__dot_product(other)

        raise TypeError("Multiplication is not defined for type " + str(type(other)))

    def __rmul__(self, other: Union['Vector', float, int]) -> Union['Vector', float]:
        """
        Multiply vector by an element, which can be a scalar type (int, float) or a Vector
        In case of Vector instance dot product is performed.
        In of scalar type a new vector returned, constructed from the current one
        with each coordinate multiplied by the scalar passed.

        :param other: Vector or a scalar type (integer, float) - element to multiply by
        :return: float in case a Vector instance was passed. Vector in case a scalar was passed/
        :raises: TypeError in case an incompatible type was passed
        """
        return self * other

    def __imul__(self, scalar: Union[float, int]) -> 'Vector':
        if type(scalar) not in [float, int]:
            raise TypeError("Multiplication-assignment is not defined for type {}".format(type(scalar)))

        self.content = self.__mul_by_scalar(scalar)
        return self

    def __mul_by_scalar(self, scalar) -> list:
        return [x*scalar for x in self.content]

    def __dot_product(self, vector) -> float:
        return float(sum(x*y for x, y in zip(self.content, vector.content)))

    def __add__(self, vector: 'Vector') -> 'Vector':
        """
        Sums current vector with another one, which must have the same size

        :param vector: vector to sum with
        :return: new vector with coordinated defined as the sum of corresponding
            coordinates
        :raise: TypeError in case an incompatible type was passed
        :raise: ValueError in case a *vector* of incompatible length was passed
        """
        if type(vector) != type(self):
            raise TypeError("Addition is not defined for type " + str(type(vector)))

        if vector.__length != self.__length:
            raise ValueError("Vector sizes must match")

        return Vector([x + y for x,y in zip(self.content, vector.content)])

    def __sub__(self, vector: 'Vector') -> 'Vector':
        """
        Subtract another vector from the current one. Vectors must have the same size.

        :param vector: vector to subtract
        :return: new vector with coordinated defined as the difference of corresponding
            coordinates
        :raise: TypeError in case an incompatible type was passed
        :raise: ValueError in case a *vector* of incompatible length was passed
        """
        if type(vector) != type(self):
            raise TypeError("Subtraction is not defined for type " + str(type(vector)))

        if vector.__length != self.__length:
            raise ValueError("Vector sizes must match")

        return Vector([x - y for x,y in zip(self.content, vector.content)])

    def __len__(self) -> int:
        """
        Get vector length

        :return: vector length
        """
        return self.__length

    def __getitem__(self, key: int) -> float:
        """
        Get vector coordinate value

        :param key: positive zero-based index of coordinate to retrieve
        :return: coordinate value
        :raise: TypeError in case invalid *key* type was passed
        :raise: IndexError in case *key* is not inside range [0, len(vector)]
        """
        if not isinstance(key, int):
            raise TypeError("Key must either be an integer")

        if 0 <= key < self.__length:
            return float(self.content[key])
        else:
            raise IndexError("Index out of range. Got index: {} (Vector length: {})".format(key, self.__length))

    def __str__(self):
        return "Vector({0})".format((str(self.content)))
