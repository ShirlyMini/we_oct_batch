#jumping statement [Conditional statement & looping statement]
#     1. break
#     2. continue

# for j in range(1,11):
#     print(j)
#     if j==5:
#         break

# a=1 # init
# while a<=10: # cond
#     print(a)
#     #a=a+1 # incr
#     if a == 5:
#         break
#     a+=1
#
# print("next program")

# continue - skip any block

# skip number divisible by 5
# for j in range(1,11):
#     if j%5==0:
#         continue
#     print(j)

a=0 # init
while a<=9: # cond

    #a=a+1 # incr
    a+=1
    if a%5== 0:
        continue
    print(a)