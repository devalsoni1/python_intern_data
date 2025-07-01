import pandas as pd
import numpy as np
# df = pd.DataFrame({'one':[10,20,30,40,50,6000],'two':[1000,20,30,40,50,2000]})

# print(df.replace({1000:10,2000:60,6000:53.9044}))
# print(df)

# data = {'Category':['A','B','C','D','C','A'],
#         'Value':[10,20,15,26,34,64]}


# df = pd.DataFrame(data)
# group_data = df.groupby('Category')['Value'].mean()

# print(group_data)

# data = {'Category':['A','B','C','D','C','A'],
#         'Value':[10,20,15,26,34,64],
#         'Subcate':['x','y','q','g','y','o']}


# df = pd.DataFrame(data)
# print(df)
# group_data = df.groupby(['Category','Subcate'])['Value'].mean()
# print(group_data)

# data = {'Name':['BAB','CAC','ABA'],'Age':[93,73,16]}
# df = pd.DataFrame(data)
# # result = df.sort_values(by='Name')
# # result = df.sort_values(by='Age')
# result = df.sort_values(['Name','Age'],ascending=[True,False])
# print(result)
# dATA = 

# print(pd.date_range('6/1/2024',periods=5))

# df = pd.read_csv('industry.csv')

# df = pd.read_json('ff.json')
# print(df)

# df = pd.read_csv('data.csv')
# x = df["Index"].mean()

# df.fellna({})

