
# While Loop


x=1               
while x<3:         
    print("Ks")    
    x = x+1        
-------------------------------------------------------------------------------------------------------------------------------------------------

#nested while ---> while in a while
i=1
j = 1
while i<=5:
    print("telusko")
    i= i+1
    while j <=5:
        print("rocks")
        j =  j+1         # first it will enter to a 2nd while condn(inner loop) complete the loop condn and then again will go first while condn

i=1

while i<=5:
    print("telusko", end=" ")
    j = 1
    while j <=5:
        print("rocks",end=" ")
        j =  j+1
    i= i+1
    print()
-------------------------------------------------------------------------------------------------------------------------------------------------------
print("Ks")
print("Ks")
print("Ks")
print("Ks")
print("Ks")
print("Ks")
print("Ks")

#instead of writing a same line for multiple times and gets printed we cando a looop

x=1
while x<=7:
    print("Ks")
    x=x+1           

------------------------------------------------------------------------------------------------------------------------------------------

x = 1

while x<5:
    print("DA")
    x= x+1
    if x==3:
        break
----------------------------------------------------------------------------------------------------------------------------------------
"""**While True - it is infinite loop . thi will stop using break only**"""

x=1
while True :
    print(x,"Komal")
    if x==6:
        break
    x=x+1
-------------------------------------------------------------------------------------------------------------------------------------------
"""Q. check for the student named a mahesh"""

while True:                   # it will ask for input until the if condn satisfies
    name = input("Enter the name :")
    if name =="Mahesh" or name=="mahesh":
        break

x=1                   
while x<=10:          
    print("DA")        
    x= x-5             
    if x<=-20:         
        break

----------------------------------------------------------------------------------------------------------------------------------------

x = 1

while x<7:
    print(x,"DA")
    if x==6:
        break
    x= x+1
--------------------------------------------------------------------------------------------------------------------------------------------------

"""Q. Ask the user to put a 5 numbers and do sum"""

s =0
x=1
while x<=5:
    n=eval(input("Enter the number:"))
    s=s+n
    x=x+1

print(s)
-------------------------------------------------------------------------------------------------------------------------------------------------------

"""**Q.Ask use to enter multiple values and do sum**"""

print("Enter all the numbers wanted & once done with all enter a #")
s=0                                  
while True:                           
    n= input("Enter the numbers:")
    if n=="#":                        
        break
    s=s+eval(n)
print("Sum of all values",s)

--------------------------------------------------------------------------------------------------------------------------------------------------------

## **while else**

x = 1
while x<=5:
    print("DA")
    x= x+1           #here while condition(while x<=5) fails as x=6; so the break is ot executed
    if x==13:        # as written above break is not executed ; elese will execute
        break
else:
    print("python")

