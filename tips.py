# short hand if
age = 4
# if age < 10:
#     status = "Kid"
# elif 10 < age < 18:
#     status = "Teenager"
# else:
#     status = "Adult"
#
# print(status)

# status = "kid" if age <13 else "teenager" if age < 18 else "adult"
# print(status)

status = "kid" if age < 13 else "teenager" if age < 18 else "adult"
####################################################################
########## swap functions
# x, y = "Ahmed", "Python"
# # def swaps(x,y):
# #     temp = x
# #     x= y
# #     y = temp
# print(f"x ={x}, y = {y}")
# x,y = y,x
# print(f"x ={x}, y = {y}")


# join
# myname = "Ahmed" # act like an array
# print("_".join(myname))

# split
# myname ="noha:x:100:100"
# print(myname.split(":"))  # return with list

# is in check
# l1 = ["Ahmed", "Maraim", "Ali", "Salma", "Aya"]
# l2 = ["Ahmed", "Maraim", "Ali", "Salma", "Aya"]
# print(l1 is l2)  # is operator ,,, compare values and address
# print(l1 == l2)
# print("Ahmed" in l1)


# #### sequence unpacking
# names = ["Ahmed", "Maraim", "Ali", "Mohamed", "Noha","Salma", "Aya"]
# # a, b, c, d, e = names  # split the list into separate variables,
# # # ---> no of variables should match number of elements in the list
# # print(a, b, c, d, e)
#
# a, *b,d,  e = names  # split the list into separate variables,
# print(a, b, d, e)


### enumration
# enum ---> special datatype ===> helps you to restrict values of certain variable
##  weeekdays = enum("Sat", "sun")
weekdays = ("sat", "sun", "mon")

#### in python ---> enum ---> add counter to the itertable
l = [3,4,6,7,10]
# for i in l:
#     print(i)

# # create range ,,, 0,1,2,3,  # you used the range to create iterator , 0,1,2,3,4,
# for item in range(0,len(l)):
#     print(l[item])
### create iterator using enumarate function
# myl = enumerate(l)
# print(myl)  # enumerate object
# print(type(myl))
#
# for index, myval in myl:
#     print(f"index = {index}, and val = {myval}")

######### enum with set
# mys= {"a","b", 10}
# tests = enumerate(mys)
# print(tests)
# for indexx, item in tests:
#     print(f"index = {indexx}, and val = {item}

# dicc = {"course":"python", "track":"AI", "day":"friday"}
#
# enum_dic = enumerate(dicc)
# for index, item in enum_dic:
#     print(f"index = {index}, and val = {item}")


#######################
# all and any

# l = ["t", True, 0, "Ahmed", "Python"]
# print(all(l))  # check that all items in the itertable are evaluate to True
# print(any(l))  # check that at least of the items in the itertable are evaluate to True.


# print
#
# print("Good morning",end=" ")
# print("Test")

# check string --=-> values is spaces
# name = input("Plz enter name   ")
# if name.isspace():  # all the string is spaces
#     print("plz provide another string")
# else:
#     print(name)