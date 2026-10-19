import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a = np.array(a)
	b = np.array(b)
	dim_1 = np.array(a.shape)
	dim_2 = np.array(b.shape)
	if dim_1[1] == dim_2[0]:
		return np.matmul(a, b)
	else:
		return -1
	pass 