import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()
from time import time
input1 = int(input('Enter 1 to start the watch : '))
start = Utility_obj.Time()
print(start)
input2 = int(input('Enter 2 to stop the watch : '))
stop = Utility_obj.Time()
print(stop)
time = stop - start
print(time)

