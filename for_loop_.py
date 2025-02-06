# FOR LOOP


l=[]                            #using for loop
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)

s = (23,67,"sb",34.9,(34.7,78,"ks"))        #sequence in tuple
for i in s:
    print(i)
------------------------------------------------------------------------------------------------------------------------------
**Q.Ask user to enter a 5 numbers and do a sum**"""

sum=0
for i in range(5):
    numbers = eval(input("enter a number:"))
    sum = sum+numbers
print(sum)

-------------------------------------------------------------------------------------------------------------------------------------------
"""**write a multiplication table of 5**"""

print(5,"*",1,"=",5)
print(5,"*",2,"=",10)
print(5,"*",3,"=",15)
print(5,"*",4,"=",20)
print(5,"*",5,"=",25)

for i in range(1,6):              #whichever value is changing considered as i
    print(5,"*",i,"=",5*i)

------------------------------------------------------------------------------------------------------------------------------------------------

n=['k', 'o', 'k', 'o', 'm', 'a', 'l', 'a', 'l', '9', '4', '9', '0', '1', '9']
m=[]                            #without using set
for i in n:
    if i not in m:
        m.append(i)
print("given values",n)
print("unique values",m)

for i in m:
    print(i,n.count(i))

----------------------------------------------------------------------------------------------------------------------------------------------------------
#write a program to return a pawan

l=["srk","ks","pawan","uday","re"]
k=[]
for i in l:
    if i=="pawan":        #here loop will be repeated for 3 times asa it will matches the condn loop will break and will not check for further values
        k.append(i)
        break
print(k)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#write the program to sum all even numbers and all odd numbers seperateley


l=[10,20,30,35,37,32,39]

es=0
os=0

for i in l :
    if i%2==0:
        es = es+i
    else:
        os=os+i

print("sum of even numbers",es)
print("sum of odd numbers",os)

------------------------------------------------------------------------------------------------------------------------------------------------

# nested for loop

'''
i will work as (i=1,1=2,i=3)
i =1
for j (it wil work as j=1,j=2) so
print(i,j)
1,1
1,2 -->after completing for all j values it will go for next i value

i =2
print(i,j)
2,1
2,2
'''

for i in range(1,4):
    for j in range(1,3):
        print(i,j)


