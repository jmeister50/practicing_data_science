import pandas as pd

filename = 'sitka_weather_07-2018_simple.csv'

# Open and read csv
csv = pd.read_csv(filename)

# Get list of all column names
column_names = csv.columns

# Print out each column name
for column_name in column_names:
	print(column_name)

# Find high values in the TMAX Column
highs = csv['TMAX']
print(highs)