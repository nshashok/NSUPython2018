import operator
import unittest
from typing import Union, List


class Vector:
    def __init__(self, coordinates: Union[List[Union[int, float, complex]], int, float, complex]):
        self._coordinates = coordinates

        if isinstance(coordinates, (int, float, complex)):
            self._coordinates = [coordinates]
            self._len = 1

        else:
            self._len = len(coordinates)

    def __str__(self):
        return "Vector({})".format(str(self._coordinates))

    def __len__(self) -> int:
        return self._len

    def __add__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to add")

        return Vector(list(map(operator.add, self._coordinates, other._coordinates)))

    def __iadd__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to add")

        for i in range(self._len):
            self._coordinates[i] += other._coordinates[i]
        return self

    def __sub__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to subtract")

        return Vector(list(map(operator.sub, self._coordinates, other._coordinates)))

    def __isub__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to subtract")

        for i in range(self._len):
            self._coordinates[i] -= other._coordinates[i]
        return self

    def __mul__(self, other: Union[int, float, complex, 'Vector']) -> Union[int, float, complex, 'Vector']:
        if isinstance(other, (int, float, complex)):
            return Vector([i * other for i in self._coordinates])

        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal to multiply")

        return sum(i for i in map(operator.mul, self._coordinates, other._coordinates))

    def __rmul__(self, other: Union[int, float, complex, 'Vector']) -> Union[int, float, complex, 'Vector']:
        return self * other

    def __imul__(self, scalar: Union[int, float, complex]) -> 'Vector':
        if not isinstance(scalar, (int, float, complex)):
            raise TypeError("Unexpected argument type: {}".format(type(scalar)))

        for i in range(self._len):
            self._coordinates[i] *= scalar
        return self

    def __neg__(self) -> 'Vector':
        return self * -1

    def __eq__(self, other: 'Vector') -> bool:
        if len(self) != len(other):
            return False

        return self._coordinates == other._coordinates

    def __getitem__(self, item: int) -> Union[int, float, complex]:
        if 0 <= item < self._len:
            return self._coordinates[item]
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, key: int, value: Union[int, float, complex]) -> None:
        if 0 <= key < self._len:
            self._coordinates[key] = value
        else:
            raise IndexError("Vector index out of range")


class TestEratosthenes(unittest.TestCase):
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
