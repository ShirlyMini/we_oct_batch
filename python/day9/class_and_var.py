class myclass:
    var1="class variable"

    def __init__(self):
        a="constructor var"
        # self.a=a#
        self.var2=a#
        myclass.var2=a
        print(a)

    def func1(self, a,b):# instance method
        print("this is func1", a, b)
        print(self.var1)
        print(myclass.var1)
        print(self.var2)

    @staticmethod
    def func2(a,b):
        print("this is func2")
        print(myclass.var1)
        # print(self.var2)#NameError: name 'self' is not defined


#############################
#myclass---> class name
obj=myclass()#---> obj
# print(obj.var1)
# print(myclass.var1)
obj.func1(1,2)
obj.func2(1,2)


