import numpy as np
import random


# Element by element
u = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])

print(u * x)
print()


# Using broadcasting
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(9 * y)
print()


# Using 2d arrays
a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
b = np.array([[0, 1, 2]])

print(b + a)
print()


# Using only 1d arrays
c = np.array([[0], [10], [20], [30]])
d = np.array([[0, 1, 2]])

print(c + d)
