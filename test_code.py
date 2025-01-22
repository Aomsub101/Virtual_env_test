import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Perform basic arithmetic
arr_squared = arr ** 2  # Squaring each element
arr_sum = arr.sum()     # Sum of all elements
arr_mean = arr.mean()   # Mean of the array

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Matrix operations
matrix_transpose = matrix.T  # Transpose of the matrix
matrix_product = np.dot(matrix, matrix.T)  # Matrix multiplication

# Output
print("Original Array:", arr)
print("Squared Array:", arr_squared)
print("Sum of Array:", arr_sum)
print("Mean of Array:", arr_mean)
print("\nOriginal Matrix:\n", matrix)
print("\nTransposed Matrix:\n", matrix_transpose)
print("\nMatrix Product:\n", matrix_product)
