import numpy as np

# Random values
random_arr = np.random.rand(3, 3)
print("Random Array:\n", random_arr)

# 4x2 empty array (values uninitialized, may be garbage)
empty_arr = np.empty((4, 2))
print("\nEmpty 4x2 Array:\n", empty_arr)

# Full array with value 7
full_arr = np.full((4, 2), 7)
print("\nFull 4x2 Array with 7:\n", full_arr)

# 3x5 array of zeros
zeros_arr = np.zeros((3, 5))
print("\n3x5 Zeros Array:\n", zeros_arr)

# 4x3x2 array of ones
ones_arr = np.ones((4, 3, 2))
print("\n4x3x2 Ones Array:\n", ones_arr)

matrix = np.arange(2, 11).reshape(3, 3)
print("\n3x3 Matrix from 2 to 10:\n", matrix)

vector = np.zeros(10)
vector[5] = 11
print("\nNull Vector with 6th value = 11:\n", vector)

arr = np.array([10, 20, 30, 40, 50])
reversed_arr = arr[::-1]
print("\nReversed Array:\n", reversed_arr)

import numpy as np

# Original array
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

# Convert to float
float_arr = arr.astype(float)
print("Array converted to float type:", float_arr)
