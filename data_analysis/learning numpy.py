import numpy as np


"""
How to search for help about a lib
help(np.array)
"""


"""
# Creating of an array 1D: [1, 2 ,3]
x = np.array([1, 2 , 3])
print('x: ', x.shape)
"""


"""
# Creating of an array 2D: nested lists
x = np.array([[1, 2], [3, 4]])
print('x:\n', x)
print('shape: ', x.shape)
"""


"""
# Array with zeros as values
dim = (4, 4)  # lines, columns
x = np.zeros(dim)
print('x:\n', x)
print('shape: ', x.shape)
"""


"""
# Array with ones as values
dim = (4, 4)  # lines, columns
x = np.ones(dim)
print('x:\n', x)
print('shape: ', x.shape)
"""

"""
# Creation of values inside a range
# uniform values between 5 and 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print('x: ', x)
print('shape: ', x.shape)
"""


# Create a identity matrix
n = 4
x = np.eye(n)
print('x:\n', x)
print('shape: ', x.shape)


"""
# Create random values
# np.random.seed(10)
x = np.random.random(size=(2, 3))
print('x:\n', x)
print('shape: ', x.shape)
"""
