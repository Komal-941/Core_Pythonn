# Set Methods

s ={1, 2, 2.5, 3, 4, 'Komal', 5, 7}
s.add(89)                              #add a single value only
print(s)

s.add("Shelar")
print(s)

------------------------------------------------------------------------------------------------------------------------------------------------

s ={1, 2, 4, }                           #whille assigning multiple items need to assign them in a list
s.update(["Shelar", False , 8.4, 23])     #adds muliple values
print(s)
-----------------------------------------------------------------------------------------------------------------------------------------------

s ={1, 2, 2.5, 3, 4, 7,8, "Komal"}
s.discard("Shelar")                         #used to removing particular value
print(s)
--------------------------------------------------------------------------------------------------------------------------------------------------------

s ={1, 2, 2.5, 3, 4, 'Komal', 5, 7}
s.remove("Komal")                           #used to removing perticular value
print(s)
------------------------------------------------------------------------------------------------------------------------------------------------------

s ={1, 2, 2.5, 3, 4, 'Komal', 5, 7}
del s                                             #to delete the set
-------------------------------------------------------------------------------------------------------------------------------------------------------
original_object ={1, 2, 2.5, 3, 4, 'Komal', 5, 7}
print(id(original_object))            
new_object = s.copy()                    #will copy the object as a shell means, we can dupliacte but the changes in second object will not affect on first
print(new_object)
print(id(new_object))

new_object.add(23)              # will ad the value in new object only
print(new_object)

print(original_object)                 # original object will remain the same
-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Set Operations

a ={2,4,6,8}
b = {4,5,6,7,8}
c= a.union(b)                             #will copy the object as a shell means, we can dupliacte but the changes in second object will not affect on first
print(c)
------------------------------------------------------------------------------------------------------------------------------------------------------------

a ={2,4,6,8}
b = {4,5,6,7,8}
c= a.intersection(b)           #it will create a new objcet with  common elements of both set
print(c)
------------------------------------------------------------------------------------------------------------------------------------------------------

s1.isdisjoint(s2)                #returns boolean value if set are having intersection or not. (common elements in between)

s2.isdisjoint(s3)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

s1 ={1,2,3}
s2 = {2,3,4,5}

print(s1-s2)        #if there are comon elements between two sets and we wanna remove a common element from any one set
print(s2-s1)

s1 ={1,2,3,5,6}
s2 = {2,3,5,7,8}

print(s1-s2)
print(s2-s1)
------------------------------------------------------------------------------------------------------------------------------------------------

s1 ={1,2,3,5,6}
s2 = {2,3,5,7,8}

s1.symmetric_difference(s2)     #returns new set of the element that are either of sets, but not in both (eleminate the common one )

s1 ={1,2,3,5,6}
s2 = {2,3,5,7,8}
print(s1)
print(s2)

s1.union(b) - s1.intersection(s2)
----------------------------------------------------------------------------------------------------------------------------------------------------

s1 ={2,3,5}
s2 = {2,3,5,7,8}

ans1 = s1.issubset(s2)       #if all values in set1 are present in set2 then set1 is called as sub set  and set2 is super set.
print(ans1)

ans2 = s2.issubset(s1)
print(ans2)
-------------------------------------------------------------------------------------------------------------------------------------------

s1 ={2,3,5}
s2 = {2,3,5,7,8}

ans1 = s1.issuperset(s2)            #if all values in set1 are present in set2 then set1 is called as sub set  and set2 is super set.
print(ans1)

ans2 = s2.issuperset(s1)
print(ans2)

