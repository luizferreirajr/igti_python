import numpy as np
import pandas as pd

# == CÓDIGO 1 == #
# Z = np.zeros((4, ))
# print('Z: ', Z)

# == CÓDIGO 2 == #
# Z = np.zeros((4, ))
# Z[1] = 1.
# print('Z: ', Z)

# == CÓDIGO 3 == #
# Z = np.zeros((4, ))
# Z[1:] = 1.
# print('Z: ', Z)

# == CÓDIGO 4 == #
# Z = np.ones((4,))
# Z[-1] = 0.
# print('Z: ', Z)

# == CÓDIGO 5 ==#
# X = np.twos((2, 2))
# print('X:\n', X)

# == CÓDIGO 6 ==#
# X = np.array([[1, 2], [3, 4]])
# Y = X[0, :]
# Y[1] = 10
# print('X:\n', X)

# == CÓDIGO 7 ==#
# X = np.array([[1, 3], [11, 10]])
# print(np.mean(X[X > np.pi]))

# == CÓDIGO 8 ==#
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog',
#                   'cat', 'snake', 'cat', 'dog', 'dog'],
#        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#        'priority': ['yes', 'yes', 'no', 'yes', 'no',
#                     'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# == CÓDIGO 9 ==#
# df = pd.DataFrame(data=data, index=labels)
# print(df.sort_values(by='visits', ascending=False))

# == CÓDIGO 10 ==#
y_true = np.array([1., 2., 1.])
# y_pred = np.array([1.1, 1.98, 1.05])
y_pred = y_true

print('y_true: \n', y_true)
print('y_pred: \n', y_pred)
print()

print(np.sqrt(((y_true-y_pred)**2).mean()))
