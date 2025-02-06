# **1. Arithmetic Operator**

7+5                #addition

4-5                #subtraction

3*9                #multiplication

6/2                 # div : always gives output in float

9//4                 #floor div: gives the quotient value ; here  9 is divident and 4 is divisor ; 2 is quotient and  1 is remaining value

9%4                  # Modulo : it gives the remainder

2**2                  #exponent : to calculate the power like square , cube, forth root

(5*8)                 #paranthesis
---------------------------------------------------------------------------------------------------------------------------------------
# **2.Assignment Operator**
y= 5
y= y+4
print(y)

y=5
y+=4
print(y)

y=10
y*=4
print(y)

y=10
y/=4
print(y)

y=6
y**=2
print(y)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# **3.Comparison(Relational) Operator**

5==5       #will give outputas True or False

5!=5   #as they r same values it shows the false coz != this for not equal to

8>9

8.9<9.0

19>=10
------------------------------------------------------------------------------------------------------------------------------------------------
# **4.Logical Oprator**

5<3 and 2<3                   # all conditions needs to be true in the and opertor

5<4 or 2<3                    #min one condition should be true

# T or F and T         ( here as per operators precedence will fisrt focus on comparison operator)
# T or F               (as per Logical Operator prece it fisrt focus on AND ope. and then Or Ope.)
# T                    ( as in Or oper. min one cond is true)
4>3 or  2>5 and 5<6

b = False or not (5>2) and True
print(b)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
# **5.Identity Operator**

a= 3
b=3
a is b

print (id(a))

print (id(b))      # both id are matched

x= 6
y=8
x is not y

print (id(x))

print (id(y))  # ids are differnt

a = "venkatesh"
"tes" in a

a = "venkatesh"
"ter" in a
