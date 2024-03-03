# [1,"string",[1,2,3]]
# mutable or changeable
#ordered

# create list

# mylist=[1,2,3,4,5]
# print(mylist)
# mylist=["apple", "orange", "kiwi"]
# print(mylist)
# mylist=[1,2,3,4,5,"apple", "orange", "kiwi"]
# print(mylist)
# print(type(mylist))#<class 'list'>
#
# mylist=[1,2,3,4,5,"apple", "orange", "kiwi", [1,2,3,4,5]]
# print(mylist)

# empty list
#mylist=[] or list()
# mylist=[]
# print(type(mylist))
# mylist=list()
# print(type(mylist))

#########################################################3
# accessing element in list

# mylist=[1,2,3,4,5,"apple", "orange", "kiwi", [1,2,3,4,5]]# 0 to n-1
#
# print(mylist[0])
# print(mylist[5])
# print(mylist[8])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-1][2])# nested list
#
# mylist=[["a", "b", "c"], ["d", "e", "f"]]
# print(mylist[0])
# print(mylist[0][1])

################################################3
# using for loop

# mylist=["apple", "orange", "kiwi", 1,2,3,4]
#
# for i in mylist:
#     if i =="orange":
#         print(i)

###############################################
# changing the items in list

# mylist=["apple", "orange", "kiwi", 1,2,3,4] # orange to banana
# print(id(mylist))
# mylist[1]="banana"
# print(mylist)
# print(id(mylist))
#
# # length
#
# print(len(mylist))#7

######################################3
# exesistence of an item

# mylist=["apple", "orange", "kiwi"]
#
# print("orange" in mylist)
# print("banana" in mylist)
#
# print("orange" not in mylist)#False
# print("banana" not in mylist)# true

########################################
# add new element in list

# mylist=["apple", "orange", "kiwi"]
#
# # approach1
# # mylist.append("banana")
# # print(mylist)
#
# # apprach 2
# mylist.insert(1,"banana")
# print(mylist)

#######################################
#remove element in list

#mylist=['apple', 'banana', 'orange', 'kiwi']

# appr 1

# #mylist.pop() # by default it will remove last element
# mylist.pop(1)
# #mylist.pop(10)#IndexError: pop index out of range
# print(mylist)

#appr2
# del statemnt

# del mylist[2]
# print(mylist)

# del mylist
# print(mylist)#NameError: name 'mylist' is not defined. Did you mean: 'list'?

# appr3
# mylist.remove("kiwi")
# print(mylist)

# clear list
# mylist=['apple', 'banana', 'orange', 'kiwi']
# mylist.clear()
# print(mylist)#[]

#################################################3
# copying list (mutable or changeable)
# swallow and deep copy


# swallow copy # id/obj address/mem address/ are same
# mylist1=['apple', 'banana', 'orange', 'kiwi']
# mylist2=mylist1
# print(mylist1)
# print(mylist2)
# mylist2.pop()
# print(f"mylist1{mylist1} ID {id(mylist1)}")
# print(f"mylist2{mylist2} ID {id(mylist2)}")

# deep copy #id are different
# mylist1=['apple', 'banana', 'orange', 'kiwi']
# mylist3=mylist1.copy()  # appr1
# print(f"mylist1{mylist1} ID {id(mylist1)}")
# print(f"mylist3{mylist3} ID {id(mylist3)}")
# mylist3.append("strawberry")
# print(f"mylist1{mylist1} ID {id(mylist1)}")
# print(f"mylist3{mylist3} ID {id(mylist3)}")

# mylist3=list(mylist1) ## appr2
# print(f"mylist1{mylist1} ID {id(mylist1)}")
# print(f"mylist3{mylist3} ID {id(mylist3)}")
# mylist3.append("strawberry")
# print(f"mylist1{mylist1} ID {id(mylist1)}")
# print(f"mylist3{mylist3} ID {id(mylist3)}")

##################################################
# combine two list

# mylist1=['apple', 'banana', 'orange', 'kiwi']
# mylist2=[1,2,3,4,5]
# mylist3=[1,2,3,4,5]
# appr 1
# print(mylist1+mylist2)#['apple', 'banana', 'orange', 'kiwi', 1, 2, 3, 4, 5]

# appr 2

# mylist1.extend(mylist2)
# print(mylist1)
# print(mylist2)

# mylist2.extend(mylist1)
# print(mylist1)
# print(mylist2)

# app3
#
# for i in mylist1:
#     mylist2.append(i)
#
# print(mylist2)

# comparator
# print(mylist1==mylist2)
# print(mylist1!=mylist2)