

**To print Single Value**


print(13)                            #printng numeric value

print("Hello World!")                #printing non-numeric value

-----------------------------------------------------------------------------------------------------------------------------------------------------

"""**To print Multiple Values**"""

print(12,"Twelve", 10, "Ten")

print(12,"Twelve", 10, "Ten", sep=":")

------------------------------------------------------------------------------------------------------------------------------------------------------
    
"""**To print Single Variables**"""

a = 12
print(a)

x = "Hello World!"
print(x)
------------------------------------------------------------------------------------------------------------------------------------------------------

"""**To print Multiple Variables**"""

a,b= 4,8
print(a,b)

x,y,z = 91.3 , "Komal" ,True
print(x,y,z, sep="/")

--------------------------------------------------------------------------------------------------------------------------------------------------------
"""**To Print Combination of Values & Variables**"""

a = 4
print("the square root of 2:", a)

name = "komal"
print("My name is" , name)

---------------------------------------------------------------------------------------------------------------------------------------------------------

"""**To delete a Variable**"""

t = 40
del t

y,z,x = 21,34.7, 98
del y, z

-------------------------------------------------------------------------------------------------------------------------------------------------------
"""**Format Function**"""

name = "komal"
CGPA = 9.03
print("my name is {} , and I got cgpa {}" .format(name,CGPA))

com = "Infosys"
ID = 10050
print("Name of the company is {}, and ID is {}" .format(com,ID))

--------------------------------------------------------------------------------------------------------------------------------------------------------

"""**To check the DataTypes of Variable**"""

k = 45
print(k)

type(k)

o = "Name"                           #string datatype
type(o)

p = False
type(p)

---------------------------------------------------------------------------------------------------------------------------------------------------------

"""**Contatination**"""

"Hello" + "World"

"Hello" +" "+ "World"

a = "hello"
b = "world"
a+b

a = "Hello"
b = "World"
a+ " " + b

