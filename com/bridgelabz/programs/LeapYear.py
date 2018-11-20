# This program returns whether the given year is leap year or not

import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()
year = input('Enter the year : ')

result = Utility_obj.leapYear(year)
print(result)