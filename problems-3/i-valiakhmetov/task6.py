#!/bin/python

import types
import collections

class Vector(object):
	"""My Vector class for n-dimensional math vector"""

	def setVector(self, v):
		r"""Initializes a vector with an array_like values,
		generators, collections.

		Parameters
		----------
		v: array_like, generators, collections
			Array_like -- lists, tuples, etc.
		"""
		m = 0
		mtype = int
		if (isinstance(v, types.GeneratorType) or
			isinstance(v, collections.Collection)):
			self.__vector = list(v)
			for num in self.__vector:
				if (isinstance(num, int)):
					pass
				elif (isinstance(num, float) and m < 1):
					mtype = float
					m = 1
				elif (isinstance(num, complex)):
					mtype = complex
					m = 2
				else:
					raise TypeError("Invalid type")
			self.__vector = list(map(mtype, self.__vector))
			self._dim = len(self.__vector)
		else:
			raise TypeError("Invalid type")
			
	def __init__(self, v):
		self.setVector(v)

	def magnitude(self):
		r"""Vector magnitude
		
		Returns
		-------
		type
			float or int
		"""
		return sum(map((lambda x: x**2), self.__vector)) ** .5
		
	def getDimension(self):
		"""Vector dimension, number of coordinates
		-------
		type
			int
		"""
		return self._dim

	def __add__(self, b):
		"""Sums two vectors together
		Parameters
		----------
		b : Vector

		Returns
		-------
		type
			Vector

		Raises
		------
		ValueError
			In case of different vector dimensions
		"""
		if (self._dim == b._dim):
			return Vector([x + y for x, y in zip(self.__vector, b.__vector)])
		else:
			raise ValueError("Invalid dimension")

	def __sub__(self, b):
		"""Substract two vectors
		Parameters
		----------
		b : Vector

		Returns
		-------
		type
			Vector

		Raises
		------
		ValueError
			In case of different vector dimensions
		"""
		if (self._dim == b._dim):
			return Vector([x - y for x, y in zip(self.__vector, b.__vector)])
		else:
			raise ValueError("Invalid dimension")

	def __mul__(self, b):
		"""Dot product in case if b is a vector; vector*b(where b = const) if b is a const
		Parameters
		----------
		b : Vector
		b : Int

		Returns
		-------
		type
			Vector

		Raises
		------
		ValueError
			In case of different vector dimensions
		TypeError
			In case of unknown type
		"""
		if (isinstance(b, (int, float, complex))):
				return Vector(list(map((lambda x: x*b), self.__vector))) # vector*const
		elif (isinstance(b, Vector)):
			if (self._dim == b._dim):
				return sum([x*y for x, y in zip(self.__vector, b.__vector)]) # dot product
			else:
				raise ValueError("Different dimensions")
		else:
			raise TypeError("Invalid type")

	def __eq__(self, b):
		"""Checks for equality two vectors
		Parameters
		----------
		b : Vector

		Returns
		-------
		type
			True, if two vectors equals each other
			False, otherwise
		"""
		if (self._dim == b._dim):
			for x, y in zip(self.__vector, b.__vector):
				if (x != y):
					return False
			return True
		else:
			return False

	def __getitem__(self, i):
		"""Returns i coordinate of a vector
		Parameters
		----------
		i : int

		Returns
		-------
		type
			int, float
		"""
		return self.__vector[i]

	def __str__(self):
		"""Returns string representation of a vector

		Returns
		-------
		type
			string
		"""
		return str(self.__vector)

class Vector3D(Vector):
	"""My Vector class for 3-dimensional math vector"""
	def __init__(self, v):
		super().__init__(v)
		if (self._dim != 3):
			raise ValueError("Invalid dimension")

	def dotprod(self, b):
		if (self._dim == b._dim):
			return sum([x*y for x, y in zip(self.__vector, b.__vector)])
		else:
			raise ValueError("Invalid dimension")

if __name__ == "__main__":
	a = Vector([1,2,complex(1)])
	b = Vector((1,2,3))
	c = Vector((i for i in (1,2,3)))
	m = Vector([complex(1,2), complex(2,3), complex(3,5)])
	g = Vector3D((1,2,3))
	print(g*b)
	print(a*b)
	print(b*c)
	print(m.magnitude())