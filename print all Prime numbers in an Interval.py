""" Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval """

def findPrime(a,b):
    primeList = []
    for i in range(a,b):
        if a>1:
            flag = 0
            for j in range(2,int((i/2)+1)):
                if i%j == 0:
                    flag = 1
                    break
            if flag==0:
                primeList.append(i)

    return primeList


num1 = 2
num2 = 10
primeNumbers = findPrime(num1,num2)
print("All prime numbers between {} and {} are: ".format(num1,num2),primeNumbers)            
