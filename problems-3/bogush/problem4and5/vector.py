from numbers import Number
from typing import Sequence, TypeVar, Callable, Generic, Union

supported_types = [int, float, complex]
T = TypeVar('T', *supported_types)


class Vector(Generic[T]):
    @staticmethod
    def of(*elements: Number) -> 'Vector':
        if not all((type(x) in supported_types for x in elements)):
            raise TypeError
        most_complex_type = type(max(elements, key=lambda x: supported_types.index(type(x))))
        elements = [most_complex_type(e) for e in elements]
        return Vector[most_complex_type](elements)

    def __init__(self, elements: Sequence[T]):
        self.elements = list(elements)

    def __len__(self):
        return len(self.elements)

    def map(self, apply: Callable[[T], T]) -> 'Vector[T]':
        return Vector[T]([apply(x) for x in self.elements])

    def __add__(self, other: 'Vector[T]') -> 'Vector[T]':
        return Vector[T]([x + y for x, y in zip(self.elements, other.elements)])

    def __sub__(self, other: 'Vector[T]') -> 'Vector[T]':
        return Vector[T]([x - y for x, y in zip(self.elements, other.elements)])

    def __mul__(self, factor: Union[Number, 'Vector[T]']) -> 'Vector[T]':
        if isinstance(factor, Number):
            return self.map(apply=lambda x: x.__mul__(factor))
        elif isinstance(factor, Vector) and len(factor) == len(self):
            return self & factor
        else:
            raise TypeError

    def __and__(self, other: 'Vector[T]') -> T:
        return sum(x * y for x, y in zip(self.elements, other.elements))

    def __eq__(self, other):
        return self.elements == other.elements

    def __getitem__(self, index: int) -> T:
        return self.elements[index]

    def index(self, element: T) -> int:
        return self.elements.index(element)

    def __repr__(self):
        return str(self.elements)
