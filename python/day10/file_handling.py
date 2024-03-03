# txt or excel or py

# open using 3 modes
# read - if file not exsist it will create - it will throw error - file should exist
# write - overwritten- if file not exsist it will create
# append - no overwritten- if file not exsist it will create
# save

########################################3
# write
# fh = open("test1.txt", "w")
# fh.write("this the line 4\n")
# fh.write("this the line 5\n")
# fh.write("this the line 6\n")
# fh.close()

####################################
# append
# fh = open("test2.txt", "a")
# fh.write("this the line 1\n")
# fh.write("this the line 2\n")
# fh.write("this the line 3\n")
# fh.close()

####################################
# read
# fh = open("test3.txt", "r")#FileNotFoundError: [Errno 2] No such file or directory: 'test3.txt'
# fh = open("test1.txt", "r")
# # print(fh.read())# read all the content
# # print(fh.readlines())# read all lines in list
# # for line in fh.readlines():
# #     print(line)
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time
# print(fh.readline())# read one line at a time

############################################################33
# FH using with statement

# fh = open("test1.txt", "w")

# with open("test3.txt", "w") as fh:
#     fh.write("this is wriiten from with statement1\n")
#     fh.write("this is wriiten from with statement2\n")
#     fh.write("this is wriiten from with statement3\n")
#
# with open("test3.txt", "a") as fh:
#     fh.write("this is wriiten from with statement4\n")
#     fh.write("this is wriiten from with statement5\n")
#     fh.write("this is wriiten from with statement6\n")

with open("test3.txt") as fh: #default mode is read
    print(fh.read())