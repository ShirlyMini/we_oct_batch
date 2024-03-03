# str1="Hello"
# str2="welcome"
#
# print(max(str1))
# print(min(str1))
# print(max(str2))
# print(min(str2))
#
# # numerical equalent
# # ord()--> convert char to number(asiic)
#
# print(ord("a")) #
# print(ord("A"))
#
# # convert number(asiic) to char
#
# print(chr(97)) # a
# print(chr(1234)) # a

############################################3
# existence of substring
#"in" and "not in" operator
# str2="welcome python"

# print("python" in str2)
# print("python" not in str2)
# print("java" in str2)
# print("java" not in str2)

# comparator operation
# print("string" == "string") # true
# print("string" != "string") # False
# print("string" != "strong") # true
# print("string" == "strong") # false
# print("string" < "strong") # True (taking the numerical equalent)

##########################################3
# Testing strings


# str1="welcome python"
# str2="welcome"
# str3="welcome123"
# str4="123456"
#
# str5="   "
# str6="Welcome Python Is"
# str7="WELCOME"
# str8="123.456"
# print(str1.isalpha()) # false
# print(str2.isalpha()) # True
# print(str3.isalpha()) #false
#print(str4.isalpha()) #false

# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())

# print(str1.isspace())
# print(str2.isspace())
# print(str3.isspace())
# print(str4.isspace())
# print(str5.isspace())

# print(str1.istitle())
# print(str6.istitle())

# print(str2.isupper())
# print(str2.islower())
# print(str7.isupper())
# print(str7.islower())

# print(str4.isdigit())
# print(str3.isdigit())
# print(str3.isdecimal())
# print(str4.isdecimal())
# print(str8.isdigit())
# print(str8.isdecimal())
# print(str8.isnumeric())
# print(str4.isnumeric())
# print(str3.isnumeric())


################################################33
#searching for substring


# str1="Welcome to python to python"
#
# print(str1.endswith("python"))
# print(str1.startswith("python"))
# print(str1.startswith("Wel"))
# print(str1.startswith("W"))
#
# print(str1.find("o"))
# print(str1.find("to"))
# print(str1.find(" "))
# print(str1.find("o", 8))
# print(str1.find("o", 8, 17))
# print(str1.count("to"))
# print(str1.count("o"))
# print(str1.count("o"))
# print(str1.count("o", 8,17))
# print(str1.count("o", 8))

##################################################3
# converting strings

#str1="welcome to python"
# str2="python"
# # str3="WELCOME"
# # str4="WelCome To pyTHON"
#
# # print(str1.capitalize())
# # print(str2.capitalize())
# # print(str1.title())
# print(str2.title())
# print(str2)
# b=str2.title()
# print(b)
# # print(str1.upper())
# # print(str3.lower())
# # print(str4.swapcase())
#
# a="string"
#
# print(a[3])
# #a[3]="o"#TypeError: 'str' object does not support item assignment
# print(a.replace("i", "o"))
# print(a)
# a1=a.replace("i", "o")
# print(a1+"er")


#######################################3
# reverse string

# appr 1

# s="welcome to python"

# -n.. -3 -2 -1 0 1 2 3 4 5 ...n
 #ranges [start=0: stop=n-9(last index):incremental=1]
# reverse index = travese from right to left -1 to
# print(s[1:10]) # 1 to 9
# print(s[5::2])
# print(s[5::3])
# print(s[-1:-3])
# print(s[-3:-1])
# print(s[-3:])
# print(s[-16:-1])
# print(s[-16::2])
#
#
# print(s[::-1]) # one line appr
# print(s[-7:-15:-1]) # come to

# appr2

# using for loop

# str1="welcome to python"
# rev_str=""
#
# for i in str1:
#     print(rev_str)
#     rev_str=i+rev_str # w+""=w
#                         # e+w=ew
#                         # l+ew=lew
# print(rev_str)

# seq type
# list
#tuple
# set # array
#
# dict #hasp map