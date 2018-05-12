import unittest
from unittest import TestCase

from vector3d import Vector3D


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
        self.assertRaises(ValueError, Vector3D([]))
        self.assertRaises(ValueError, Vector3D([1]))
        self.assertRaises(ValueError, Vector3D([1, 2]))

    def test_vector3d_more_than_3_elements(self):
        self.assertRaises(ValueError, Vector3D([1, 2, 3, 4]))
        self.assertRaises(ValueError, Vector3D([1, 2, 3, 4, 5]))
        self.assertRaises(ValueError, Vector3D([1, 2, 3, 4, 5, 6]))


if __name__ == 'main':
    unittest.main()