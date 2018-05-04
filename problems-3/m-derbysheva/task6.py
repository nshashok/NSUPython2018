from itertools import tee
from types import GeneratorType


class Vector:
    """Class of algebra vector with standart operations"""

    def __init__(self, *args, **kwargs):
        """initialisation of Vector

        Parameters
        -----------
        args: tuple of elements of Vector

        Returns
        -----------
        New instance of Vector, if args are null returns (0)

        Raises
        -----------
        TypeError
            if args are not a number
        """
        if "types" in kwargs:
            types = kwargs["types"]
        else:
            types = (int, float, complex)
        if len(args) == 0:
            raise TypeError("Empty list of arguments")
        else:
            iterable = args
            type_index = 0
            try:
                if len(args) == 1:
                    if isinstance(args[0], GeneratorType):
                        iterable = args[0]
                    else:
                        while type_index < len(types):
                            try:
                                types[type_index](args[0])
                                break
                            except (TypeError, ValueError):
                                type_index += 1
                        else:
                            type_index = 0
                            iter(args[0])
                            iterable = args[0]
            except TypeError:
                pass
            it1, it2 = tee(iterable, 2)
            for val in it1:
                while type_index < len(types):
                    try:
                        types[type_index](val)
                        for i in range(type_index + 1, len(types)):
                            if isinstance(val, types[i]):
                                type_index = i
                                break
                        break
                    except (TypeError, ValueError):
                        type_index += 1
                else:
                    raise TypeError("init values are not numbers or iterable")
            self.value = tuple(types[type_index](val) for val in it2)

    def __getitem__(self, idx):
        """get element by index
        Parameters
        -----------
        idx: int

        Returns
        -----------
        num: number
            Value of element by index

        Raises
        -----------
        TypeError
            if index is not an integer
        IndexError
            if index is out of bounds
        """
        if type(idx) is not int:
            raise TypeError("index must be integer")

        if idx > len(self.value) or idx < 0:
            raise IndexError("out of bounds")
        return self.value[idx]

    def __str__(self):
        """string representation of vector
        Returns
        -----------
        str: string
        """
        return str(self.value)

    def __len__(self):
        """lenght of vector
        Returns
        -----------
        num: int
            number of elements
        """
        return len(self.value)

    def __add__(self, v):
        """summ of two vectors in new instance of Vector
        Parameters
        -----------
        v: Vector
        Returns
        -----------
        result: Vector
            Result which is a new instance
        Raises
        -----------
        TypeError
            if v is not a Vector
        ValueError
            if two Vectors have different lenght
        """
        if not isinstance(v, Vector):
            raise TypeError("trying to add something that is not a Vector")
        if len(self) != len(v):
            raise ValueError("Vectors are different sizes")

        add = tuple(i + j for i, j in zip(self, v))
        return Vector(add)

    def __sub__(self, v):
        """subtraction of two vectors (self - another vector) in new instance of Vector
        Parameters
        -----------
        v: Vector
        Returns
        -----------
        result: Vector
            Result which is a new instance
        Raises
        -----------
        TypeError
            if v is not a Vector
        ValueError
            if two Vectors have different lenght
        """
        if not isinstance(v, Vector):
            raise TypeError("trying to subtract something"
                            " that is not a Vector")
        if len(self) != len(v):
            raise ValueError("Vectors are different sizes")

        sub = tuple(i - j for i, j in zip(self, v))
        return Vector(sub)

    def __mul__(self, num):
        """multiplication on number in new instance of Vector
        or dot product with another Vector
        Parameters
        -----------
        num: number or Vector
        Returns
        -----------
        result: Vector or number
            Result which is a new instance
        Raises
        -----------
        TypeError
            if v is not a Vector or number
        ValueError
            if two Vectors have different lenght
        """
        if isinstance(num, Vector):
            if len(self) != len(num):
                raise ValueError("Vectors are different sizes")
            return sum(i * j for i, j in zip(self, num))
        else:
            if not isinstance(num, (int, float, complex)):
                raise TypeError("Argument is not a Vector or number")
            mult = tuple(i * num for i in self)
            return Vector(mult)

    def __eq__(self, v):
        """comparing two vectors
        Parameters
        -----------
        v: Vector
        Returns
        -----------
        ans: boolean
            True if vectors are equal, False in all other occasions
        """
        if not isinstance(v, Vector):
            return False
        return self.value == v.value


class Vector3D(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        if len(self.value) != 3:
            raise TypeError("wrong number of arguments")

    def cross(self, vector):
        if not isinstance(vector, Vector3D):
            raise TypeError("vector is not a Vector3D")
        if len(vector.value) == len(self.value):
            return Vector3D(self[1] * vector[2] - self[2] * vector[1],
                            self[2] * vector[0] - self[0] * vector[2],
                            self[0] * vector[1] - self[1] * vector[0])
