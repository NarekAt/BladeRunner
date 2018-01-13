from operator import add
from operator import mul

class BladeError(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(BladeError):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def transformer(vectorStr):
	vectorStr = vectorStr[1:-1]

	vector = map(int, vectorStr.split(','))
	return vector

def BladeAdd(vector1Str, vector2Str):
	vector1 = transformer(vector1Str)
	vector2 = transformer(vector2Str)

	if (len(vector1) != len(vector2)):
		raise InputError(vector1Str + " + " + vector2Str, "Wrong vector size.")

	return map(add, vector1, vector2)

def BladeSMult(vectorStr, number):
	vector = transformer(vectorStr)
	for i in range(0, len(vector)):
		vector[i] *= number

	return vector

def BladeMult(vector1Str, vector2Str):
	vector1 = transformer(vector1Str)
	vector2 = transformer(vector2Str)

	if (len(vector1) != len(vector2)):
		raise InputError(vector1Str + " * " + vector2Str, "Wrong vector size.")

	return map(mul, vector1, vector2)

def BladeDotProduct(vector1Str, vector2Str):
	vector1 = transformer(vector1Str)
	vector2 = transformer(vector2Str)

	if (len(vector1) != len(vector2)):
		raise InputError(vector1Str + " . " + vector2Str, "Wrong vector size.")

	product = sum(map(mul, vector1, vector2))
	return product