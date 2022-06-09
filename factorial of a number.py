''' Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720. '''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num = 20
print("Factorial of {} = ".format(num),factorial(num))            