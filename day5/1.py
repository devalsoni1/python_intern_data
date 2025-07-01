# import pandas as pd
# a = [10,20,30,40]
# s = pd.Series(a)
# print(s)

# import pandas as pd 
# ds = {
#     "num":[10,20,30,40],
#     "alpha":['A','B','C','D']
# }

# df = pd.DataFrame(ds)

# print(df)
# print(type(df))

# import pandas as pd


# print(pd.__version__)

# pd.Series(a,index=['a','b','c','d')
          
# import pandas as pd
# qm= {"days":11,"day2":22,"day3":33,"day4":55}
# s= pd.Series(qm,index=['days','day2'])
# print(s)
          
# import pandas as pd
# a=[11,22,3,5]

# d=pd.Series(a)
# print(d)
# print(ps.tolist

# import pandas as pd
# data ={
#     "name":['dev','sani','shivam'],
    
#     "num":[23,24,25]
# }

# df = pd.DataFrame(data)

# print(df)

# import pandas as pd
# df = pd.DataFrame([['a','b'],['c','d']])

# print(df)

# result = df.iloc[1:3:]
# print(result)

# import pandas as pd
# data = {'A':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
# print(data)
# df = pd.DataFrame(data)
# col_A= df.loc[:,'A']
# print(col_A)
# col_AB= df.loc[:,'A':'b']
# print(col_AB)
import pandas as pd
# df = pd.DataFrame([['a','b'],['c','d'],['e','f']],columns=['col1','col2'])

# print(df)

# df.iloc[1:3,1]=['x','y']

# print(df)

df = pd.DataFrame({'A':[1,2,3,4,5],'B':[4,0,6,7,8]},index=['r1','r2','r3','r4','r5'])

print(df)
result = df.drop(df.index[2:4])
print(result)