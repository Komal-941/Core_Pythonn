# import math       #will import math module func

math.sqrt(81)        #to know the use of func can use shift+tab to get docstring

math.factorial(5)

from math import *            #importing all func
sqrt(9)

factorial(5)

math.exp(1)

pow(2,3)                      #will give the cube of 2

log(5)

import random

random.random()                 #will give number between 0-1

for i in range (10):
    print(random.random())          #this will give u a 10  float values from  0-1

for i in range (5):
    print(random.randint(1,50))            #here it will gives 5 integers randomly numbers from 1-50

for i in range (10):
    print(random.randint(1,50))

#if we don't want a repeated values
def unique():
    s=set()
    while True:
        x = random.randint(1,50)
        s.add(x)
        if len(s)>10:
            break
    print(s)#gives op in set

unique()



