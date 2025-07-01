# d = {1: 'Program', 2: 'For', 3: {'A': 'Dictionary', 'B': 'In', 'C': 'Python'}}
# print(d[1])
# print(d[3]['A'])
# print(d[3]['C'])

# def my_func():
#     print("Hello daale")

# my_func()

k = int(input("enter a vlaue"))

def rec(k):
    if(k>0):
        k = k - 1
        print(k)

        rec(k)

    else:
        result = 0 
rec(k)