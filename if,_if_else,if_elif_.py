
# IF


if 4<3:
    print('komal')            #as condition failed it will ingnore the block
    print('sopan')
    print('shelar')

print("Invalid")

if 1 < 3:
    a = eval((input("enter you age:")))
    b = 23
    c = a+b
    print(c)
-------------------------------------------------------------------------------------------------------------------------------
# if-else

a = eval(input("1sem perce:"))

if  a>60:                          #condn successed  ; so the main block  excecuted
    print("Passed")
else:
    print("Failed")

-------------------------------------------------------------------------------------------------------------------------------

ATM = 8970

Pin = eval(input("enter your Pin"))

if Pin==ATM:
    print("enter the withdrawl amount")

else:
    print("Pin Mismatched")

----------------------------------------------------------------------------------------------------------------------------------
# if-elif

Aggregate = eval(input())

if Aggregate>85:               #if the main block condn failed the it will go for the next condition i.e, 1 elif
    print("First Class")
#1 elif
elif Aggregate>70:
    print("Second Class")       #if the 1 elif condn failed the it will go for the next condition i.e, 2 elif
#2 elif
elif Aggregate>65:
    print("All Clear")            #if the 2 elif condn failed the it will go for the next condition i.e, else

else:
    print("Eligible for Re-exam")

#write a program to print grades of student, if marks>90 as a A grade ,if marks>70 as grade B, else Failed

marks = eval(input("Grades receieved:"))
name = input("students name:")

if marks>90:
    print(name,"got A Grade")

elif marks>70:
    print(name,"got B Grade")

else:
    print("Failed")

prompt = eval(input("assignments done : 0,1,2,3 :"))

if prompt ==0:
    print("3 assignmnets pending")

elif prompt ==1:
    print("2 assignments pending")

elif prompt==2:
    print("1 more assignment pending")

elif prompt==3:
    print("all work has been done")

else:
    print("Something went wrong ; check for the count")

-----------------------------------------------------------------------------------------------------------------------------------
# nested if

pin = 2354
balance = 30000

entered_pin = eval(input("enter your pin :"))

if entered_pin == pin:
    withdraw = int(input("enter the amount:"))
    if withdraw < balance:
        print("transaction proceed")
    else:
        print("insufficient balance")


else:
    print("Pin doesn't matched")

