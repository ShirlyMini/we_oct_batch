#types of functions

# class myclass:
#     # instance method
#     # instance refers object
#     #this is default method
#     def func1(self,a,b):
#         # self is repr the class obj
#         # self as first parameter
#         print("this is self parameter", self)
#         print("this is func1")
#         return a+b
#
#
#     def func2(a,b):
#         print(a)#<__main__.myclass object at 0x000002583B7F4390>
#         print(b)#1
#         return a,b
#
# # obj=myclass()# instanciation
# # print("this is obj", obj)
# # #obj.func1(obj,1,2)# obj is passed as first parameter
# # #
# # print(obj.func1(1,2))
# # print(obj.func2(1))#myclass.func2() takes 2 positional arguments but 3 were given
# # # obj and 2 other parameter a and b
#
# myclass.func1(1,2,23)
# myclass.func2(1,2)
# myclass().func1(1,2)
# myclass().func2(1)

# task + calc
# employee DB
###########################################################3333
# static method# class name
# instance method# obj creation

# class myclass:
#     @staticmethod# decorator
#     def func1():
#         print("this is function1")
#     @staticmethod
#     def func2(a,b,c):
#         print("this is function1",a,b,c)
#
# obj=myclass()
###############################important##########################
# print("this is myclass()", myclass())# obj
# print("this is myclass", myclass)# class name
# obj.func1()
# obj.func2(1,2,3)
# myclass.func1()
# myclass.func2(1,2,3)

####################################################
# constructor
# also a instance method
# __init__
# it will get invoked at the time of obje creator
# no return in constructor

class myclass:
    def __init__(self, a, b):
        print("this is my constructor1", a,b)


obj=myclass(1,2)
