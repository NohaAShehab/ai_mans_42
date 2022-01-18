#

# 'sequence unpacking'
# l = [2, 4, 6, 7]
# a, b, c, d = l
# print(a, b, c, d)

with open("names.txt") as rfile:
    data = rfile.read()
    print(data)

print(rfile)

# list comprehension ---> python2
'generate list of integers , 2,4,6,8,10'
# l = [2,4,6,8,10]
# l = [i * i for i in range(1, 11) if i % 2 == 0]
# print(l)


myl = ["apple", "Kiwi","strawberry", "banana"]
# for i in myl:
#     print(i)

# for i in range(len(myl)):
#     print(f"item at {i} = {myl[i]}")


'Enumurate'
e_myl= enumerate(myl)  # generate iterator for the element
print(e_myl)
print(type(e_myl))

for i, item in e_myl:
    print(f"item at {i} = {item}")


myd = {"name": "noha", "email": "nshehab@iti.gov.eg"}

for i, item in enumerate(myd):  ### keys
    print(f"{i} --- {item}, {myd[item]}")


###################################################
l1 = [2, 5, 6]
l2 = [15, 7, 8]
m = l1 + l2  # new list

print(l1)