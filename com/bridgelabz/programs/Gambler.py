#This program prints the number of times a person won and percentage
# of win and loss
import random
import utilityPackage.utility

numberOfBets= int(input('Enter number of times you wnat to gamble: '))
goal = int(input('Enter your goal: '))
money = int(input('Enter amount of money you have: '))
Utility_obj = utilityPackage.utility.utility()
list = []
list = Utility_obj.GambleingMethod(numberOfBets, goal, money)
print('Number of win : ' + str(list[0]))
print('Number of lose :' + str(list[1]))
print('Percentage of win : ' + str(list[2]))
print('Percentage of lose : ' + str(list[3]))

