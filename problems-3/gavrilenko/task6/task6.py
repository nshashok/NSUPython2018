import task4-5.py


class AlmostVector3D(task4-5.AlmostVector):
    def __init__(self, *args):
        super().__init__(*args) 
        if self._length != 3:
            raise TypeError
            
    def cross_product(self, other):
        if not isinstance(other, AlmostVector3D):
            raise TypeError
        return AlmostVector3D((self[1] * other[2] - self[2] * other[1], self[2] * other[0] - self[0] * self[2], self[0] * other[1] - self[1] * other[0]))