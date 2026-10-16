# n = 4629
# x = [int(b) for b in str(n)]
# x.sort()
# total = 0
# for i in range(len(x)-2,len(x)):
#     total += x[i]
# print(total)

# #Finding the second largest number and multiflying them 
# n = 5831
# x = [int(x) for x in str(n)]
# x.sort()
# total = 1
# for i in range(len(x)-2,len(x)):
#     total *= x[i]
# print(total)

# #know ther smallest number
# n = 4629
# x = [int(d) for d in str(n)]
# x.sort()
# total = 1
# for i in range(2):
#     total *= x[i]
# print(total)


# n = 4629
# x = [int(d) for d in str(n)]
# x.sort()
# total = 1
# for i in range(len(x)-3,len(x)):
#     total *= x[i]
# print(total)

n = 5831
x = [int(d) for d in str(n)]
x.sort()
total = 1
for i in range(len(x)-2,len(x)):
    total *=x[i]
print(total)