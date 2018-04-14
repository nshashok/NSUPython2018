class Vector:
    """Class of algebra vector with standart operations"""

    def __init__(self, *args):
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
        if len(args) == 0:
            self.value = (0,)
        else:
            most_complex = int
            iterable = args
            try:
                if len(args) == 1:
                    iter(args[0])
                    iterable = args[0]
            except TypeError:
                pass
            for val in iterable:
                if not isinstance(val, (int, float, complex)):
                    raise TypeError("init values are not numbers or iterable")
                if most_complex == int:
                    if type(val) == float:
                        most_complex = float
                    elif type(val) == complex:
                        most_complex = complex
                elif most_complex == float and type(val) == complex:
                    most_complex = complex
            self.value = tuple(most_complex(val) for val in iterable)

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
        return Vector(*add)

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
        return Vector(*sub)

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
            return Vector(*mult)

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
