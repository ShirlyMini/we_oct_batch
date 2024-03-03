#class 1- parent/ base/ super class
# class 2- child/derived

# acquiring the attr of parent to child

# class A:# parent
#     var1="parent var"
#     def func(self):
#         print("func from parent class A")
#
# class B(A):# child
#     var2="child var"
#     def func_child(self):
#         print("func from child class B")

################################
# obj=B()
# print(obj.var1)
# print(obj.var2)
# obj.func()
# obj.func_child()



#####################################################

# class A:  # parent
#     var1 = "parent var"
#
#     def func_parent(self):
#         print("func from parent class A")
#
#
# class B(A):  # child
#     var2 = "child var"
#
#     def func_child(self):
#         print("func from child class B")
#         print(self.var2)
#         print(self.var1)
#         print("#####################")
#         self.func_parent()
#
#
# obj=B()
# obj.func_child()

###############################################################
# class A:  # parent1
#     var_p1 = "parent1 var"
#
#     def func_parent1(self):
#         print("func from parent1 class A")
#
# class C:  # parent2
#     var_p2 = "parent2 var"
#
#     def func_parent2(self):
#         print("func from parent2 class C")
#
# class B(A,C):  # child
#     var2 = "child var"
#
#     def func_child(self):
#         print("func from child class B")
#         print(self.var2)
#         print(self.var_p1)
#         print(self.var_p2)
#         print("#####################")
#         self.func_parent1()
#         self.func_parent2()
#
# obj = B()
# obj.func_child()


#########################################################

class A:  # parent1
    var_p1 = "parent1 var"

    def __init__(self):
        print("parent1 constructor")

    def func_parent1(self):
        print("func from parent1 class A")

class C:  # parent2
    var_p2 = "parent2 var"

    def __init__(self):
        print("parent2 constructor")

    def func_parent2(self):
        print("func from parent2 class C")

class B(C,A):  # child# Method Resolution Order
    var2 = "child var"

    def __init__(self):
        print("child constructor")
        A.__init__(self)
        C.__init__(self)

    def func_child(self):
        print("func from child class B")
        print(self.var2)
        print(self.var_p1)
        print(self.var_p2)
        print("#####################")
        self.func_parent1()
        self.func_parent2()

obj = B()
obj.func_child()