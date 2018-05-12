from numbers import Number
from typing import Sequence, TypeVar, Callable, Generic, Union

supported_types = (int, float, complex)
T = TypeVar('T', *supported_types)


def _most_appropriate_cast(value, types):
    for the_type in types:
        if isinstance(value, the_type):
            return value
    # value is not of any type in types.
    # try to cast
    for the_type in reversed(types):
        try:
            return the_type(value)
        except (TypeError, ValueError):
            pass
    raise TypeError('failed to cast to any of types: {}'.format(types))


class Vector(Generic[T]):
    @staticmethod
    def of(*elements) -> 'Vector':
        elements = (_most_appropriate_cast(e, supported_types)
                    for e in elements)

        appropriate_to_all_type = max(
            (type(e) for e in elements),
            key=lambda t: supported_types.index(t)
        )

        elements = map(appropriate_to_all_type, elements)
        return Vector[appropriate_to_all_type](elements)

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
            return self.dot_product(factor)
        else:
            raise TypeError

    def dot_product(self, other: 'Vector[T]') -> T:
        return sum(x * y for x, y in zip(self.elements, other.elements))

    def __eq__(self, other):
        return self.elements == other.elements

    def __getitem__(self, index: int) -> T:
        return self.elements[index]

    def index(self, element: T) -> int:
        return self.elements.index(element)

    def __repr__(self):
        return str(self.elements)
