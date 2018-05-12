import random
import unittest
from unittest import TestCase

from vector3d import Vector3D


def random_int():
    return random.randint(-1000, 1000)


def random_int_vector():
    return Vector3D([random_int(), random_int(), random_int()])


def random_float():
    return random.random() * 2000 - 1000


def random_float_vector():
    return Vector3D([random_float(), random_float(), random_float()])


def random_complex():
    return random_float() + random_float() * 1j


def random_complex_vector():
    return Vector3D([random_complex(), random_complex(), random_complex()])


class Vector3DTest(TestCase):
    def assert_all_of_type(self, elements, the_type):
        for element in elements:
            self.assertTrue(isinstance(element, the_type),
                            '%s is not of type %s' % (element, the_type))

    def test_int_vector3d(self):
        self.assert_all_of_type(Vector3D([1, 2, 3]).elements, int)

    def test_float_vector3d(self):
        self.assert_all_of_type(Vector3D([1., 2., 3.]).elements, float)

    def test_complex_vector3d(self):
        self.assert_all_of_type(Vector3D([1j, 2j, 3j]).elements, complex)

    def test_vector3d_less_than_3_elements(self):
        self.assertRaises(ValueError, lambda: Vector3D([]))
        self.assertRaises(ValueError, lambda: Vector3D([1]))
        self.assertRaises(ValueError, lambda: Vector3D([1, 2]))

    def test_vector3d_more_than_3_elements(self):
        self.assertRaises(ValueError, lambda: Vector3D([1, 2, 3, 4]))
        self.assertRaises(ValueError, lambda: Vector3D([1, 2, 3, 4, 5]))
        self.assertRaises(ValueError, lambda: Vector3D([1, 2, 3, 4, 5, 6]))

    def test_cross_product_on_random_ints(self):
        for _ in range(10):
            a = random_int_vector()
            b = random_int_vector()
            cross = a.cross(b)
            self.assertEqual(cross * a, 0)
            self.assertEqual(cross * b, 0)

    def test_cross_product_on_random_floats(self):
        for _ in range(10):
            a = random_float_vector()
            b = random_float_vector()
            cross = a.cross(b)
            self.assertAlmostEqual(cross * a, 0., 6)
            self.assertAlmostEqual(cross * b, 0., 6)

    def test_cross_product_on_random_complex(self):
        for _ in range(10):
            a = random_complex_vector()
            b = random_complex_vector()
            cross = a.cross(b)
            self.assertAlmostEqual(cross * a, 0j, 6)
            self.assertAlmostEqual(cross * b, 0j, 6)


if __name__ == 'main':
    unittest.main()