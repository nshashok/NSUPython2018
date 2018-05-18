from typing import Sequence

from vector import Vector, T


class Vector3D(Vector):
    def __init__(self, elements: Sequence[T]):
        if len(elements) != 3:
            raise ValueError("3d vector must contain exactly 3 elements")
        super().__init__(elements)

    def cross(self, other: 'Vector3D'):
        return Vector3D([
            self[1]*other[2] - self[2]*other[1],
            self[2]*other[0] - self[0]*other[2],
            self[0]*other[1] - self[1]*other[0],
        ])
