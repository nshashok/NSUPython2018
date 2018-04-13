import types
from itertools import zip_longest


class Vector(object):
    def __init__(self, *args):
        self.__complex = None
        print(type(args))
        if len(args) == 1:
            l = (0,0,0)
            if isinstance(*args, (tuple, list)):
                print("collection")
                l = tuple(args)
            elif isinstance(*args, types.GeneratorType):
                print("generator")
                l = (e for e in args[0])
            self.values = [None] * len(l)
            for i in enumerate(args):
                self[i[0]] = i[1]
        else:
            
        for i in enumerate(self.values):
            self[i[0]] = self.__complex(i[1])

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(*([a[0] + a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)]))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(*([a[0] - a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)]))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([a[0] * a[1] for a in zip_longest(self.values, other.values, fillvalue=0.0)])
        elif self._isnumeric(other):
            return Vector(*([a * other for a in self.values]))

    def __rmul__(self, other):
        if self._isnumeric(other):
            return Vector(*([a * other for a in self.values]))

    def __truediv__(self, other):
        if self._isnumeric(other):
            divided = [None] * len(self)
            for i in enumerate(self.values):
                if self._isreal(i[1]):
                    divided[i[0]] = float(i[1]) / other
                else:
                    divided[i[0]] = i[1] / other
            return Vector(*divided)

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.values == other.values

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.values != other.values

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        try:
            if self._iscomplex(value):
                self.__complex = complex
                self.values[key] = complex(value)
            elif self._isfloat(value):
                if self.__complex != complex:
                    self.__complex = float
                self.values[key] = float(value)
            elif self._isint(value):
                if self.__complex != complex and self.__complex != float:
                    self.__complex = int
                self.values[key] = int(value)
            else:
                raise ValueError(str(value) + " is not int, float or complex")
        except IndexError:
            raise IndexError("Vector assignment index out of range")

    def __str__(self):
        return "Vector of len=%s: %s" % (self.__len__(), self.values)

    def _isint(self, value):
        return self._istype(value, int)

    def _isfloat(self, value):
        return self._istype(value, float, [int])

    def _iscomplex(self, value):
        return self._istype(value, complex, [int, float])

    def _isnumeric(self, value):
        return self._isint(value) or self._iscomplex(value) or self._isfloat(value)

    def _isreal(self, value):
        return self._isint(value) or self._isfloat(value)

    def _istype(self, value, ch_type: type, other_types=()):
        try:
            for type in other_types:
                if isinstance(value, type):
                    return False
            num = ch_type(value)
            return True
        except ValueError:
            return False
        except TypeError:
            return False

vector1 = Vector(1, 2, 3, 4, 5j)
vector2 = Vector((6, 7, 8))
vector2 = Vector([6, 7, 8])
print(vector1)
print(vector2)