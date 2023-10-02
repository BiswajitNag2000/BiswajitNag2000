#Array manipulation(reshape and transpose)
import numpy as np
a = np.arange(20)
print("Original Array:")
print(a)
#Printing Reshape result
b = a.reshape((5,4))
print("Reshaped Array:")
print(b)
#Printing Transpose result
c = a.transpose()
print("Transpose of Array:")
print(b)