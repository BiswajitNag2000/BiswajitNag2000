import numpy

my_array = []
a = int(input("what number of speed you want to enter? :"))
for _ in range(a):
    my_array.append(float(input("Enter the speed in km/hr:")))
my_array = numpy.array(my_array)
mean = sum(my_array) // len(my_array)
print("Enter the Average speed is: ", mean, "km/hr")
