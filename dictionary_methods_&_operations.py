
# dict methods


marks = {"history":45,"Hindi":56 ,"English" :56 }

marks.items()            # return the key: value pair present in dict in format of list of tuple


marks.keys()             #return the keys in dict


marks.values()           #return the values in dict

-------------------------------------------------------------------------------------------------------------------------------

# Dict Operation

-------------------------------------------------------------------------------------------------------------------------------

marks = {"history":45,"Hindi":56 }
marks.update({"eng":78})                                   #adding single value
marks

marks.update({23:67, "Ks":34.87 , 67.9:True})                 #adding Multiple values
marks

--------------------------------------------------------------------------------------------------------------------------------------

marks = {'history': 45, 'Hindi': 56, 'eng': 78, 23: 67, 'Ks': 34.87, 67.9: True}
del marks["Hindi"]                                        #deleting the values
print(marks)

----------------------------------------------------------------------------------------------------------------------------------------

marks = {'history': 45, 'Hindi': 56, 'eng': 78}
marks.clear()                                  # clears the dictionary
marks

-----------------------------------------------------------------------------------------------------------------------------------------

marks = {'history': 45, 'Hindi': 56, 'eng': 78}
new_marks = marks.copy()                         #copied the dict

new_marks.update({"chem": 90})
print(marks)
new_marks

-----------------------------------------------------------------------------------------------------------------------------------------

marks = {'history': 45, 'Hindi': 56, 'eng': 78}            
marks['Hindi'] = 76                                #Replacing the existing value with new 
marks

-----------------------------------------------------------------------------------------------------------------------------------------

d ={"Ks":43,"Sk":90,"hs":65}
d.pop("Sk")                                         #Replacing the existing key  with new 

