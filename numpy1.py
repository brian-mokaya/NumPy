import numpy as np

# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)

# Perform operations
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Average of the array
print("Square Roots:", np.sqrt(my_array))

# Create a list of numbers from 10 to 50
numbers = list(range(10, 51))

# Create a numpy array from the list
numbers_array = np.array(numbers)

# Print the mean of the array
print("Mean of the array:", numbers_array.mean())

# Print the max of the array
print("Max of the array:", numbers_array.max())

# Print the min of the array
print("Min of the array:", numbers_array.min())

# Print the size of the array
print(numbers_array.size)