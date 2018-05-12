from vector import Vector
from unittest import main, TestCase


class VectorTest(TestCase):
    def assert_all_of_type(self, elements, the_type):
        for element in elements:
            self.assertTrue(isinstance(element, the_type),
                            '%s is not of type %s' % (element, the_type))

    def test_vector_of_integers(self):
        v = Vector.of(1)
        self.assert_all_of_type(v.elements, int)
        v = Vector.of(1, 2)
        self.assert_all_of_type(v.elements, int)
        v = Vector.of(1, 2, 3)
        self.assert_all_of_type(v.elements, int)

    def test_vector_of_integer_strings(self):
        v = Vector.of('1')
        self.assert_all_of_type(v.elements, int)
        v = Vector.of('1', '2')
        self.assert_all_of_type(v.elements, int)
        v = Vector.of('1', '2', '3')
        self.assert_all_of_type(v.elements, int)

    def test_vector_of_floats(self):
        v = Vector.of(1.)
        self.assert_all_of_type(v.elements, float)
        Vector.of(1., 2.)
        self.assert_all_of_type(v.elements, float)
        Vector.of(1., 2., 3.)
        self.assert_all_of_type(v.elements, float)

    def test_vector_of_float_strings(self):
        v = Vector.of('1.')
        self.assert_all_of_type(v.elements, float)
        Vector.of('1.', '2.')
        self.assert_all_of_type(v.elements, float)
        Vector.of('1.', '2.', '3.')
        self.assert_all_of_type(v.elements, float)

    def test_vector_of_complex(self):
        v = Vector.of(1j)
        self.assert_all_of_type(v.elements, complex)
        Vector.of(1j, 2j)
        self.assert_all_of_type(v.elements, complex)
        Vector.of(1j, 2j, 3j)
        self.assert_all_of_type(v.elements, complex)

    def test_vector_of_complex_strings(self):
        v = Vector.of('1j')
        self.assert_all_of_type(v.elements, complex)
        Vector.of('1j', '2j')
        self.assert_all_of_type(v.elements, complex)
        Vector.of('1j', '2j', '3j')
        self.assert_all_of_type(v.elements, complex)

    def test_vector_of_mixed_values(self):
        v = Vector.of(1, '2')
        self.assert_all_of_type(v.elements, int)
        v = Vector.of(1, 2.)
        self.assert_all_of_type(v.elements, float)
        v = Vector.of(1, '2.')
        self.assert_all_of_type(v.elements, float)
        v = Vector.of(1., '2')
        self.assert_all_of_type(v.elements, float)
        v = Vector.of(1j, 2.)
        self.assert_all_of_type(v.elements, complex)
        v = Vector.of(1, 2j)
        self.assert_all_of_type(v.elements, complex)
        v = Vector.of('1.', 2j)
        self.assert_all_of_type(v.elements, complex)
        v = Vector.of(1, 2., '3j')
        self.assert_all_of_type(v.elements, complex)
        v = Vector.of(1j, 2., '3')
        self.assert_all_of_type(v.elements, complex)

    def test_vector_of_cruft(self):
        self.assertRaises(TypeError, lambda: Vector.of(''))
        self.assertRaises(TypeError, lambda: Vector.of('asdf'))
        self.assertRaises(TypeError, lambda: Vector.of({1}))
        self.assertRaises(TypeError, lambda: Vector.of([1]))
        self.assertRaises(TypeError, lambda: Vector.of({1: 2}))

    def test_vector_add(self):
        self.assertEqual(Vector.of(1) + Vector.of(2), Vector.of(3))
        self.assertEqual(Vector.of(1, 2) + Vector.of(3, 4), Vector.of(4, 6))

    def test_vector_sub(self):
        self.assertEqual(Vector.of(3) - Vector.of(2), Vector.of(1))
        self.assertEqual(Vector.of(4, 6) - Vector.of(3, 4), Vector.of(1, 2))

    def test_vector_mult_by_scalar(self):
        self.assertEqual(Vector.of(1) * 1, Vector.of(1))
        self.assertEqual(Vector.of(1) * 2, Vector.of(2))
        self.assertEqual(Vector.of(3) * 2, Vector.of(6))

        self.assertEqual(Vector.of(1.) * 1., Vector.of(1.))
        self.assertEqual(Vector.of(1.) * 2., Vector.of(2.))
        self.assertEqual(Vector.of(3.) * 2., Vector.of(6.))

        self.assertEqual(Vector.of(1j) * 1j, Vector.of(-1+0j))
        self.assertEqual(Vector.of(1j) * 2j, Vector.of(-2+0j))
        self.assertEqual(Vector.of(3j) * 2j, Vector.of(-6+0j))


if __name__ == '__main__':
    main()
