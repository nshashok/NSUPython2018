import collections
import numbers
import types
from typing import Union


def _is_scalar(obj):
    return type(obj) in [int, float, complex]


class Vector:
    """
    Class Vector models mathematical object vector in n-dimensional vector space
    """

    def __init__(self, *args):
        """
        Constructs a new n-dimensional vector.

        :param content: list of numbers - vector coordinates
        """
        self.__valid_types_ordered = (int, float, complex)
        self.content = []
        self.__length = 0

        if len(args) == 0:
            iterable = []
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, collections.Iterable) or \
                    isinstance(arg, types.GeneratorType):
                iterable = arg
            elif _is_scalar(arg):
                iterable = [arg]
            else:
                raise TypeError("Cannot construct Vector from {}".format(type(arg)))
        else:
            iterable = args

        self.__init_from_iterable(iterable)

    def __init_from_iterable(self, iterable):
        def try_number_cast(element):
            for t in self.__valid_types_ordered:
                try:
                    return t(element)
                except:
                    pass
            raise TypeError("Element {} of type {} is not convertible to number".format(element, type(element)))

        def get_final_type(found_types):
            for t in reversed(self.__valid_types_ordered):
                if t in found_types:
                    return t
            return None

        found_types = set()

        for e in iterable:
            if isinstance(e, numbers.Number):
                found_types.add(type(e))
            else:
                converted = try_number_cast(e)
                found_types.add(type(converted))

        final_type = get_final_type(found_types)

        self.content = [final_type(e) for e in iterable]
        self.__length = len(self.content)

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

    def __mul__(self, other: Union['Vector', complex, float, int]) -> Union['Vector', complex, float, int]:
        """
        Multiply vector by an element, which can be a scalar type or a Vector
        In case of Vector instance dot product is performed.
        In case of scalar type a new vector is returned, constructed from the current one
        with each coordinate multiplied by the scalar passed.

        :param other: Vector or a scalar type (integer, float) - element to multiply by
        :return: float in case a Vector instance was passed. Vector in case a scalar was passed
        :raises: TypeError in case an incompatible type was passed
        """
        if type(other) == type(self):
            if len(other) == len(self):
                return self.__dot_product(other)
            else:
                raise ValueError("Cannot multiply vectors of different lengths")
        elif _is_scalar(other):
            return Vector(self.__mul_by_scalar(other))

        raise TypeError("Multiplication is not defined for type " + str(type(other)))

    def __rmul__(self, other: Union['Vector', complex, float, int]) -> Union['Vector', complex, float, int]:
        """
        Perform right multiplication with same effect as left multiplication

        :param other: Vector or a scalar type (integer, float) - element to multiply by
        :return: float in case a Vector instance was passed. Vector in case a scalar was passed
        :raises: TypeError in case an incompatible type was passed
        """
        return self * other

    def __imul__(self, scalar: Union[complex, float, int]) -> 'Vector':
        """
        Modify current vector by multiplying its content by a scalar

        :param scalar: scalar to multiply current vector by
        :return: current vector with modified content
        """
        if _is_scalar(scalar):
            raise TypeError("Multiplication-assignment is not defined for type {}".format(type(scalar)))

        self.content = self.__mul_by_scalar(scalar)
        return self

    def __mul_by_scalar(self, scalar) -> list:
        return [x * scalar for x in self.content]

    def __dot_product(self, vector: 'Vector'):
        return sum(x * y for x, y in zip(self.content, vector.content))

    def __add__(self, vector: 'Vector') -> 'Vector':
        """
        Sum current vector with another one, which must have the same size

        :param vector: vector to sum with
        :return: new vector with coordinates defined as the sum of corresponding
            coordinates
        :raise: TypeError in case an incompatible type was passed
        :raise: ValueError in case a *vector* of incompatible length was passed
        """
        if type(vector) != type(self):
            raise TypeError("Addition is not defined for type " + str(type(vector)))

        if vector.__length != self.__length:
            raise ValueError("Vector sizes must match")

        return Vector([x + y for x, y in zip(self.content, vector.content)])

    def __sub__(self, vector: 'Vector') -> 'Vector':
        """
        Subtract another vector from the current one. Vectors must have the same size.

        :param vector: vector to subtract
        :return: new vector with coordinates defined as the difference of corresponding
            coordinates
        :raise: TypeError in case an incompatible type was passed
        :raise: ValueError in case a *vector* of incompatible length was passed
        """
        if type(vector) != type(self):
            raise TypeError("Subtraction is not defined for type " + str(type(vector)))

        if vector.__length != self.__length:
            raise ValueError("Vector sizes must match")

        return Vector([x - y for x, y in zip(self.content, vector.content)])

    def __len__(self) -> int:
        """
        Get vector length

        :return: vector length
        """
        return self.__length

    def __getitem__(self, key: int) -> Union[complex, float, int]:
        """
        Get vector coordinate value

        :param key: positive zero-based index of coordinate to retrieve
        :return: coordinate value
        :raise: TypeError in case invalid *key* type was passed
        :raise: IndexError in case *key* is not inside range [0, len(vector))
        """
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")

        if 0 <= key < self.__length:
            return self.content[key]
        else:
            raise IndexError("Index out of range. Got index: {} (Vector length: {})".format(key, self.__length))

    def __str__(self):
        return "Vector({0})".format(str(self.content))
