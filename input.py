# -*- coding: utf-8 -*-
"""Input.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Komal-941/Core_Pythonn/blob/main/Input.ipynb
"""

# if we want a data from user (which may vary from user to user ) there is inbuilt function called Input
# by default it will take input as str datatype

a = input("enter your name :")
print(a)

x = input("ID:")
x

type(x)

#Eval Function is used when we want to give input apart frm strng ;
#this eval function evalute the values automatically ; no need to put datatype beofre input

a= eval(input("Put a Mob.No."))
a

type(a)

I= eval(input())
print(I)
print(type(I))

