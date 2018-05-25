class Vector:
    """

    Math vector, have standart operations

    """

    def __init__(self, coord):

        """

        creates vector with shown coord

        :param coord: list or tuple of numbers

        """
        
        self._coord = list(coord)
        self._length = len(coord)
    
    def __str__(self):

        """

        show vector in string

        :return: vector in string

        """

        return str(self._coord)
    
    def __len__(self):

        """

        vector's length

        :return: vector's length

        """

        return self._length

    def __add__(self, other):

        """

        sum vectors

        :param other: second vector for sum

        :return: the result of sum two vectors

        """

        return Vector(tuple(self[i] + other[i] for i in range(self._length)))

    def __sub__(self, other):

        """

        self vector minus other vector

        :param other: second vector for minus

        :return: the result of minus two vectors

        """

        return Vector(tuple(self[i] - other[i] for i in range(self._length)))

    def __mul__(self, other):

        """

        if other is vector -> Vector self dot other
        if other is number -> Vector self * other

        :param other: vector or number

        :return: vector self dot vector other or vector self * other

        :raise: TypeError exception if other not vecot and not a number

        """

        if isinstance(other, Vector):
            return sum(self[i] * other[i] for i in range(self._length))

        elif isinstance(other, (int, float, complex)):
            return Vector(tuple(self[i] * other for i in range(self._length)))

        else:
            raise TypeError("Wrong param other: ".format(type(other)))

    def __eq__(self, other):

        """
        compare two vectors

        :param other: vector to compare with self

        :return: if vectors are equal returns true, else false

        """

        return all(self[i] == other[i] for i in range(self._length))

    def __getitem__(self, item):

        """

        returns Vector[item] coordinate

        :param item: coordinate to return

        :return: value Vector[item]

        """

        return self._coord[item]
