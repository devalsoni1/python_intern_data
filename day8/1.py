import pandas as pd
import numpy as np

# df = np.array([[1,2,3,4,5],[2,3,4,5,6]],dtype='S')

# print(df)

# print(df.shape)
# print(df.dtype)

# print(np.zeros((1,4)))   
# print("-------------")      # 3 rows, 4 columns array of zeros
# print(np.ones((2,3))) 
# print("-------------")         # 2 rows, 3 columns array of ones
# print(np.eye(3))      
# print("-------------")         # Identity matrix 3x3
# print(np.arange(10, 20, 2))
# print("-------------")    # [10 12 14 16 18]
# print(np.linspace(0,1,num = 2, endpoint = False,retstep=True))      # 5 evenly spaced values between 0 and 1


# arr = np.arange(10,20,3)

# print("array using arange();",arr)

# arr2 = np.random.rand(2,3)
# print("arrar  2d is",arr2)

# arr3 = np.random.rand(2,3,4)
# print("Array 3 is",arr3)

# a = np.empty 

# empar = np.empty(2,3)

# print(empar)

# arr1 = np.array([1,2,3,4])

# print(arr1[0])

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[1,8,9,9],[9,0,0,1]]])

print(arr)

print(arr[-1,-2,0])