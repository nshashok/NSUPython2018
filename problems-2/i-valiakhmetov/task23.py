#!/bin/python

class Vector(object):
	"""My Vector class for n-dimensional math vector"""

	def __init__(self, v):
		self.__vector = v
		self.__dim = len(v)

	def setVector(self, v):
		r"""Initializes a vector with an array_like value

		Parameters
		----------
		v: array_like
			Array_like -- lists, tuples, etc.
		"""
		self.__vector = v
		self.__dim = len(v)

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
		if (self.__dim == b.__dim):
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
		if (isinstance(b, int)):
				return Vector(list(map((lambda x: x*b), self.__vector))) # vector*const
		elif (isinstance(b, Vector)):
			if (self.__dim == b.__dim):
				return sum([x*y for x, y in zip(self.__vector, b.__vector)]) # dot product
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
		if (self.__dim == b.__dim):
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
