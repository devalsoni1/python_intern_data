import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. Replace NaN with 0 and interchange 3 rows and 3 columns
arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

# Replace NaN with 0
arr_no_nan = np.nan_to_num(arr, nan=0)
print("Array with NaN replaced:\n", arr_no_nan)

# To interchange rows and columns, we can transpose
# It will result in 4x2 since the original array is 2x4
transposed = arr_no_nan.T
print("Transposed array:\n", transposed)

# ------------------------------
# 2. Move axes of 3D array to new positions
arr_3d = np.arange(24).reshape(2, 3, 4)
print("\nOriginal 3D shape:", arr_3d.shape)

# Swap axis 0 and axis 2
moved_axes = np.moveaxis(arr_3d, 0, 2)
print("Shape after moving axes:", moved_axes.shape)

# ------------------------------
# 3. Replace NaN values with average of columns
arr2 = np.array([[1, np.nan, 3],
                 [4, 5, np.nan],
                 [np.nan, 8, 9]])

print("\nOriginal array:\n", arr2)

# Compute column means ignoring nan
col_means = np.nanmean(arr2, axis=0)
inds = np.where(np.isnan(arr2))
arr2[inds] = np.take(col_means, inds[1])
print("Array after replacing NaN with column averages:\n", arr2)

# ------------------------------
# 4. Replace negative values with zero
arr_neg = np.array([2, -4, 5, -7, 8])
arr_replaced = np.where(arr_neg < 0, 0, arr_neg)
print("\nReplace negatives with zero:\n", arr_replaced)

# ------------------------------
# 5 & 6. Study the following program and import numpy
import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

# Find average
avg = (arr1 + arr2) / 2
print("\nAverage of arr1 and arr2:\n", avg)

# ------------------------------
# 7. Calculate average, mean, median, mode of two 2d arrays
from scipy import stats

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

# Combine arrays
combined = np.concatenate((a, b), axis=0)
print("\nCombined array:\n", combined)

# Average (element-wise mean of two arrays)
avg_arr = (a + b) / 2
print("Element-wise average:\n", avg_arr)

# Mean
print("Mean:", np.mean(combined))

# Median
print("Median:", np.median(combined))

# Mode
mode_result = stats.mode(combined, axis=None, keepdims=True)
print("Mode:", mode_result.mode[0])

# ------------------------------
# 8. Solve system of equations using linalg

# Equations:
# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])

# Solve using linalg.solve
solution = np.linalg.solve(A, B)
print("\nSolution using linalg.solve:\n", solution)

# Solve using inverse
A_inv = np.linalg.inv(A)
x_vals = A_inv @ B
print("Solution using inverse matrix:\n", x_vals)

# ------------------------------
# 9. Customizing Matplotlib: plot semester result
semesters = ['Sem 1', 'Sem 2']
marks = [75, 85]

plt.figure(figsize=(6,4))
plt.bar(semesters, marks, color=['blue', 'green'])
plt.title("Semester-wise Result Comparison")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.show()
