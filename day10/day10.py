import numpy as np

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])


# # swap the row 0 to row 2 till colum 0
# # arr[[0, 2],:1] = arr[[2, 0],:1]

# # print(arr)

# # print("----------------------------------------")


# # start from index 1 and select column 0 ,2
# arr[1,[0, 2]] = arr[1,[2, 0]]

# print(arr)

# shape(block,row,colummn)

# arr = np.array([[[1,2,3],[4,5,6]],[[0,9,8],[7,6,5]]])

# print(arr)

# print("===========================")


# arr[[0,1],[0,1],:] = arr[[1,0],[1,0],:]

# print(arr)

# arr = np.array([1,2,np.nan,4,np.nan,5])

# res = np.nan_to_num(arr, nan=0.0, posinf=None, neginf=None, copy=False)


# emp = np.isnan(arr)

# print(arr)
# print(emp)
# print(res)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# arr2 = np.array([1,2,3])

# np.savez("data.npz",array1=arr,array2=arr2)

# res = np.load("data.npz")

# print("array1 ",res['array1'])
 
# with open('data.txt','w') as f:
#     f.write("1.0 2.0 3.0 \n4.0 5.0 6.0")

# res = np.loadtxt('data.txt')
# print(res)

# data  = np.array([[1,2,3],[4,5,6],[7,8,9]])

# np.savetxt("output.txt",data, delimiter=' ',fmt='%1.1f')

# res = np.loadtxt("output.txt")


# print(res)

# with open('data.csv','w') as f:
#     f.write("1.0,2.0,3.0,4.0\n5.0,6.0,7.0,8.0")

# data = np.genfromtxt('data.csv',delimiter=',')
# print(data)

# arr1 = np.array([[2, 3],
#               [3, 4]])

# arr2 = np.array([8, 11])

# arr1_inv = np.linalg.inv(arr1)

# res = np.dot(arr1_inv,arr2)
# print(res)

import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

y=np.tan (x)

# print(y)

plt.plot(x, y, label='sin(x)',color='red',linestyle='dotted')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.grid(True)
plt.show()