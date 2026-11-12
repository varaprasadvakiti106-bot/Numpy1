import numpy as np

#NumPy Array Indexing
arr = np.array([1,2,3,4])
print(arr[1])
print(arr[3])
print(arr[2] + arr[3])

#Access 2-D Arrays
d2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d2)
print("Size of the array: ",d2.size)
print("Shape of the array: ",d2.shape)
print("Dimension of the array: ",d2.ndim)
print("Type of the array: ",d2.dtype)

d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

print(d[0][0])
print(d[1][1])
print(d[2][2])

#or use single braket with comma(,)
print(d[1,2])

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))

#NumPy Array Reshaping
#Reshaping means changing the shape of an array.
#The shape of an array is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension.

a = np.arange(8)
print("Original array:", a)

b = a.reshape(2,4)
print("Reshaped array:", b)

c = a.reshape(-1,2)
print("Reshaped array:", c)

d = a.reshape(2,2,2)
print("Reshaped array:", d)

Arr = np.array([[1,2,3],[4,5,6]])
flat = Arr.flatten()
print("Original array:", Arr)
print("Flattened array:", flat)

flat2 = Arr.flatten()
flat2[0] = 10
print("Modified flattened array:", flat2)

#✅ ravel() This function is also used to flatten arrays, but it returns a view when possible.
#So, changes made to the raveled array may affect the original.

X = np.array([[1,2,3],[4,5,6]])
R = X.ravel()
print("Original array:", X)
print("Raveled array:", R)
R2 = X.ravel()
R2[0] = 10
print("Original array after modifying raveled array:", X)
print("Modified raveled array:", R2)

#✅ np.newaxis
#This is not a function but a method to add a new axis (dimension) to your array.
#Used to convert row vectors to column vectors and vice versa.

a = np.array([[1,2,3,4],[5,6,7,8]])

row = a[np.newaxis, :]
col = a[:, np.newaxis]

print("ROw: ",row)
print("Row vector shape: ",row.shape)
print("Column: ",col)
print("Column vector shape: ", col.shape)

b = np.array([1,2,3,4])

row=b[np.newaxis, :]
col=b[:, np.newaxis]

print("B Row: ",row)
print("B Row vector shape: ",row.shape)
print("B col: ",col)
print("B col vector shape: ",col.shape)

#✅ np.resize()
#Resizes array even if shape doesn’t match. It repeats data if needed.
#Not often used in ML because it alters data.
#📌 Syntax:
#np.resize(array, new_shape)

a = np.array([1,2,3,4,5])
b = np.resize(a,(2,4))

print("Resize: ",b)

#✅ np.random.rand() 
rand = np.random.rand(5)
print("random numbers: ",rand)
rand_floats = np.random.randint(3,4,size=(2,3))
print("Random 2D decimal numbers: ",rand_floats)
a = np.random.randint(1,6,size=(10)) #✅ np.random.randint()
print("Random 1D integer numbers: ",a)

#✅ np.random.randn() Generates numbers from a normal distribution (can be negative or positive)
Rand_values = np.random.randn(5)
print("Random 1D decimal numbers: ",Rand_values)
Rand_2D = np.random.randn(3,2)
print("Random 2D decimal numbers: ",Rand_2D)

#np.random.seed() Fixes the random values so results are the same every time
np.random.seed(42)
print("First time: ",np.random.rand(3))
print("Second time: ",np.random.rand(3))

np.random.seed(2)
print(np.random.rand(3))

#np.random.choice()  Selects random items from a list or array
choices = np.random.choice([1,2,3,4,5], size= 6)
print("Random choices (can repeat): ",choices)

unique_choices = np.random.choice([1,2,3,4,5], size= 5, replace=False)
print("Random unique choices (no repeat): ",unique_choices)

# NumPy Boolean Indexing & Filtering
#✅ 1. Basic Boolean Indexing (Select elements from an array based on a condition)
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Original array: ",arr)
# Select elements greater than 5
selected = arr[arr > 5]
print("Values > 5: ",selected)
#see the boolean mask
mask = arr > 5
print("Boolean mask: ",mask)
boolean = arr > 4
print("Boolean mask for values > 4: ",boolean)

#✅ 2. Multiple Conditions ( Combine conditions using & (AND), | (OR), ~ (NOT))
between = arr[(arr > 4) & (arr < 8)] #(AND condition)
print("Values between 4 and 8: ",between)
outside = arr[(arr < 4) | (arr > 8)] #(OR condition)
print("Values outside 4 and 8: ",outside)
not_values = arr[~(arr > 5)] #(NOT condition)
print("Values not > 5: ",not_values)

#✅ 3. np.where() Function ( Find indices where condition is True, or replace values)
indices = np.where(arr > 5)
print("Indices where > 5: ",indices[0])
print("Values at those indices: ",arr[indices])
# Replace values greater than 5 with 0
replaced = np.where(arr > 5, 11, arr)
print("Replaced values > 5 with 11: ",replaced)

#✅ 4. Filtering 2D Arrays ( Apply boolean indexing to multi-dimensional arrays)
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original matrix: ",matrix) 
# Select elements greater than 5
high_values = matrix[matrix > 5]
print("Values > 5 in matrix: ",high_values)
# Select rows where the first column is > 4
row_filter = matrix[matrix[:, 1]> 4]
print("Rows where first column > 4: ",row_filter)

#✅ 5. Real-World Data Cleaning (Remove outliers and invalid data)
data = np.array([10, 20, 30, 1000, 40, 50, -999, 60])
print("Original data: ",data)
# Remove outliers (values > 100 or < 0)
cleaned_data = data[(data <= 100) & (data >=0)]
print("Cleaned data (removed outliers): ",cleaned_data)
print(f"Removed {len(data) - len(cleaned_data)} invalid entries readings")
# Calculate statistics on clean data
print("Mean of cleaned data: " ,np.mean(cleaned_data))


#NumPy Join, Split & Sort Operations
#✅ 1. Array Joining
#Joining means combining multiple arrays into one.
# np.concatenate()
A = np.array([1,2,3])
B = np.array([4,5,6])
print("Concatenated array: ",np.concatenate((A,B)))
C = np.array([[1,2],[3,4]]) #axis=0 means join along rows
D = np.array([[5,6],[7,8]])
print("2D array : ",np.concatenate((C,D)))

#np.stack() Stacks arrays along a new axis (adds one dimension).
a = np.array([1,2,3])
b = np.array([4,5,6])
stacked = np.stack((a,b))
print("Stacked array: ",stacked)
print("shape: ",stacked.shape)

a1 = np.array([[1,2,3]])
b1 = np.array([[4,5,6]])
result = np.stack((a1,b1))
print("Stacked 2D array: ",result)
print("shape: ",result.shape)

# np.hstack() Stacks arrays horizontally (along columns).
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Hstack array: ",np.hstack((a,b)))

#np.vstack() Stacks arrays vertically (along rows).
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Vstack array: ",np.vstack((a,b)))

#✅ 2. Array Splitting
# Splitting means breaking one array into multiple smaller arrays.
#np.split()
arr = np.array([[1,2,3,4],
                [5,6,7,8]])
result = np.split(arr, 2, axis=0)
print("split result: ",result)

#np.hsplit() splits an array horizontally (column-wise).
a = np.array([[1,2,3,4],
              [5,6,7,8]])
print("hsplit result: ",np.hsplit(a, 2))

#np.vsplit() splits an array vertically (row-wise).
print("vsplit result: ",np.vsplit(a,2))

#✅ 3. Sorting Arrays
#Sorting means arranging elements in ascending order.
arr = np.array([4,33,23,1,10])
print("sorted array: ",np.sort(arr))
print("sorted indices: ",np.argsort(arr))

#✅ Sorting 2D Arrays
matrix = np.array([[3,2,1],
                   [6,5,4]])
print("row-wise sorted: ",np.sort(matrix, axis=1))
print("column-wise sorted: ",np.sort(matrix, axis=0))