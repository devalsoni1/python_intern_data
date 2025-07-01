import numpy as np

# arr = np.array([
#     [[1,2,3],[4,5,6]],
#     [[7,8,9],[0,0,0]]
# ])


# print(arr)

# print(arr.shape)

# x=np.zeros((1,2))

# print(x)

# arr = np.array([1,2,3,4,5,6,7,8])

# base = 1

# x = arr.copy()

# o = arr.view()

# arr[0] = 42

# print(arr)

# print(x)

# print(o)

# print(arr.reshape(2,4), base)

# arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])

# x = arr.shape

# print(x)

# arr = np.array([1,2,3,4,5,6], ndmin=2)

# print(arr)

# arr = np.array([[[1 2]
#   [3 4]
#   [5 6]]
# ,[[0 9]
#   [8 7]
#   [6 5]]])

# newar = arr.reshape(-1)

# print(newar)

# arr = np.array([1,2,3,4,5])
# for x in arr:
#     print(x)

# arr = np.array([[[1,2,3,4],[5,6,7,8],[9,0,1,0]],[[0,9,8,7],[6,5,4,3],[3,2,1,0]]])

# for row in arr:
#     print(row)
#     for x in row:
#         print(x)
#         for y in x:
#             print(y)
            # for i in y:
            #     print(i)

a = np.array([[1,2],[3,4]])

b = np.array([[1,2],[3,4]])

x = np.concatenate((a,b))

print(x)