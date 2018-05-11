from itertools import zip_longest


class Vector(object):
    """Vector with float numbers.

    Attributes:
        values (list): Vector values.
    """

    def __init__(self, *args):
        """Creates a new vector and checks parameters.

        Args:
             args(Union): float of str values
        """
        self.values = [float(a) for a in args]

    def __add__(self, other):
        """Sums two vectors.

        Args:
             other(object): object to summarize with.

        Returns:
            Vector: if isinstance(other, Vector) is true.
            None: otherwise.
        """
        if isinstance(other, Vector):
            return Vector(*([a[0] + a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)]))

    def __sub__(self, other):
        """Subtracts two vectors.

        Args:
             other(object): object to subtract self vector with.

        Returns:
            Vector: if isinstance(other, Vector) is true.
            None: otherwise.
        """
        if isinstance(other, Vector):
            return Vector(*([a[0] - a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)]))

    def __mul__(self, other):
        """Multiplies two vectors (scalar) or multiplies self vector with a number.

        Args:
            other(object): object to multiply self vector with.

        Returns:
            float: if isinstance(other, Vector) is true.
            Vector: if isinstance(other, type(1)) or isinstance(other, type(1.0)) is true.
            None: otherwise.
        """
        if isinstance(other, Vector):
            return sum([a[0] * a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)])
        elif isinstance(other, type(1)) or isinstance(other, type(1.0)):
            return Vector(*([a * other for a in self.values]))

    def __rmul__(self, other):
        """Multiplies self vector with a number from the right.

        Args:
            other(object): 

        Returns:
            Vector: if isinstance(other, Vector) is true.
            None: otherwise.
        """
        if isinstance(other, type(1)) or isinstance(other, type(1.0)):
            return Vector(*([a * other for a in self.values]))

    def __truediv__(self, other):
        """Divides self vector by a number.

        Args:
            other(object): 

        Returns:
            Vector: if other is float or integer.
            None: otherwise.
        """
        if isinstance(other, type(1)) or isinstance(other, type(1.0)):
            divided = tuple(a / other for a in self.values)
            return Vector(*divided)

    def __len__(self):
        """Returns length of the vector.

        Returns:
            int
        """
        return len(self.values)

    def __eq__(self, other):
        """Checks if two Vectors have the same values.

        Args:
            other(object): 

        Returns:
            bool: true if other has the same values as self, false otherwise.
            None: if other is not Vector.
        """
        if isinstance(other, Vector):
            return self.values == other.values

    def __ne__(self, other):
        """Checks if two Vectors don't have the same values

        Args:
            other(object): 

        Returns:
            bool: true if other doesn't have the same values as self, false otherwise.
            None: if other is not Vector.
        """
        if isinstance(other, Vector):
            return self.values != other.values

    def __getitem__(self, key):
        """Returns the value under the key number.

        Args:
            key(int): key. 

        Returns:
            float
        """
        return self.values[key]

    def __setitem__(self, key, value):
        """Sets the value under the key number.

        Args:
            key(int): 
            value: 

        Returns:
            None

        Raises:
            IndexError: if value can't be converted to float
        """
        try:
            self.values[key] = float(value)
        except IndexError:
            raise IndexError("Vector assignment index out of range")

    def __str__(self):
        """Creates string view of Vector

        Returns:
            str
        """
        return "Vector of len=%s: %s" % (self.__len__(), self.values)


def test():
    vector1 = Vector(1, 2, 3, 4, 5)
    vector2 = Vector(6, 7, 8)
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Sum v1 + v2:", vector1 + vector2)
    print("Sum v1 + 5:", vector1 + 5)
    print("Div by 5 v1:", vector1 / 5)
    print("Mul by 5 v1:", vector1 * 5)
    print("RMul by 5 v1:", 5 * vector1)
    print("Scalar mul v1 * v2:", vector1 * vector2)
    print("Item 3 of v1:", vector1[3])
    vector1[3] = 15
    print("Changed v1:", vector1)
    print("v1 == v2:", vector1 is vector2)
    print("v1 != v2:", vector1 is not vector2)
    try:
        vector2[3] = 15
    except IndexError as e:
        print("\tInvalid:", e)
    try:
        vector3 = Vector("a", 7, 8)
    except ValueError as e:
        print("\tInvalid:", e)


if __name__ == "__main__":
    test()