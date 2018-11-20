#This program prints the percentage of Heads and Tails occured
#  after flipping the coin N times
import random
numberOfFlips = int(input('Enter number of times you want to flip the coin'))
countTails =0
countHeads = 0
if numberOfFlips >= 0 :
    for x in range(numberOfFlips):
        for x in range(1):
            a = random.random()
            if a < 0.5 :
                    countTails += 1
            else :
                     countHeads += 1

else:
    print('Enter proper value')

    #print(countHeads)
    #print(countTails)
percentageOfHead = float((countHeads * 100)/numberOfFlips)
percentageOfTails = 100 - percentageOfHead
print('Percentage of Heads = ' + str(percentageOfHead))
print('Percentage of Tails = ' + str(percentageOfTails))