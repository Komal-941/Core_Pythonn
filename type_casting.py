
### Used to convert one data type to other

a= 12
type(a)

-----------------------------------------------------------------------------------------------------------------------------------------
#converting int to bollean datatype

a1 = bool(a)
a1

type(a1)

-------------------------------------------------------------------------------------------------------------------------------------------

# Converting Boolean to Int Datatype

b = False
b1 = int(b)
type(b1)

------------------------------------------------------------------------------------------------------------------------------------------------
#converting int to float datatype

x = 45
x1 = float(x)
x1

type(x)

y = 98765
y1= float(y)
y1

type(y1)
-----------------------------------------------------------------------------------------------------------------------------------------------------
#converting  float  to int datatype

z = 56.89
z1 = int(z)
z1

type(z)

-------------------------------------------------------------------------------------------------------------------------------------------------

a = input("Enter Number  :", )             #This is a input Function
print(a)
print(type(a))                             # By default it will take a input as str only

a = int(input("enter a number :"))           # Here at this line we are doing typecasting string into integer
print(a)
print(type(a))

