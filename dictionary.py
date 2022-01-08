# set ---> values
# ---> list ---> index ---> refer to values
# key---> value pair
# dictionary
s = {"Python", True, 38}  # immutable datatype
# dictionary
# dic = {"course": "Python", "Absent": True, "Studentno": 38}
# print(type(s))
# print(type(dic))
# Associative arrays
# key:value pair representation for the data , seperated by comma -- > {}

# mydic = {"course": "Python", "Absent": True, "Studentno": 38}
# # access element at certain position using keys
# print(mydic["course"])
# # update cetain item
# mydic["course"] = "Pandas"
# print(mydic)
# # mutbable datatype
# mydic["year"] = 2022
# print(mydic)
# # before pyhon 3.6

### get len of the dic
# mydic = {"course": "Python", "Absent": True, "Studentno": 38}
# print(len(mydic))
# # get keys of dic
# print(mydic.keys()) # can be casted to list
# print(mydic.values())
# # get items of dic
# print(mydic.items())  # dic_items ([(key,value),....])
# mydic["day"]=None
# print(mydic)
# loop over dict
mydic = {"course": "Python", "Absent": True, "Studentno": 38}
# for myitem in mydic:
#     print(f"{myitem} : {mydic[myitem]}")

# for key, val in mydic.items():  # (key, value(
#     print(f"{key} : {val}")
#
# print("hii")
#
# "formmated string"
# myname = "Ahmed Nabieh"
# mytemp = f"My name is {myname}"

mydic = {"course": "Python", "Absent": True, "Studentno": 38}
d = {"day":"sat", "year":2022, "course":"Pandas"}
# mydic.update(d)
# print(mydic)
# dictionary doesn't suppor concatination
# c = mydic + d
# print(c)

myd = {"courses":["python","numerica"], "year":2022}
# # clear
# print(myd)
# myd.clear()
# print(myd)  # remove the key-value pairs
#
# del myd
dd = dict({"key":"value"})
print(dd)

myd = {"courses":["python","numerica"], "year":2022}
for item in myd:
    print(item)

if "courses" in myd:  # evaluate to true
    print("hii")

if 2022 in myd.values():
    print("byee")





