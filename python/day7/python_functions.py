# set of statement which will do specific task
# create function - no mem alloc
# invoke function - mem alloc
# def is keyword

# def myfunc():#create functio
#     print("Hello")
#     a=10
#     b=20
#     print(a+b)
#
# myfunc()#invoke function
########################################################
# return statement

# def myfunc():
#     a=10
#     b=20
#     #print(a+b)
#     return a+b
#
# print(myfunc())
#
# var=myfunc()
# print(var>100)

# def myfunc():
#     a=10
#     b=20
#     #print(a+b)
#     return a, b
#
# print(myfunc())#(10, 20)

# def myfunc():
#     a=10
#     b=20
#     return
#
# print(myfunc())#None

# def myfunc():
#     a=10
#     b=20
#     return True
#
# print(myfunc())

######################################################
# parameters
# postional and keyword

# def addition(a,b):
#     print(a+b)
#
# addition(10,20)# postional
# addition(a=10,b=20)# keyword
# addition(b=10,a=20)# keyword


# def addition(a,b,c=0,d=0):# default parameter
#     print(f'{a}+{b}+{c}+{d}={a + b + c + d}')

# addition(10,20)# postional
# addition(10,20,30)# postional
# addition(10,20,30, 40)# postional

# addition(a=10,b=20)# keyword
# addition(a=10,b=20,c=30)# keyword
# addition(a=10,b=20,c=30,d=40)# keyword

# addition(10,20,c=30, d=40)
# addition(10,20,a=30, b=40)#TypeError: addition() got multiple values for argument 'a'
# addition(a=10,b=20,30, 40)#positional argument follows keyword argument


##############################################################3
# global and local variable
# global - var outside func
# local - var inside func
#################################################3
# a=1
#
# def myfunc(c):
#     b=2
#     print("inside the func", a,b,c)
#
# print("before call func", a)
# myfunc(10)
# print("after call func", a)


# a=1# global
#
# def myfunc():
#     a=2# local
#     print("inside the func", a)
#
# print("before call func", a)
# myfunc()
# print("after call func", a)

# a="global"# global
#
# def myfunc():
#     global a# local to global
#     a="local"# local
#     print("inside the func", a)
#
# print("before call func", a)
# myfunc()
# print("after call func", a)