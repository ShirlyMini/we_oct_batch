# range function
# range(start=0, end=n-1, step=1)# default values

# print(list(range(10)))
# print(list(range(0,10)))
# print(list(range(2,10)))
# print(list(range(5,10)))
# print(list(range(5,11)))

# print(list(range(0,10,2)))
# print(list(range(0,10,3)))
#
# print(list(range(1,10,2))) # odd
# print(list(range(2,11,2))) # even
# # 10, 9, 8...1
# print(list(range(10,0,-1)))
# print(list(range(20,0,-3)))

# While loop - condition based

# 1. initialize
# 2. condtion
# 3. increment

# # print 1 2 3 10
#
# a=1 # init
# while a<=10: # cond
#     print(a)
#     #a=a+1 # incr
#     a+=1

# print 10...1

# a=10 # init
# while a>=1: # cond
#     print(a)
#     #a=a-1 # decr
#     a-=1

# for loop - always goes with range function
# print 1 2 3 10
# for j in range(1,11):
#     print(j)

# for j in range(2,11, 2):
#     print(j)

for i in range(1,11):
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")