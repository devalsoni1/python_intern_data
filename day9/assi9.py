import numpy as np

# 1) Combining a one and a two-dimensional NumPy Array

arr1d = np.array([1, 2, 3])
arr2d = np.array([[4, 5, 6],
                  [7, 8, 9]])

print("--- 1) Combining Arrays ---")
print("Original 1D array:\n", arr1d)
print("Original 2D array:\n", arr2d)

arr1d_reshaped = arr1d.reshape(1, -1)
combined_vstack = np.vstack((arr1d_reshaped, arr2d))
print("\nCombined (vstack - 1D as new row):\n", combined_vstack)

new_column = np.array([[10], [11]])
combined_hstack = np.hstack((arr2d, new_column))
print("\nCombined (hstack - 1D-like as new column):\n", combined_hstack)

combined_concatenate_row = np.concatenate((arr1d_reshaped, arr2d), axis=0)
print("\nCombined (concatenate axis=0 - 1D as new row):\n", combined_concatenate_row)

arr_to_add_column = np.array([[10], [11]])
combined_concatenate_col = np.concatenate((arr2d, arr_to_add_column), axis=1)
print("\nCombined (concatenate axis=1 - 1D-like as new column):\n", combined_concatenate_col)
print("-" * 40)


# 2) Flatten a 2d numpy array into 1d array

arr2d_flat = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

print("--- 2) Flatten Array ---")
print("Original 2D array for flattening:\n", arr2d_flat)

flat_array_flatten = arr2d_flat.flatten()
print("\nFlattened array (using .flatten()):", flat_array_flatten)

flat_array_reshape = arr2d_flat.reshape(-1)
print("Flattened array (using .reshape(-1)):", flat_array_reshape)

flat_array_ravel = arr2d_flat.ravel()
print("Flattened array (using .ravel()):", flat_array_ravel)
print("-" * 40)


# 3) Reverse a numpy array

arr1d_rev = np.array([10, 20, 30, 40, 50])
print("--- 3) Reverse Array ---")
print("Original 1D array for reversing:", arr1d_rev)

reversed_arr1d = arr1d_rev[::-1]
print("Reversed 1D array:", reversed_arr1d)

arr2d_rev = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("\nOriginal 2D array for reversing:\n", arr2d_rev)

reversed_rows = arr2d_rev[::-1, :]
print("Reversed rows:\n", reversed_rows)

reversed_cols = arr2d_rev[:, ::-1]
print("Reversed columns:\n", reversed_cols)

reversed_both = arr2d_rev[::-1, ::-1]
print("Reversed both rows and columns:\n", reversed_both)
print("-" * 40)


# 4) Practice operations like

# Get the maximum value from given array

arr_max = np.array([[10, 2, 8],
                    [4, 25, 6],
                    [7, 12, 9]])

print("--- 4) Max/Min/Shape/Select/Sum/Arithmetic Operations ---")
print("\nArray for Max/Min operations:\n", arr_max)

max_value = np.max(arr_max)
print("Maximum value in the array:", max_value)

max_per_column = np.max(arr_max, axis=0)
print("Maximum value per column (axis=0):", max_per_column)

max_per_row = np.max(arr_max, axis=1)
print("Maximum value per row (axis=1):", max_per_row)


# Get the minimum value from given array

arr_min = np.array([[10, 2, 8],
                    [4, 25, 6],
                    [7, 12, 9]]) # Same array as max, but could be different

min_value = np.min(arr_min)
print("\nMinimum value in the array:", min_value)

min_per_column = np.min(arr_min, axis=0)
print("Minimum value per column (axis=0):", min_per_column)

min_per_row = np.min(arr_min, axis=1)
print("Minimum value per row (axis=1):", min_per_row)


# Find the number of rows and columns of a given array using NumPy

arr_shape = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]])

print("\nArray for shape determination:\n", arr_shape)
rows, cols = arr_shape.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {cols}")

arr1d_shape = np.array([1, 2, 3, 4, 5])
print("\n1D Array for shape determination:", arr1d_shape)
shape_1d = arr1d_shape.shape
print("Shape of 1D array:", shape_1d)


# Select the elements from a given array (each element and specific element)

arr_select = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])

print("\nArray for element selection:\n", arr_select)

element_at_0_0 = arr_select[0, 0]
print("Element at (0, 0):", element_at_0_0)

element_at_1_2 = arr_select[1, 2]
print("Element at (1, 2):", element_at_1_2)

first_row = arr_select[0, :]
print("First row:", first_row)

second_column = arr_select[:, 1]
print("Second column:", second_column)

sub_array = arr_select[0:2, 1:3]
print("Sub-array (rows 0-1, cols 1-2):\n", sub_array)

diagonal_elements = arr_select[[0, 1, 2], [0, 1, 2]]
print("Diagonal elements:", diagonal_elements)

specific_elements = arr_select[[0, 2], [1, 0]]
print("Specific elements at (0,1) and (2,0):", specific_elements)

elements_greater_than_50 = arr_select[arr_select > 50]
print("Elements greater than 50 (boolean indexing):", elements_greater_than_50)


# Find the sum of values in a 2D array using for loop

arr2d_sum_loop = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

print("\nArray for sum operation:\n", arr2d_sum_loop)
total_sum = 0
for row in arr2d_sum_loop:
    for element in row:
        total_sum += element
print("Sum using for loop:", total_sum)

numpy_sum = np.sum(arr2d_sum_loop)
print("Sum using np.sum():", numpy_sum)

sum_rows = np.sum(arr2d_sum_loop, axis=1)
print("Sum of each row (axis=1):", sum_rows)

sum_cols = np.sum(arr2d_sum_loop, axis=0)
print("Sum of each column (axis=0):", sum_cols)


# Adding, Subtracting, multiplying, dividing arrays in Numpy

arr1_ops = np.array([[1, 2, 3],
                     [4, 5, 6]])

arr2_ops = np.array([[7, 8, 9],
                     [10, 11, 12]])

print("\nArrays for arithmetic operations:")
print("Array 1:\n", arr1_ops)
print("Array 2:\n", arr2_ops)

addition_result = arr1_ops + arr2_ops
print("\nAddition (arr1 + arr2):\n", addition_result)

subtraction_result = arr1_ops - arr2_ops
print("Subtraction (arr1 - arr2):\n", subtraction_result)

multiplication_result = arr1_ops * arr2_ops
print("Element-wise Multiplication (arr1 * arr2):\n", multiplication_result)

division_result = arr1_ops / arr2_ops
print("Division (arr1 / arr2):\n", division_result)

arr_scalar_add = arr1_ops + 10
print("Array 1 + 10 (scalar addition):\n", arr_scalar_add)

arr_scalar_mult = arr1_ops * 2
print("Array 1 * 2 (scalar multiplication):\n", arr_scalar_mult)
print("-" * 40)