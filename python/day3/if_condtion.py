# control statements
# 1. reusage of block
# 2. skip block
# 3. repeat based on condition

# types:
#
# 1. Conditional statement
#     1. if
#     2. if..else
#     3. if..elif..else[nested if]
#
# 2. looping statement [reuse]
#     1. while
#     2. for
#
# 3. jumping statement [Conditional statement & looping statement]
#     1. break
#     2. continue

# example 1

# print("statement 1")
# print("statement 2")
# print("statement 3")
# print("statement 4")
# if False:
#     print("statement 100")
# print("statement 5")
# print("statement 6")
# print("statement 7")
# print("statement 8")
# example 2
# n=2001
# print(n%4 == 0)
# if n%4 == 0:
#     print("Leap year")

# example3
# n=2001
# print(n%4 == 0)
# if n%4 == 0:
#     print("Leap year")
# else:
#     print("Not Leap year")

# example4
# n=1
# if n%2==0:
#     print("Hello EVEN")
#     print(f"{n} is even")
# else:

#     print("Hello ODD")
#     print(f"{n} is odd")

# eligibile for vote

# example5
# ternary operator
# n=4
# print(f"{n} is even" if n%2==0 else f"{n} is odd")
# {print("Hello EVEN"), print(f"{n} is even")} if n%2==0 else {print("Hello ODD"), print(f"{n} is odd")}

# example6
# multiple condition

n=int(input("enter weekday in number(1-7)"))
print(type(n))
if n==1:
    print("Sunday")
elif n==2:
    print("Monday")
elif n==3:
    print("Tuesday")
elif n==4:
    print("Wednesday")
elif n==5:
    print("Thusday")
elif n==6:
    print("Friday")
elif n==7:
    print("Saturday")
else:
    print("invalid number")

#1=Jan, 2=feb

