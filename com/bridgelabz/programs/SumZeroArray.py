from array import *
import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()

array1 = array('i' , [])
size = int(input('Enter the size of array : '))
print("Enter" , size, "elements in an array")
for i in range(size):
    element = int(input())
    array1.append(element)

print(array1)
array1 = Utility_obj.SumZeroArray(array1, size)