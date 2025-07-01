# import pandas as pd

# data = {'a': 10, 'b': 20, 'c': 30}
# series_from_dict = pd.Series(data)
# print(series_from_dict)
# print(series_from_dict['b'])
# #list
# data = [100, 200, 300]
# index = ['x', 'y', 'z']
# series_from_list = pd.Series(data, index=index)
# print(series_from_list)
# #acces list 
# print(series_from_list['y'])

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# }
# df = pd.DataFrame(data)
# print(df)

# data_list = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
# df_l = pd.DataFrame(data_list, columns=['ID', 'Name'])
# print(df_l)

# data_ll = [
#     ['Math', 90],
#     ['English', 85],
#     ['Science', 95]
# ]
# df_ll1 = pd.DataFrame(data_ll, columns=['Subject', 'Marks'])
# print(df_ll1)

# data_t = [
#     (1, 'Apple'),
#     (2, 'Banana'),
#     (3, 'Cherry')
# ]
# df_t = pd.DataFrame(data_t, columns=['ID', 'Fruit'])
# print(df_t)

# data_dd = [
#     {'Name': 'Tom', 'Age': 20},
#     {'Name': 'Jerry', 'Age': 22},
#     {'Name': 'Spike', 'Age': 25}
# ]
# df_dd = pd.DataFrame(data_dd)
# print(df_dd)

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Delhi']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 40)

# 1. Different ways to iterate over rows

# a) Using iterrows()
print("Using iterrows():")
for index, row in df.iterrows():
    print(row['Name'], row['Age'])

# b) Using itertuples()
print("\nUsing itertuples():")
for row in df.itertuples(index=False):
    print(row.Name, row.Age)

print("-" * 40)

# 2. Selecting rows based on condition
print("People whose Age > 28:")
condition_df = df[df['Age'] > 28]
print(condition_df)
print("-" * 40)

# 3. Select any row using iloc[]
print("Select 2nd row (index 1) using iloc:")
second_row = df.iloc[1]
print(second_row)
print("-" * 40)

# 4. Limited rows selection with given column
print("First 2 rows, only 'Name' column:")
limited_rows = df.loc[0:1, ['Name']]
print(limited_rows)
print("-" * 40)

# 5. Drop rows based on condition
print("Drop rows where City == 'Delhi':")
filtered_df = df[df['City'] != 'Delhi']
print(filtered_df)
print("-" * 40)

# 6. Insert row at given position
new_row = {'Name': 'Eve', 'Age': 22, 'City': 'Bangalore'}
# Insert at position 2
df1 = pd.concat([df.iloc[:2], pd.DataFrame([new_row]), df.iloc[2:]]).reset_index(drop=True)
print("After inserting new row at index 2:")
print(df1)
print("-" * 40)

# 7. Create a list from rows
print("Convert rows to list of dictionaries:")
rows_list = df1.to_dict(orient='records')
print(rows_list)
