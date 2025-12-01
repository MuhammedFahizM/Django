import numpy as np


# Creating an array from a list

# arr = np.array([1,2,3,4,5])
# print(arr)



# Checking array Properties :-
# print("Array type : ",type(arr))
# print("Array Shape : ",arr.shape)
# print("Array Size : ",arr.size)
# print("Array Data Type : ",arr.dtype)



# Multidimensional Array:-
# matrix = np.array([[1,2,3],[4,5,6]])
# print(matrix)



               # Numpy Opertaions:-

  # Mathematical Operations:-

# arr = np.array([10,20,30])
# print("Addition : ",arr + 5)
# print("Multipication : ", arr * 2)
# print("Exponentiation : ",arr ** 2)


# Array Indexing and Slicing

# arr = np.array([10,20,30,40,50])
# print(arr[1:4])


# Special Arrays :-
zeros = np.zeros((2,3))  # 2x3 matrix of zeros,creates an array filled with 0s
ones = np.ones((3,3))  # 3x3 matrix of ones,creates an array filled with 1s
random_values = np.random.rand(2,2)  # 2x2 matrix of random values [generates]
# print(zeros)
# print(ones)
print(random_values)