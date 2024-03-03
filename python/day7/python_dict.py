# mapping type
#prod1=120rs
#prod2=130
#prod3= 140

# dictionary

#collection of key and value pair
# {}
# mutable and unordered()

# key = unique
# value can be dulicated

##################################################
# create

# mydict={'product1':120, 'product2':130, 'product3':130}
# print(mydict)
# print(type(mydict))
# mydict=dict({'product1':120, 'product2':130, 'product3':130})
# print(mydict)
# print(type(mydict))

# empty dict

# mydict={}
# print(mydict)
# print(type(mydict))
# mydict=dict()
# print(mydict)
# print(type(mydict))

##################################################
# accessing elem

# mydict={"brand":"maruthi", "price": 120000, "year": 2023}
# mydict={"brand":"maruthi", "price": 120000, "year": 2023, "brand":"hero", "brand":"i20"}

# appr1
# print(mydict["brand"])
# print(mydict["price"])
# print(mydict["year"])

#appr2
# print(mydict.get('brand'))
# print(mydict.get('price'))
# print(mydict.get('year'))

##################################################
# changing elem

# mydict={"brand":"maruthi", "price": 120000, "year": 2023}
#
# # appr1
# # mydict['price']=130000
# # print(mydict)
#
# # appr2(more than one value)
# mydict.update({"price": 130000, "year": 2020, 'seats':7})# add and update
# print(mydict)

##########################################
# for loop

# mydict={"brand":"maruthi", "price": 120000, "year": 2023}

# for i in mydict:
#     print(i)
#
# for i in mydict.items():
#     print(i)
#
# for key,val in mydict.items():
#     print(key, val)

# print(list(mydict.items())[0])
# print(list(mydict.items())[1])
# print(list(mydict.items())[2])

# for i in mydict.keys():
#     print(i)
#
# for i in mydict.values():
#     print(i)
#
# print(list(mydict.keys())[0])
# print(list(mydict.values())[0])

###########################################3
# in and not in
# mydict={"brand":"maruthi", "price": 120000, "year": 2023}
#
# print("year" in mydict.keys())
# print("maruthi" in mydict.values())
# print("yeardscs" not in mydict.keys())
# print("maruthicsdc" not in mydict.values())

#############################################

# print(len(mydict))
# print(len(mydict.keys()))
# print(len(mydict.values()))

###################################
# add new key value pair

# mydict={"brand":"maruthi", "price": 120000, "year": 2023}
#
# # appr1
# mydict['purchased_on']='2024'
# print(mydict)
#
# # appr2(more than one value)
# # mydict.update({"price": 130000, "year": 2020, 'seats':7})# add and update
# # print(mydict)

##################################################3
# remove item

# mydict={"brand":"maruthi", "price": 120000, "year": 2023}
# print(mydict)
# appr1
# print(mydict.pop('year'))#2023
# print(mydict)

# appr2
# print(mydict.popitem())
# print(mydict)

# appr3
# del mydict['brand']
# print(mydict)
#
# del mydict
# print(mydict)#NameError: name 'mydict' is not defined. Did you mean: 'dict'?

# appr4
# mydict.clear()
# print(mydict)

################################
# combine
# d1={"brand":"maruthi", "price": 120000, "year": 2023}
# d2={"brand1":"audi", "price1": 360000, "year1": 2023}
#
# # print(d1+d2)#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#
# d1.update(d2)
# print(d1)
# print(d2)

#######################################33
# copy
# swallow  and deep

# d1={"brand":"maruthi", "price": 120000, "year": 2023}
# d2=d1#swallow copy
# print(f'{d1} id {id(d1)}')
# print(f'{d2} id {id(d2)}')
# d2.popitem()
# print(f'{d1} id {id(d1)}')
# print(f'{d2} id {id(d2)}')

# d1={"brand":"maruthi", "price": 120000, "year": 2023}
# # d2=d1.copy()#deep copy
# d2=dict(d1)#deep copy
# print(f'{d1} id {id(d1)}')
# print(f'{d2} id {id(d2)}')
# d2.popitem()
# print(f'{d1} id {id(d1)}')
# print(f'{d2} id {id(d2)}')