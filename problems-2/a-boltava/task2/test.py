from .task2 import Vector
import unittest


class VectorTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Vector.empty(), Vector.empty())
        self.assertEqual(Vector.zero(2), Vector.zero(2))
        self.assertEqual(Vector([1,2,3,4]), Vector([1,2,3,4]))

    def test_addition(self):
        self.assert_type_error(lambda _: Vector([1]) + 1)
        self.assert_type_error(lambda _: Vector([1]) + "string")

        a = Vector([1,2,3])
        b = Vector([1,2,3])
        c = Vector([2,4,6])

        self.assertTrue(a + b == c)
        self.assertTrue(a + Vector([0,0,0]) == a)
        self.assertTrue(Vector([1]) + Vector([2]) == Vector([3]))
        self.assertTrue(Vector([1,2,3]) + Vector([2,3,4]) == Vector([3,5,7]))

    def test_subtraction(self):
        self.assert_type_error(lambda _: Vector([1]) + 1)
        self.assert_type_error(lambda _: Vector([1]) + "string")

        a = Vector([1,2,3])
        b = Vector([1,2,3])
        c = Vector([2,4,6])

        self.assertTrue(a - b == Vector.zero(3))
        self.assertTrue(a - Vector.zero(3) == a)
        self.assertTrue(Vector([1]) - Vector([2]) == Vector([-1]))
        self.assertTrue(Vector([1,2,3]) - Vector([2,3,4]) == Vector([-1,-1,-1]))

    def test_dot_product(self):
        self.assert_type_error(lambda _: Vector([1]) * "abc")

        v = Vector([1,2,3])
        self.assertEqual(v*v, 14)
        self.assertEqual(v * Vector([0] * len(v)), 0)
        self.assertEqual(Vector([1,2,3]) * Vector([3,2,1]), 10)

    def assert_type_error(self, func):
        with self.assertRaises(TypeError):
            func()

    def test_length(self):
        for length in range(1,10):
            self.assertEqual(len(Vector([0]*length)), length)

    def test_multiplication_by_scalar(self):
        self.assert_type_error(lambda _: Vector([1]) * "abc")

        content = []
        for scalar in range(10):
            content += [scalar]
            self.assertEqual(scalar * Vector(content), Vector([scalar*x for x in content]))

        content = [1,2,3]
        scalar = 3.5
        self.assertEqual(Vector(content) * scalar, Vector([scalar * x for x in content]))

    def test_getitem(self):
        self.assert_type_error(lambda _: Vector([1])["abc"])

        length = 100
        v = Vector([n for n in range(length)])
        with self.assertRaises(IndexError):
            a = v[length + 1]

        for n in range(length):
            self.assertEqual(n, v[n])


if __name__ == "__main__":
    unittest.main()
