import numpy as np
a = np.arange(20)
print("Original Array:")
print(a)

b = a.reshape((5,4))
print("Reshaped Array:")
print(b)

c = b.transpose()
print("Transpose of Array:")
print(c)