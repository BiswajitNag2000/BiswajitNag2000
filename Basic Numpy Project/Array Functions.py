import numpy as np

a = np.arange(20).reshape(5, 4)
print("The array is:")
print(a)
print("the first two rows are:")
print(a[[0, 1], :])
print("The last two columns are:")
print(a[:, [-2, -1]])
