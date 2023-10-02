import numpy  as np
import sys

List = (range(10))


print("size of each element of list in bytes: ", sys.getsizeof(List[0]))

print("Size of whole list in bytes: ", sys.getsizeof(List)*len(List))

array_size = 10
one_dimensional_array = np.random.rand(array_size)
two_dimensional_array = np.random.rand(array_size, 2)
three_dimensional_array = np.random.rand(array_size, 3)

print("size of each element of the array in bytes:", one_dimensional_array.itemsize)
print("whole size of array in bytes:", one_dimensional_array.nbytes)
print("size of each element of the array in bytes:", two_dimensional_array.itemsize)
print("whole size of array in bytes:", two_dimensional_array.nbytes)
print("size of each element of the array in bytes:", three_dimensional_array.itemsize)
print("whole size of array in bytes:", three_dimensional_array.nbytes)




