import utilityPackage.utility
Utility_obj = utilityPackage.utility.utility()

a = int(input("Enter the value of 'a'"))
b = int(input("Enter the value of 'b'"))
c = int(input("Enter the value of 'c'"))
root = []
root = Utility_obj.quadraticEquation(a,b,c)
print(root)