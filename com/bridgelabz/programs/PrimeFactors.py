def PrimeFactors() :
    number = int(input('Enter the number : '))
    if number > 0:
        list = []
        listPrimeFactors = []
        j = 0
        i = 0
        k=0
        num = number+1
        for i in range(2,num):

         while number%i == 0:
                list.append(i)
                number=number/i


        print(list)

        for k in range(0,len(list)):
                if list[k] == 2:
                    listPrimeFactors.append(list[k])
                else :
                    for j in range(2, list[k]):
                        if   list[k]%j == 0 :
                            flag = 0;
                            break
                        else :
                            flag = 1
                    if flag == 1:
                        listPrimeFactors.append(list[k])
                    else:
                        pass

        print(listPrimeFactors)
        PrimeFactors()

    else :
        print('Enter value greater than 0')
        PrimeFactors()
        return

PrimeFactors()