from itertools import chain

from vector import Vector
from unittest import main, TestCase


class VectorTest(TestCase):
    test_examples = {
        Vector: {
            int: [
                [0],
                [1],
                [-1],
                [1, 2, 3],
                [-1, -2, -3],
            ],
            float: [
                [0.0],
                [3.14],
                [1.0, 2.0, 3.0],
                [-1.0, -2.0, -3.0],
            ],
            complex: [
                [0j],
                [1j],
                [-1j],
                [1 + 2j],
                [1 - 2j, 3 + 4j, 5j - 6],
            ],
        },
        Vector.of: {
            int: [
                [0],
                [1],
                [-1],
                [1, 2, 3],
                [-1, -2, -3],
            ],
            float: [
                [0.0],
                [3.14],
                [1.0, 2, 3],
                [1, 2, 3.0],
                [1, 2.0, 3],
                [-1, -2, -3.0],
            ],
            complex: [
                [0j],
                [1j],
                [-1j],
                [1 + 2j],
                [1 - 2j, 3, 0],
                [0, 1.0, -1j],
            ],
        },
    }

    all_examples_list = chain(*chain(*[value.values() for value in test_examples.values()]))

    def testInit(self):
        for example_type, examples in VectorTest.test_examples.get(Vector).items():
            for example in examples:
                for elem in Vector[example_type](example):
                    self.assertEqual(type(elem), example_type)

    def testOf(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            Vector.of('a')
            # noinspection PyTypeChecker
            Vector.of(1, 2, 3, '4')
            # noinspection PyTypeChecker
            Vector.of([])

        for example_type, examples in VectorTest.test_examples.get(Vector.of).items():
            for example in examples:
                for elem in Vector.of(*example):
                    self.assertEqual(type(elem), example_type)

        self.assertEqual(Vector.of(1, 2.0), Vector.of(1.0, 2))
        self.assertEqual(Vector.of(1, 0j), Vector.of(1 + 0j, 0))

    def testGetitem(self):
        for example in VectorTest.all_examples_list:
            v = Vector.of(*example)
            for i, elem in enumerate(example):
                self.assertEqual(v[i], elem)

    def checkBinaryOperation(self, operation):
        for example_type, examples in VectorTest.test_examples.get(Vector).items():
            for example1 in examples:
                for example2 in examples:
                    vector1 = Vector[example_type](example1)
                    vector2 = Vector[example_type](example2)
                    vector3 = Vector[example_type]([operation(x, y) for x, y in zip(example1, example2)])
                    self.assertEqual(operation(vector1, vector2), vector3)

    def checkUnaryOperation(self, operation):
        for example_type, examples in VectorTest.test_examples.get(Vector).items():
            for example1 in examples:
                vector1 = Vector[example_type](example1)
                vector2 = operation(vector1)
                for elem1, elem2 in zip(example1, vector2):
                    self.assertEqual(elem2, operation(elem1))

    def testAdd(self):
        self.checkBinaryOperation(lambda x, y: x + y)
        self.assertEqual(Vector.of(1, 2.0, 3.0 + 4.0j) + Vector.of(9, 8.0, 7.0 + 6.0j),
                         Vector.of(10, 10.0, 10.0 + 10.0j))
        v = Vector.of(1, 2, 3)
        self.assertEqual(v + v, v * 2)
        self.assertEqual(v + v - v, v)

    def testSub(self):
        self.checkBinaryOperation(lambda x, y: x - y)
        self.assertEqual(Vector.of(10, 10.0, 10.0 + 10.0j) - Vector.of(1, 2.0, 3.0 + 4.0j),
                         Vector.of(9, 8.0, 7.0 + 6.0j))

    def testMul(self):
        self.checkUnaryOperation(lambda x: x * 2)
        self.checkUnaryOperation(lambda x: x * 3)
        self.checkUnaryOperation(lambda x: x * (-1))


if __name__ == '__main__':
    main()
