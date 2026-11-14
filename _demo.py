import pandas as pd
# Exploring DataFrame Properties in Pandas
#Create a Sample DataFrame
data = {
    'Name': ['vara','siddhu','bannu'],
    'subject': ['maths','science','english'],
    'Marks': [75, 92, 89],
    'Passed': [False, True, True]
}

df = pd.DataFrame(data)
print(df)
print("shape",df.shape)
print("size",df.size)
print("Number of dimensions: ",df.ndim)
#Labels and Metadata
print("Index: ",df.index)
print("Columns: ",df.columns)
print("Axes: ",df.axes)
#Data Types & Internal Values
print("Data types: ",df.dtypes)
print("Internal values: ",df.values)
print("info: ",df.info())
print("describe: ",df.describe())
print("memory usage: ",df.memory_usage())
print("check for object type: ",df.select_dtypes(include='object'))
print("check for numeric type: ",df.select_dtypes(include='number'))
print("check for boolean : ",df.select_dtypes(include='bool'))

#Accessing Data in a DataFrame
print("Access single column: ",df['Name'])
print("Access multiple columns: ",df[['Name','Marks']])  
print(df)

# Access row by position using iloc
print(df.iloc[0:2])
# Access row by label using loc
print(df.loc[0:2])
# Access specific cell: 2nd row, 3rd column
print(df.iloc[1,2])
# Access specific cell by label
print(df.loc[0,'Passed'])
# Access multiple rows and columns
print(df.loc[0:2, ['Name', 'Marks']])

#Importing & Exploring Datasets in Pandas
df = pd.read_csv('C:\\Users\\Vakiti Teja\\Desktop\\Numpy\\sales_data.csv')
print(df)
print(df.head())
print(df.tail())
print(df.sample(n=5))

# Info: Rows, columns, dtypes, nulls
print(df.info())

## Describe: Summary statistics for numeric columns
print(df.describe())

# 🔸 Setting a Custom Index
# Set 'rating' column as index
df_indexed = df.set_index('rating')
print(df_indexed)

# Filtering Data in Pandas
#Filter Using Logical Conditions

df[df['rating'] > 4.0]
print(df[df['rating'] > 4.0])
print(df[df['rating'] < 3.0])

# Combining Multiple Conditions with & and |
print(df[(df['rating'] > 4.0) & (df['rating'] < 5.0)])

#Filtering Text Columns using .str
print(df[df['Name'].str.contains('vara')])