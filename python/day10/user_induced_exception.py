# raise
# assert

# raise - if conditional

# raise Exception("this is raised by shirly")#Exception: this is raised by shirly
raise IndexError("this is raised by shirly")#IndexError: this is raised by shirly
# raise AttributeError("this is raised by shirly")
# raise TypeError("this is raised by shirly")

# yr=1999
# try:
#     if yr%4==0:
#         print("leap year")
#     else:
#         # print("Not a leap year")
#         raise Exception("Not a leap year")#Exception: Not a leap year
# except Exception as msg:
#     print("exception caught",msg)

####################################################33
# assert(condition based)

# assert 5<2, "worng condition"#AssertionError: worng condition

# yr=1999
# try:
#     assert yr%4==0, "Not a leap year"
#     print("Leap year")
# except Exception as msg:
#     print("exception caught", msg)
###########################################################
# raise--use along with if condition---any kind of exception
# assert -- by default it is condition based--assertion error
###########################################################

# list1=[1,2,3,4,5]
# 100 in list1