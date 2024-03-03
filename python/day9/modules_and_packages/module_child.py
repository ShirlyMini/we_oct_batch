########################################################3
# module- collection of classes and func
# from module1 import A
# from module2 import C
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
# obj= B()
#
# obj.func_child()
###########################################################3
# package- collectionof modules

# from pack1.module3 import parent1
# from pack1.module4 import parent2
#
# class B(parent1,parent2):  # child
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
# obj= B()
#
# obj.func_child()


from pack1.pack2.module5 import myfunction

myfunction()