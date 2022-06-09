'''  
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
Fn = Fn-1 + Fn-2

'''

def fib(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)


print("Fibonacci sum = ",fib(10))        

