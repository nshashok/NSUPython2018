

class AlmostVector:
    """
    Mathematical vector with a basic vector operations
    """

    def __init__(self, coordinates):
        """
        creates a vector with specified coordinates

        :param coordinates: tuple or list of numbers

        """

        self._length = len(coordinates)
        self._coordinates = list(coordinates)

    def __getitem__(self, item):
        """
        returns vector's 'item' coordinate

        :param item: number of coordinate to return
        :return: value of vector's 'item' coordinate

        """
        return self._coordinates[item]

    def __add__(self, other):
        """
        adds two vectors

        :param other: vector to add with
        :return: the result of adding two vectors

        """

        return AlmostVector(tuple(x + y for x, y in zip(self._coordinates, other._coordinates)))

    def __sub__(self, other):
        """
        subtracts a vector from another vector

        :param other: vector for subtraction
        :return: the result of subtracting one vector from another

        """
        return AlmostVector(tuple(x - y for x, y in zip(self._coordinates, other._coordinates)))

    def __mul__(self, other):
        """
        if 'other' is a scalar then
            multiplies the vector by this scalar
        if 'other' is a vector then
            returns dot product of two vectors

        :param other: scalar or another vector
        :return: dot product of two vectors or result of multiplying one vector by scalar
        :raise: TypeError exception if 'other' is not a number or vector

        """
        if isinstance(other, (int, float, complex)):
            return AlmostVector(map(lambda x: x * other, self._coordinates))
        elif isinstance(other, AlmostVector):
            return sum(x * y for x, y in zip(self._coordinates, other._coordinates))
        else:
            raise TypeError("Wrong type: {}".format(type(other)))

    def __rmul__(self, other):
        """
        reverse multiplication (check __mul__ description)

        :param other: scalar or vector
        :return: dot product of two vectors or result of multiplying one vector by scalar

        """

        return self * other

    def __len__(self):
        """
        gets length of this vector

        :return: vector's length

        """

        return self._length

    def __str__(self):
        """
        gets string representation of this vector

        :return: this vector as a string

        """

        return str(self._coordinates)

    def __eq__(self, other):
        """
        compares two vectors

        :param other: vector to compare with
        :return: true if vectors are equal and false if not

        """

        if self._length != other._length:
            return False

        for x, y in zip(other._coordinates, self._coordinates):
            if x != y:
                return False
        return True

