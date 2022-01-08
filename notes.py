# m = range(5)  # start from 0, end n-1
# m = range(1, 10, -1)
# # m = range(1, 10, 2)
# # m = range(10, 1, -2)
# print(type(m))
# print(m)
# for i in m:  # generate i ---> upon call
#     print(i)

# break , continue   ---> for loop , while loop
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("loop ended")

print("This is after loop ")