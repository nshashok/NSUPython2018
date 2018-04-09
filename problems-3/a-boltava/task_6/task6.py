from .vector import Vector


class Vector3D(Vector):

    def __init__(self, *args):
        super().__init__(*args)
        if len(self) != 3:
            raise ValueError("Vector must be of length 3")

    def cross_product(self, other: 'Vector3D'):
        if not isinstance(other, Vector3D):
            raise TypeError("Vector3D required for cross product")

        return Vector3D(
            self[1]*other[2] - self[2]*other[1],
            self[0]*other[2] - self[2]*other[0],
            self[0]*other[1] - self[1]*other[0]
        )
