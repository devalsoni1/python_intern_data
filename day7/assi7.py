# import re

# email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# email = "hello@example.com"
# print(bool(re.match(email_pattern, email)))  # True

# mobile_pattern = r'^\d{10}$'

# number = "9876543210"
# print(bool(re.match(mobile_pattern, number)))  # True

# text = "Hello World, This Is Python."
# pattern = r'\b[A-Z][a-z]*\b'
# matches = re.findall(pattern, text)
# print(matches)  

# text = "Order 123 costs $45 and item 678 costs $90."
# numbers = re.findall(r'\d+', text)
# print(numbers)

# import pandas as pd

# # Create a datetime Series
# dates = pd.Series(['2024-01-10', '2024-03-15', '2024-07-01'])
# dates = pd.to_datetime(dates)

# print("Original Dates:")
# print(dates)

# # Extract year, month, day
# print("Year:")
# print(dates.dt.year)

# print("Month:")
# print(dates.dt.month)

# print("Day of week:")
# print(dates.dt.day_name())

# # Filter dates after March 1, 2024
# filtered = dates[dates > '2024-03-01']
# print("Dates after 2024-03-01:")
# print(filtered)

import pandas as pd

# Read CSV
df = pd.read_csv('')

# Show data
print("Original Data:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isna().sum())

# Fill missing Sales with 0
df['Sales'] = df['Sales'].fillna(0)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by Product and sum Sales
result = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales per Product:")
print(result)
