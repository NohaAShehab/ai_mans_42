# list is mutable datatype
# can be changed after creation
names = ["Ahmed", "Sara", "Salma", "Habiba", "Ali", "Abdulrahman", "Mostafa"]
mixedlist = [1, True, "iti", 33.44, 4 + 7j, names]
# change list values in the run time
# names[1] = "Omar"  # update
# print(names)
# print(mixedlist)
# names[1] = "jkhjkhjk"  # update
# print(mixedlist)
# names[7] ="Toqaa"  # list assignment index out of range
# print(mixedlist)
### appending to the list --> add to the end of the list
# names.append("Toqaa")
# print(names)
#
# # insert to alist
# names.insert(2,"Noha")
# print(names)
names = ["Ahmed", "Sara", "Salma", "Habiba", "Ali", "Abdulrahman", "Mostafa"]
# l2 = ["Mariam", "Nabieh", "Haya", "Tariq"]
# #extend
# names.extend(l2)
# # names.extend("Aya")
# names.extend(["Aya"])
#
# print(names)
# #concatination
# l3 = names + l2
# print(l3)
# repetions
# students =["iti"]*5
# print(students)
# membership
# names = ["Ahmed", "Sara", "Salma", "Habiba","Ali", "Abdulrahman", "Mostafa"]
# # in
# print("Mostafa" in names)

l = [3, 55, 66, 77, 88]  # iteratable
print(min(l))
print(max(l))
# delete items from list
# # pop function
# print(l.pop())  # remove the last item
# print(l)


# pop function
# l = [3, 55, 66, 77, 66, 77889, 7877]
# print(l.pop(4))  # remove the last item
# print(l)

# delete item
l = [3, 55, 66, 77, 66, 77, 7877]
# print(l.remove(77))  # remove the last item
# print(l)


for item in l: #itertable
    print(f"item = {item}")


x = 10
name = "Mohamed"
track = "AI"
print(x,name, track)
