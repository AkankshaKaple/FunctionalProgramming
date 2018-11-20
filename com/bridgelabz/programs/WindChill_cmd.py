#from math import *
import sys
t = int(sys.argv[1])
v = int(sys.argv[2])
if t > 50 or (v > 120 or v<3) :
    w = 35.74 + (0.6215*t) + ((0.4275*t) - 35.75 ) * (v**0.16)
    print(w)
else :
    print("Enter proper values")