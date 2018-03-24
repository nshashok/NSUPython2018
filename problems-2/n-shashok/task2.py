def zip_longest(*lists):
    def generate(l):
        for item in l:
            yield item
        while True:
            yield 0.0
    gg = [generate(l) for l in lists]
    return [tuple(next(g) for g in gg) for _ in range(max([len(l) for l in lists]))]


class Vector(object):
    def __init__(self, *args):
        self.values = [float(a) for a in args]

    def __add__(self, other):
        if isinstance(other, Vector):
            print(zip_longest(self.values, other.values))
            return Vector(*([a[0] + a[1] for a in zip_longest(self.values, other.values)]))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(*([a[0] - a[1] for a in zip_longest(self.values, other.values)]))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([a[0] * a[1] for a in zip_longest(self.values, other.values)])
        elif isinstance(other, type(1)) or isinstance(other, type(1.0)):
            return Vector(*([a * other for a in self.values]))

    def __rmul__(self, other):
        if isinstance(other, type(1)) or isinstance(other, type(1.0)):
            return Vector(*([a * other for a in self.values]))

    def __truediv__(self, other):
        if isinstance(other, type(1)) or isinstance(other, type(1.0)):
            divided = tuple(a / other for a in self.values)
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
            self.values[key] = float(value)
        except IndexError:
            raise IndexError("Vector assignment index out of range")

    def __str__(self):
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
