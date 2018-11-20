import sys
import math
number = int(sys.argv[1])
if 0 <= number <= 31 :
    for i in range(number + 1):
        x = (2**i)
        print(x)
else :
    print('Enter proper value ')
