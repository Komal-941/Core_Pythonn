
# Tuple methods

mytuple1 =(1,2,3,2,1,5,4,1,2,3,2,[8,7,1,2,3,])

mytuple1.count(1)          #----> will count tuple items or indivual items only
-----------------------------------------------------------------------------------------------------------------------------------------------

tuple1= (45,54,67,76,"Komal", 12.3, True)


tuple1.index(54)                 #will give the  index number of value available
----------------------------------------------------------------------------------------------------------------------------------------------

"""**convert tuple to list**"""

# to convert the list into tuple and tuple to list

p=(1,2,3)
print(type(p))                  #tuple -->list
print(p)

r=list(p)
print(type(r))                  #list -->tuple
print(r)

n = tuple(r)
print(type(n))                  #tuple -->list
print(n)

