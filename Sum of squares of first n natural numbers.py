''' Sum of squares of first n natural numbers '''

n = int(input())
summ = 0
for i in range(1,n+1):
    summ = summ+i**2


print("Sum = ",summ)    