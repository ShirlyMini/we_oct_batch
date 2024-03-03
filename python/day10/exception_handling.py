# a=10
# print(a)#NameError: name 'a' is not defined

# print(10+"10")#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(1/0)#ZeroDivisionError: division by zero

# l1=[1,2,3,4]
# print(l1[4])#IndexError: list index out of range

# syntax error
# if 1<2
# print()

# exception error -
# print("statement1")
# print("statement1")
# print("statement1")
# print(1/0)# terminated here
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")

##############################################3
# try and except block

# try:
#     print(1/0)# zerodiv error
# except:
#     print("error happened")


# l1=[1,2,3,4]
# try:
#     print(l1[4])
# except Exception as var: # catch all kind of exception
#     print("exception happened!!!", var)


# l1=[1,2,3,4]
# try:
#     print(l1[4])
# except IndexError as var:
#     print("exception happened!!!", var)


# l1=[1,2,3,4]
# try:
#     # print(10+"10")
#     print(l1[4])
# except IndexError as var:
#     print("Index exception happened!!!", var)
#
# except TypeError as var:
#     print("Type exception happened!!!", var)

##################################################33
# optional block
# else
# finally

l1=[1,2,3,4]
try:
    print(l1[4])
except Exception as var:# when exception happen
    print("Exception happened!!!", var)
else:# when no except happen
    print("no exception happen")
finally:# no matter except happened or not
    print("finally block executed")

#Note : syntax error is not applicale or handled by try and except