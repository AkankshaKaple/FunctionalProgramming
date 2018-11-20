#This program gives the Euclidean distance from the point (x, y) to the origin (0, 0)
import sys
from  math import *
# import utilityPackage.utility
# Utility_obj = utilityPackage.utility.utility()


x = int(sys.argv[1]) #Taking first input from command line
y = int(sys.argv[2])  #Taking second input from command line
distance = int(sqrt(x*x + y*y))
print(distance)