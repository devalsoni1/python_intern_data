# import pandas as pd
# data = {
#     'A':[1,2,3],'B':[4,5,6]
# }

# df= pd.DataFrame(data)

# print(df**2)
# print("this is Poweer")
# print(df-1)
# print("this is aaddition withb 2")
# df[df['A'] != 0]
# print(df)

# import pandas as pd

# df1 = pd.DataFrame({'A':[1,2,3,4],'B':[4,5,6,7]})
# df2 = pd.DataFrame({'A':[1,2,3,4],'B':[7,8,9,7]}, index=[1,2,3,4])

# print(df1)
# print(df2)

# print("\n Addition of 2 dataframe\n", df1 + df2)
# print("\n substraction of 2 dataframe\n", df1 - df2)
# print("\n multiplication of 2 dataframe\n", df1 * df2)

# import pandas as pd
# one = pd.DatFrame({
#     'Name':['A1','A2','A3']
#     'subject':['']
# })

# import pandas as pd 
# df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5 , 6]})
# df2 = pd.DataFrame({'A': [7, 8, 9], 'B':[7 , 8 , 9]} , index=[0 , 1 , 2])

# res = left.merge(right , on='id')
# print(res)

# df3= pd.concat([df1 , df2] , axis=1)
# print(df3)
# print(df1)
# print(df2)

# print("addition\n" , df1+df2)
# print("division\n" ,df1/df2)
# print("expo\n" ,df1**df2)
# print("subtraction\n" ,df1-df2)
# print("floor value\n" , df1//df2)


# import pandas as pd
# right = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['K1','K2','K3','K4','K5'],
#     'Subject':['sub1','sub2','sub3','sub4','sub5'],
#     'Marks':[26,73,83,78,22]},
#     index=[1,2,3,4,5]
# )

# left = pd.DataFrame({
#     'id': [1, 2, 3, 4, 5],
#     'Name':['J1','J2','J3','J4','J5'],
#     'Subject':['SUB1','SUB2','SUB3','SUB4','SUB5'],
#     'Marks':[62,73,72,78,97]},
#     index=[1,2,3,4,5]
# )

# result = left.merge(right, on = 'id')
# print(result)

# result = left.merge(right, on = 'Marks')
# print(result)

# result = right.merge(left , on = 'Name')
# print(result)

# result = left.merge(right , on = ['id' ,'Marks'])
# print(result)
# print("-----------------------------------------------------------------")

# print(left.merge(right,on = 'Subject', how = 'left'))
# print("-----------------------------------------------------------------")

# print(left.merge(right,on = 'Subject', how = 'right'))
# print("-----------------------------------------------------------------")

# print(left.merge(right, how= 'outer', on='Subject'))
# print("-----------------------------------------------------------------")

# print(left.merge(right, how='cross',on='Subject'))
# print("-------------------------------------------------------")

# result = left.join(right, rsuffix="_right",lsuffix="_left")
# print(result)

# import pandas as pd

# df = pd.DataFrame({"Col1":range(12),"Col2":["A","A","A","B","B","B","C","C","C","D","D","D"],
#                    "data":pd.to_datetime(["2025-05-01","2025-05-02","2025-06-02"]*4)})

# print(df)
# res = df.pivot(index="data",columns="Col2",values="Col1")
# print(res)

import pandas as pd

data = {
    'coruse':['CS','CIVIL','MECH'],
    'year':[1,2,3],
    'Student':['Dev','Sani','shuv']
}


df = pd.DataFrame(data)
print("original DataFrame:")
print(df)

pivot_df = df.pivot_table(
    values='Student',
    index='coruse',
    columns='year',
    aggfunc='sum'
)
print(pivot_df)