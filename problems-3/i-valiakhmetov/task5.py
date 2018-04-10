#!/bin/python3

import types
import collections

class Vector(object):
	"""My Vector class for n-dimensional math vector"""

	def __is_int(self, num):
		try:
			int(num)
			return True
		except ValueError:
			return False

	def __is_float(self, num):
		try:
			float(num)
			return True
		except ValueError:
			return False

	def __is_complex(self, num):
		try:
			complex(num)
			return True
		except ValueError:
			return False

	def __setVector(self, v):
		m = 0
		mtype = int
		if (isinstance(v, types.GeneratorType) or
			isinstance(v, collections.Collection)):
			self._vector = list(v)
			for num in self._vector:
				if (isinstance(num, str)):
					if self.__is_int(num):
						num = int(num)
					elif self.__is_float(num):
						num = float(num)
					elif self.__is_complex(num):
						num = complex(num)
					else:
						raise TypeError("Invalid type")

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
			self._vector = list(map(mtype, self._vector))
			self._dim = len(self._vector)
		else:
			raise TypeError("Invalid type")
			
	def __init__(self, v):
		r"""Initializes a vector with an array_like values,
		generators, collections.
		Parameters
		----------
		v: array_like, generators, collections
			Array_like -- lists, tuples, etc.
		"""
		self.__setVector(v)

	def magnitude(self):
		r"""Vector magnitude
		
		Returns
		-------
		type
			float or int
		"""
		return sum(map((lambda x: x**2), self._vector)) ** .5
		
	def getDimension(self):
		"""Vector dimension, number of coordinates
		-------
		type
			int
		"""
		return self.__dim

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
		if (self.__dim == b.__dim):
			return Vector([x + y for x, y in zip(self._vector, b._vector)])
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
		if (self.__dim == b.__dim):
			return Vector([x - y for x, y in zip(self._vector, b._vector)])
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
				return Vector(list(map((lambda x: x*b), self._vector))) # vector*const
		elif (isinstance(b, Vector)):
			if (self._dim == b._dim):
				return sum([x*y for x, y in zip(self._vector, b._vector)]) # dot product
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
			for x, y in zip(self._vector, b._vector):
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
		return self._vector[i]

	def __str__(self):
		"""Returns string representation of a vector

		Returns
		-------
		type
			string
		"""
		return str(self._vector)

if __name__ == "__main__":
	a = Vector([1,2,complex(1)])
	b = Vector((1,2,3))
	c = Vector((i for i in (1,2,3)))
	m = Vector([complex(1,2), complex(2,3), complex(3,5)])
	print(a*b)
	print(b*c)
	print(m.magnitude())