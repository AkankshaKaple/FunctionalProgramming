# This program replaces the given string by <<username>> in the statement
import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()

input = input('Enter your name : ')
string = 'Hello <<UserName>>, welcome to python!!!'
result=  Utility_obj.stringReplace(input, string)
print(result)
