# This program shows the harmonic values till number N given by user

import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()

number = int(input('Enter the number'))
result = Utility_obj.HarmonicValue(number)
print(result)