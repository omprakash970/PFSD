#write a basic Numpy Program 
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])

print("1D Array:", array_1d)
# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
      
print("2D Array:\n", array_2d)
# Perform basic operations
print("Array Addition:\n", array_2d + 10)

print("Array Multiplication:\n", array_2d * 2)
# Calculate mean and standard deviation
print("Mean of 2D Array:", np.mean(array_2d))

print("Standard Deviation of 2D Array:", np.std(array_2d))

