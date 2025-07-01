import pandas as pd

# date_strings = pd.Series(['2024-01-10', '2024-02-15', '2024-03-20'])
# timeseries = pd.to_datetime(date_strings)
# print(timeseries)

# DataFrame 1
# df1 = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })

# # DataFrame 2
# df2 = pd.DataFrame({
#     'ID': [2, 3, 4],
#     'Age': [30, 35, 40]
# })

# # print("df1:")
# # print(df1)
# # print("\ndf2:")
# # print(df2)

# inner = pd.merge(df1, df2, on='ID', how='inner')
# print("\nInner Merge:")
# print(inner)

# left = pd.merge(df1, df2, on='ID', how='left')
# print("\nLeft Join:")
# print(left)

# right = pd.merge(df1, df2, on='ID', how='right')
# print("\nRight Join:")
# print(right)

# df1_index = df1.set_index('ID')
# df2_index = df2.set_index('ID')

# joined = df1_index.join(df2_index, how='right')
# print("\ndf.join() Right Join on Index:")
# print(joined)

# DataFrame A
# df_a = pd.DataFrame({
#     'ID': [1, 2],
#     'City': ['Delhi', 'Mumbai']
# })

# # DataFrame B
# df_b = pd.DataFrame({
#     'ID': [3, 4],
#     'City': ['Pune', 'Chennai']
# })

# # DataFrame C
# df_c = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Country': ['India', 'India', 'India', 'India']
# })

# concat_df = pd.concat([df_a, df_b])
# print("\nConcatenated DataFrame:")
# print(concat_df)

# merged = pd.merge(concat_df, df_c, on='ID')
# print("\nMerged DataFrame:")
# print(merged)

