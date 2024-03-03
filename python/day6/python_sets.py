# {1,"string",[1,2,3]}
# mutable or changeable
#unordered

# create set
# myset={1,2,3,4,5,"apple", "orange", "kiwi"}
# print(myset)
# print(type(myset))

# empty set
# myset=set()
# print(myset)
# print(type(myset))#<class 'set'>
#
# myset={}
# print(myset)
# print(type(myset))#<class 'dict'>


######################################
#accessing elemnt in set

# myset={1,2,3,4,5,"apple", "orange", "kiwi"}
# #print(myset[0])#TypeError: 'set' object is not subscriptable
#
# for i in myset:
#     if "orange"==i:
#         print(i)
#
# #length
# print(len(myset))

# with duplicate element
# myset={1,2,3,4,4,4,4,5,"apple", "orange", "kiwi"}
# print(myset)
# print(len(myset))

# myset=[1,2,3,4,4,4,4,5,"apple", "orange", "kiwi"]
# print(myset)
# print(len(myset))
#########################################3
# in and not in oper
# myset={1,2,3,4,5,"apple", "orange", "kiwi"}
#
# print(4 in myset)
# print(6 in myset)
# print(4 not in myset)
# print(6 not in myset)

########################################
# add or update set
#
# myset={1,2,3,4,5,"apple", "orange", "kiwi"}
# # appr 1
# myset.add("grape")
# print(myset)
#
# # appr 2
# myset2={1,2,3,4,5}
# myset.update({"grape", "frut1", "fruit2"})
# print(myset)
# myset.update(myset2)
# print(myset)

############################################
#item removal

# myset={1,2,3,4,5,"apple", "orange", "kiwi"}

# appr1
# myset.pop()# random
# print(myset)

# appr2
# myset.remove("apple")
#print(myset)
# myset.remove("grape")
# print(myset)#KeyError: 'grape'

#appr3
# myset.discard("kiwi")
# print(myset)
# myset.discard("grape")
# print(myset)

###############################
# #copying withsets # mutable

# swallow

# set1={1,2,3,4,5}#d/obj address/mem address/ are same
# set2=set1
# print(f"set1{set1} ID {id(set1)}")#set1{1, 2, 3, 4, 5} ID 2574873321632
# print(f"set2{set2} ID {id(set2)}")#set2{1, 2, 3, 4, 5} ID 2574873321632
# set2.pop()
#
# print(f"set1{set1} ID {id(set1)}")#set1{1, 2, 3, 4, 5} ID 2574873321632
# print(f"set2{set2} ID {id(set2)}")#set2{1, 2, 3, 4, 5} ID 2574873321632

# deep copy
# set1={1,2,3,4,5}
# #set3=set1.copy()#appr1
# set3=set(set1)##appr2
# print(f"set1{set1} ID {id(set1)}")#set1{1, 2, 3, 4, 5} ID 1530493919392
# print(f"set3{set3} ID {id(set3)}")#set3{1, 2, 3, 4, 5} ID 1530493919168
# set3.pop()
#
# print(f"set1{set1} ID {id(set1)}")#set1{1, 2, 3, 4, 5} ID 1530493919392
# print(f"set3{set3} ID {id(set3)}")#set3{2, 3, 4, 5} ID 1530493919168

######################################################3
# combine two set

myset1={1,2,3,4,5}
myset2={"apple", "orange", "kiwi"}
myset3={1,2,3,6,7}
#print(myset1+myset2)#TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.intersection(myset3))

# comparator
print(myset1==myset2)
print(myset1!=myset2)
