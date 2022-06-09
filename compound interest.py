'''

Formula to calculate compound interest annually is given by: 
A = P(1 + R/n*100) nt 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span
n is the number of times interest applied per time period

'''

import math

p = 1000
r = 20
n = 4
t = 2

interest = (p*(1+r/(n*100))**(n*t))

print("Compound interest = {:.2f}".format(interest))