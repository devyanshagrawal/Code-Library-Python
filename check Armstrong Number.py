'''
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

'''
import math

n = input()

l = len(n)

summ = 0

for i in range(l):
    summ = summ + pow(int(n[i]),l)
    print(summ)

if summ == int(n):
    print("Yes,It's an Armstrong number")
else:
    print("No,it's not an Armstrong number")        