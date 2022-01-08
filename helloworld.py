print("################# Day01 #####################")

# python loosly typed lang.

# python dynamically typed lang.

# x = 100  # int
# print(type(x))
# # change type of value inside
# # type conversion --> casting
# # convert from int to str
# x = str(x)
# print(type(x))

# # valid syntax
# name = "Nabieh" # str
# print(name)
# name = int(name)

###################################
#
y = "100"
y = int(y)

pii = 3.14
print(type(pii))

# boolean
m = True
# convert bool to int
m = int(m)
print(m)
n = False   # 0
###################3
# mm = 0
# mm = bool(mm)
# print("mm", mm)

# ######################
#
# # Falsy values
# # False , 0 , "" , """""", ''''''
# x = 0
# y = 100
# if x and y:
#     print("hiii")

###################################
'''
This is a string acts like a comment and will not be 
interpreted

if (condition){  

}
'''
day = "Friday"
company = "iti"
if (day == "Friday") and (company == "ITI"):

    print("You might work during your weekends")
elif day != "Fiday" or day != "Saturday":
    print("You must have work today")
else:
    print("Friday is your day-off")

'''
    if (x > 5){
    }
    else{
    }
'''
x = 100
if x > 10:
    pass
elif x < 5:
    pass
else:
    pass



