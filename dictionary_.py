
# Dictionary {}

**empty dict**
"""

d= dict()
print(d)

d = {}
print(d)

d = {1:2,2:"r", 3.4:True , 6.5:"shelar"}
print(d)
type(d)

"""**nested dict**

 within dict one item as dict called as nested dict
"""

car ={"cary":2001 , "carb":"Audi" , "carc" : True , "cardd" : [12,17], "care": {23,56.7} }
print(car)
print(type(car))

"""**indexing**
- syn: varibale_name{key}
"""

car ={"cary":2001 , "carb":"Audi" , "carc" : True , 13.4 : [12,17], 24: {23,56.7} }
car[13.4]

car[13.4][0]

car["carb"]

car["carb"][1]

