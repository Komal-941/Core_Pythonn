
# String Method

s="hello"
s.upper()                      # Return a copy of string in all upper case characters
---------------------------------------------------------------------------------------------------------------------------------------------

x= "WORLD"
x.lower()                        #Return a copy of string in all lower case characters

---------------------------------------------------------------------------------------------------------------------------------------------

x= "Hello WRORLD"
x.swapcase()                     #will convert the existing characters to the oppo. upper case

----------------------------------------------------------------------------------------------------------------------------------------------

d="day is tuesday"
d.capitalize()                 #the first letter will be capital and remaining as lower

f= "-hello World"
f.capitalize()

--------------------------------------------------------------------------------------------------------------------------------------------------

g="good Morning"
g.title()                       #first letter of each word will be Capitalized

----------------------------------------------------------------------------------------------------------------------------------------------------

h1= "it was  a Great day"
h1.istitle()                            #will check wether the first letter of evry word is in Upper case

--------------------------------------------------------------------------------------------------------------------------------------------------------

i=" it's really good!  "
i.strip()              #if at the start(leading) and at end(trailing) space is there ; it will get removed

-----------------------------------------------------------------------------------------------------------------------------------------------------

k2="123Python programming"
k2.removeprefix("123")             #if wanna remove some letters or numbers or any special character  from starting(leading)

----------------------------------------------------------------------------------------------------------------------------------------------------

k7="Python programming12//"
k7.removesuffix("2//")           #if wanna remove some letters or numbers or any special character from endng(leading)

----------------------------------------------------------------------------------------------------------------------------------------------------

o="Good Morning"
print(o)

o= o.replace("Good","Bad")       #Returns a copy of replaced string as new object and delete the last one
print(o)
--------------------------------------------------------------------------------------------------------------------------------------------
p= "My name is , Komal"             #whole string will split
p.split()

p1="My name is , @Komal"               #string will split as per the condn only (i.e, ,)
p1.split(",")
-------------------------------------------------------------------------------------------------------------------------------------------------
q="Komal","Sopan","Shelar"
(":").join(q)                           #to Join the list of strings as one
---------------------------------------------------------------------------------------------------------------------------------------------
r= 'python is very very easy '
r.index("very")                             #will give the index number for the value searched for (first letters index number only)

--------------------------------------------------------------------------------------------------------------------------------------------------

s="Its easy to learn"
s.find("easy")               #will give the index number for the value searched for (first letters index number only)

---------------------------------------------------------------------------------------------------------------------------------------------------

u= "941komal"
u.startswith("9")               #will give the boolean values if the given string starts as per mentioned

---------------------------------------------------------------------------------------------------------------------------------------------------

w= "KomalShelar"
w.isalnum()                    #retrun boolean values by checking wheter it contains alphates , numeric and special chara(including space)
-----------------------------------------------------------------------------------------------------------------------------------------------------

x= "Komal.Shelar"
x.isalpha()                   #use to check if only alphabates are there

x= "KomalShelar"
x.isalpha()
------------------------------------------------------------------------------------------------------------------------------------------------------

x= "KomalShel11ar"
x.isdigit()                       #use to check if only numbers are there

x= "10050"
x.isdigit()
-----------------------------------------------------------------------------------------------------------------------------------
y="Komal7721"
y.islower()         #return boolean if mentioned values are in the lower case (numbers doesn't matter)
 -----------------------------------------------------------------------------------------------------------------------------------

z="Komal7721"
z.isupper()        #return boolean if mentioned values are in the upper case (numbers doesn't matter)


