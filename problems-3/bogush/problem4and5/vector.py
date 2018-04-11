from functools import reduce
from numbers import Number
from typing import Sequence, TypeVar, Callable, Generic, Union

supported_types = [int, float, complex]
T = TypeVar('T', *supported_types)
AnySupported = Union(*supported_types)


class Vector(Generic[T]):
    @staticmethod
    def of(*elements: Number) -> 'Vector[Number]':
        most_complex_type = type(max(elements, key=lambda x: supported_types.index(type(x))))
        elements = [most_complex_type(e) for e in elements]
        return Vector[most_complex_type](elements)

    def __init__(self, elements: Sequence[T]):
        self.elements = list(elements)

    def __len__(self):
        return len(self.elements)

    def combine(self, other: 'Vector[T]' = None,
                combine: 'Callable[[T, T], T]' = lambda a, _: a) -> 'Vector[T]':
        if other is None:
            other = self
        return Vector[T]([combine(a, b) for a, b in zip(self.elements, other.elements)])

    def foreach(self, apply: Callable[[T], T]) -> 'Vector'[T]:
        return Vector[T]([apply(x) for x in self.elements])

    def __add__(self, other: 'Vector[T]') -> 'Vector[T]':
        return self.combine(other, lambda x, y: x + y)

    def __sub__(self, other: 'Vector[T]') -> 'Vector[T]':
        return self.combine(other, lambda x, y: x - y)

    def __mul__(self, factor: AnySupported) -> 'Vector[T]':
        return self.foreach(apply=lambda x: x.__mul__(factor))

    def __and__(self, other: 'Vector[T]') -> T:
        return reduce(lambda r, x, y: r + x * y,
                      zip(self.elements, other.elements), T(0))

    def __repr__(self):
        return str(self.elements)
