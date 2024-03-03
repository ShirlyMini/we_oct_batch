# list to strings
# join()
# mylist1=['apple', 'banana', 'orange', 'kiwi']
# print(" ".join(mylist1))
# print(" and ".join(mylist1))
# print(" *** ".join(mylist1))
# var=" ".join(mylist1)
# print(type(var))#<class 'str'>

# string to list
# split()
# str1="apple banana orange kiwi"
# print(str1.split())# by default splits based on space
str2="apple/banana/orange/kiwi"
print(str2.split("/"))
print(type(str2.split("a")))
