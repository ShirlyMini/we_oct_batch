# (1,"string",[1,2,3])
# immutable or not changeable
#ordered
# with tuples changing/ updating items not supported
# with tuples removal items not supported

#create tuple

# mytuple=(1,"string",[1,2,3],(1,2,3))
# print(mytuple)
# print(type(mytuple))#<class 'tuple'>

# mytuple=(1,2,3,4,5)
# mytuple=("a", "b", "c")
# print(mytuple)
# mytuple=tuple((1,"string",[1,2,3],(1,2,3)))
# print(mytuple)
# print(type(mytuple))#<class 'tuple'>

# empty tuple
# mytuple=()
# print(mytuple)
# #(or)
# mytuple=tuple()
# print(mytuple)

# accessing element in tuple
# mytuple=(1,"string",[1,2,3],(1,2,3))
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])
# print(mytuple[3])
# print(mytuple[-1])
#print(mytuple[-5])#IndexError: tuple index out of range
#print(mytuple[4])#IndexError: tuple index out of range
#
# print(mytuple[2][1])
# print(mytuple[-1][-1])

################################################3
# using for loop

# mytuple=("apple", "orange", "grape")
# for i in mytuple:
#     if i == "grape":
#         print(i)

###############################################
# changing the items in list

# mytuple=("apple", "orange", "grape")
# mytuple[1]="banana"
# print(mytuple)#TypeError: 'tuple' object does not support item assignment

###########################################
#indirect way to change items in tuple

# 1.convert tuple to list using list()
# 2.change the element
# 3.convert from list to tuple using tuple()

# mytuple=("apple", "orange", "grape")
# print(mytuple)
# print(id(mytuple))#2073253722752
#
# mylist=list(mytuple)
# print(mylist)#['apple', 'orange', 'grape']
# mylist[1]="banana"#
# print(mylist)#['apple', 'banana', 'grape']
# mytuple=tuple(mylist)
# print(mytuple)
# print(id(mytuple))#2073253613760

# length
# mytuple=("apple", "orange", "grape", "kiwi")
# print(len(mytuple))

###################################33
# check the presence of elemnt

# mytuple=("apple", "orange", "grape", "kiwi")
# print("kiwi" in mytuple)
# print("kiwicdcxa" in mytuple)
#
# print("kiwi" not in mytuple)
# print("kiwicdcxa" not in mytuple)
###################################
# adding new element tuple
# mytuple=("apple", "orange", "grape", "kiwi")
# #******NA*********

####################################
# remove element in tuple
# mytuple=("apple", "orange", "grape", "kiwi")
# print(mytuple)
# #******NA*********
#
# #with del statment
# #del mytuple[0]#TypeError: 'tuple' object doesn't support item deletion
# del mytuple
# #print(mytuple)#NameError: name 'mytuple' is not defined

##########################################3
# copying list (immutable or not changeable)
# swallow and deep copy

# swallow copy

# mytuple1=("apple", "orange", "grape", "kiwi")
# mytuple2=mytuple1
#
# print(f"mytuple1{mytuple1} ID {id(mytuple1)}")#1751539218960
# print(f"mytuple2{mytuple2} ID {id(mytuple2)}")#1751539218960
#
# # deepcopy
# mytuple1=("apple", "orange", "grape", "kiwi")
# #mytuple3=mytuple1.copy()# NA****************
# mytuple4=tuple(mytuple1)
# print(f"mytuple1{mytuple1} ID {id(mytuple1)}")#1751539218960
# print(f"mytuple4{mytuple4} ID {id(mytuple4)}")#1751539218960

###########################################
# tuple1=("apple", "orange", "grape", "kiwi")
# tuple2=(1,2,3,4,5)
#
# # combine tuple
# print(tuple1+tuple2)
# ###########################################33
#
# print(tuple1==tuple2)
# print(tuple1!=tuple2)

#############################################
# tuple1=("apple", "orange", "grape", "kiwi", "kiwi", "apple")
# print(tuple1.count("apple"))#2# number of occur
# print(tuple1.index("orange"))# retuns the index of item/elem/value
# print(tuple1.index("apple"))# 0
# print(tuple1.index("apple",1))# 5
# #print(tuple1.index("kiwi",1, 3))# ValueError: tuple.index(x): x not in tuple
# print(tuple1.index("kiwi",-3, -1))# 3
# print(tuple1.index("orange",1, 3))# 1
