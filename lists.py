# -*- coding: utf-8 -*-
"""Lists.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Komal-941/Core_Pythonn/blob/main/Lists.ipynb

# List []
- List is Advance Data type, where it can store multiple values
- Declaring a list is, Items separated by commas are enclosed within brackets [].
- List is Mutable. the items can be modified with in the same object

**Empty List** :- List with 0 item
"""

l =[ 10, 3.4, True,"Ks"]
print(l)

l[3][0]

l[2]

"""**Nested List**
- within a 1 List , adding more list
"""

p=[12,3,5,True,[12,"Komal",20.8],"Shelar"]
print(p)

type(p)

p[4][1][3]                         # idexing

print(len(p) -1)                  # positive index count

l=[1,4,16,[25,36],49,"srk"]

len(l)

l[5]

l[3][1]

l[5][0]

l[-3][-1]

"""**List Indexing**"""

l=[25,30,[26,27,28,["hello"]],[32,38]]

l[2][3][0]

"""**List Slicing**"""

l= [10,20,30,40,50,60,70]

l[-3:-7:-1]

"""**list concatenation**
- it will add/ muliply the values if both are of the same type
"""

"komal" + "shelar"

l=[1,2,3]
m=[4,5,6]
l+m

l1=["d","b", "c"]
l2=["a", 6,4.0]             # as both are the list so we can concatenate
l1+l2

p=[10,20.3,True, "Komal"]

print(p)

"""**Replace one the item**"""

p[1] = 47.9
print(p)                 #the value at index no. 1 is replaced

"""**Adding a items in a list**"""

p.append(True)               # here we can add a item in list by using append but only on at a time
print(p)

p[2] = True
print(p)