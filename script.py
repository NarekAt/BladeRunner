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


def transformer(vector1Str, vector2Str):


	vector1Str = vector1Str[1:-1]
	vector2Str = vector2Str[1:-1]

	vector1 = map(int, vector1Str.split(','))
	vector2 = map(int, vector2Str.split(','))

	return vector1, vector2


def BladeHelper():
	vector1Str = "{1,2,3,4}"
	vector2Str = "{5,6,7}"
	vector1, vector2 = transformer(vector1Str, vector2Str)

	if (len(vector1) != len(vector2)):
		raise InputError(None, "Wrong vector size")

	# addition
	print map(add, vector1, vector2)

	# mult with integer
	for i in range(0, len(vector1)):
		vector1[i] *= 5

	print vector1

	# dot product
	product = sum(map(mul, vector1, vector2))

	print product


BladeHelper()