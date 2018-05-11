import collections
import numbers
import operator
import types
import unittest
from typing import Union


class Vector:
    """
    One-dimensional vector of linear algebra with standard vector operations.

    """

    def __init__(self, *args):
        """
        Create vector.
        :param coordinates: list or tuple of elements that can be cast to number - vector coordinates,
                            or one element that can be cast to number - vector of length 1
        """

        if len(args) == 0:
            self._coordinates = []
            self._len = 0
        elif len(args) == 1:
            if isinstance(args[0], types.GeneratorType) or isinstance(args, collections.Iterable):
                self._coordinates = list(args[0])
                self._len = len(self._coordinates)
            else:
                self._coordinates = [args[0]]
                self._len = 1
        else:
            self._coordinates = [*args]
            self._len = len(self._coordinates)

        self.__cast_to_general_type()

    def __cast_to_general_type(self):
        types = set()
        for coordinate in self._coordinates:
            if isinstance(coordinate, numbers.Number):
                types.add(type(coordinate))
            else:
                coordinate = self._parse(coordinate, (int, float, complex))
                types.add(type(coordinate))

        for i in (complex, float, int):
            if i in types:
                self._coordinates = [i(elem) for elem in self._coordinates]
                break

    @staticmethod
    def _parse(value, types):
        for type in types:
            try:
                return type(value)
            except ValueError:
                pass
        raise TypeError("{} is not a number".format(value))

    def __str__(self):
        """
        String representation of vector.
        :return: str: format - Vector([c0, c1, ..., cn])
        """
        return "Vector({})".format(str(self._coordinates))

    def __len__(self) -> int:
        """
        Size of vector.
        :return: int
        """
        return self._len

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Add two vectors and return the result in new vector.
        :param other: Vector
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector
        """
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to add")

        return Vector(list(map(operator.add, self._coordinates, other._coordinates)))

    def __iadd__(self, other: 'Vector') -> 'Vector':
        """
        Add vector `other` to vector `self` and assign the result to vector `self`.
        :param other: Vector
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector
        """
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to add")

        for i in range(self._len):
            self._coordinates[i] += other._coordinates[i]
        return self

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtract vector `other` from vector `self` and return the result in new vector.
        :param other: Vector
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector
        """
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to subtract")

        return Vector(list(map(operator.sub, self._coordinates, other._coordinates)))

    def __isub__(self, other: 'Vector') -> 'Vector':
        """
        Subtract vector `other` from vector `self` and assign the result to vector `self`.
        :param other: Vector
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector
        """
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to subtract")

        for i in range(self._len):
            self._coordinates[i] -= other._coordinates[i]
        return self

    def __mul__(self, other: Union[int, float, complex, 'Vector']) -> Union[int, float, complex, 'Vector']:
        """
        If `other` is int, float, or complex then return new vector which represent multiplication vector `self`
        to scalar `other`.
        If `other` is Vector then return number which represent scalar product of vectors `self` and `other`.
        :param other: Vector, or number - int, float, complex
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector, or number - int, float, complex
        """
        if isinstance(other, (int, float, complex)):
            return Vector([i * other for i in self._coordinates])

        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to multiply")

        return sum(i for i in map(operator.mul, self._coordinates, other._coordinates))

    def __rmul__(self, other: Union[int, float, complex, 'Vector']) -> Union[int, float, complex, 'Vector']:
        """
        If `other` is int, float, or complex then return new vector which represent multiplication vector `self`
        to scalar `other`.
        If `other` is Vector then return number which represent scalar product of vectors `self` and `other`.
        :param other: Vector, or number - int, float, complex
        :raise: ValueError: if lengths of vectors not equal
        :return: Vector, or number - int, float, complex
        """
        return self * other

    def __imul__(self, other: Union[int, float, complex]) -> 'Vector':
        """
        Multiply vector `self` on scalar `other` and assign the result to vector `scalar`.
        :param other: number - int, float, complex
        :raise: TypeError: if unexpected argument type got
        :return: Vector, or number - int, float, complex
        """
        if not isinstance(other, (int, float, complex)):
            raise TypeError("Unexpected argument type: {}".format(type(other)))

        for i in range(self._len):
            self._coordinates[i] *= other
        return self

    def __neg__(self) -> 'Vector':
        """
        Change sign of all coordinates in vector.
        :return: Vector
        """
        return self * -1

    def __eq__(self, other: 'Vector') -> bool:
        """
        Check two vectors on equal.
        :param other: Vector
        :return: bool
        """
        if len(self) != len(other):
            return False

        return self._coordinates == other._coordinates

    def __getitem__(self, item: int) -> Union[int, float, complex]:
        """
        Get value of vector coordinate.
        :param item: int
        :raise: IndexError: if `item` not in range [0, len(vector) - 1]
        :return: number - int, float or complex
        """
        if 0 <= item < self._len:
            return self._coordinates[item]
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, key: int, value: Union[int, float, complex]) -> None:
        """
        Set value `value` to coordinate `key` of vector.
        :param key: int
        :param value: number - int, float or complex
        :raise: IndexError: if `key` not in range [0, len(vector) - 1]
        :return: None
        """
        if 0 <= key < self._len:
            self._coordinates[key] = value
        else:
            raise IndexError("Vector index out of range")


class TestVector(unittest.TestCase):
    def test_constructor(self):
        Vector()
        Vector("1", 2, 2.5, 3.5+1j, "15+2j")
        with self.assertRaises(TypeError):
            Vector("a")
        with self.assertRaises(TypeError):
            Vector(1, "2", "vector")

    def test_cast_to_general_type(self):
        vector = Vector("1", 2.5, "3+j")
        self.assertTrue(all(type(elem) is complex for elem in vector))
        vector = Vector("1", 2.5, "3")
        self.assertTrue(all(type(elem) is float for elem in vector))

    def test_len(self):
        a = Vector([1, 2, 3])
        self.assertEqual(len(a), 3)

    def test_add(self):
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        c = Vector([0, 0, 0])
        d = Vector([1, 2])

        self.assertEqual(Vector([2, 4, 6]), a + b)
        self.assertEqual(a, a + c)
        with self.assertRaises(ValueError):
            a + d

    def test_iadd(self):
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        c = Vector([0, 0, 0])
        d = Vector([1, 2])

        a += b
        self.assertEqual(Vector([2, 4, 6]), a)
        a += c
        self.assertEqual(Vector([2, 4, 6]), a)
        with self.assertRaises(ValueError):
            a += d

    def test_sub(self):
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        c = Vector([0, 0, 0])
        d = Vector([1, 2])

        self.assertEqual(c, a - b)
        self.assertEqual(a, a - c)
        with self.assertRaises(ValueError):
            a - d

    def test_isub(self):
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        c = Vector([0, 0, 0])
        d = Vector([1, 2])

        a -= b
        self.assertEqual(c, a)
        b -= c
        self.assertEqual(Vector([1, 2, 3]), b)
        with self.assertRaises(ValueError):
            a -= d

    def test_mul(self):
        a = Vector([1, 2, 3])
        b = Vector([2, 4, 6])
        c = Vector([0, 0, 0])
        d = Vector([1, 2])

        self.assertEqual(28, a * b)
        self.assertEqual(0, a * c)
        self.assertEqual(b, a * 2)
        self.assertEqual(b, 2 * a)
        with self.assertRaises(ValueError):
            a * d

    def test_imul(self):
        a = Vector([1, 2, 3])
        b = Vector([2, 4, 6])

        a *= 2
        self.assertEqual(b, a)
        with self.assertRaises(TypeError):
            a *= b

    def test_neg(self):
        a = Vector([1, 2, 3])
        b = Vector([-1, -2, -3])

        self.assertEqual(b, -a)

    def test_equal(self):
        self.assertTrue(Vector([1, 2, 3]) == Vector([1, 2, 3]))
        self.assertTrue(Vector([0]) == Vector([0]))
        self.assertTrue(Vector([0]) != Vector([1]))

    def test_setitem_getitem(self):
        a = Vector([1, 2, 3])
        a[0] = 0
        self.assertEqual(0, a[0])
        a[1] = 0
        self.assertEqual(0, a[1])
        a[2] = 0
        self.assertEqual(0, a[2])
        with self.assertRaises(IndexError):
            c = a[3]
        with self.assertRaises(IndexError):
            c = a[-1]


if __name__ == "__main__":
    unittest.main()
