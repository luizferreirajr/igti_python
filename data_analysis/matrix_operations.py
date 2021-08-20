import numpy as np
"""
Matrix operation
[[A B]                   [[A * G + B * H]
 [C D]  X [[G]     ==     [C * G + D * H]
 [E F]]    [H]]           [E * G + F * H]

"""

x = np.array([[1, 2], [2, 3], [3, 4]])
y = np.array([[5], [10]])

print(x)
print()
print(y)
print()
print(np.dot(x, y))

