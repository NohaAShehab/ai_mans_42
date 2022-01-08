# concatination
fname = "Noha"
midname = "Abd El-Hady"
lname = "Shehab"
# fullname = fname + " " + midname + " " + midname + " " + lname
# print(fullname)
# concatination between int and str ?
# y  = "Ahmed" + 10  # error can only concatenate str (not "int") to str
# y = 10 + "Ahmed"  # unsupported operand type(s) for +: 'int' and 'str'
# y = "Ahmed" + False
# z = 10 + True
# print(z)
# interpolation
# fullname = fname + midname*2 + lname
# print(fullname)

# replace
# test = "THis is my simple example"  # replace i with !
# print(test.replace("is", "!$"))
# # capatialize
# print(test.capitalize())  # return new string --->
# print(test.islower())  # isupper
# print(test.lower())  # the return the functions

# functions  ---> affect the same variable
# functions ---> return new value

# x = "100.12"
# y = "Noha#"
#
# # print(y.isalpha())  # check if all the string chars are alpha ---> A to z
# print(x.isnumeric())  # check if the value inside the string is int value ---> detect lang. ascii
# print(x.isdigit())  # check if the value inside the string is int value


#############3 strip
name = "    Information Technology Institute     "
# print(name.replace("i",""))
# print(len(name))
# print(len(name.strip()))
# print(name)
# print(name.strip(" Iiet"))
# print(len(name))
# print(len(name.rstrip()))
# # print(name)
# print(name.rstrip(" Iiet"))


###### format
# template string
# string formatting ---> add 0 as index ,,,
# greeting = "My name is {1}, I works at {0}"
# print(greeting.format("Noha", "ITI", "yyyy", "tttt"))
# print(greeting.format( "Valeo", "Test"))
# print(greeting.format("Amr", "Amazon"))

# # named formated, keyword args
# greeting = "My name is {myname}, I works at {mywork}"
# print(greeting.format(myname="Noha", mywork=100))
# print(greeting.format( "Valeo", "Test"))  # {0}
# # print(greeting.format("Amr", "Amazon"))
# myname = ""
# mywork = ""
# greeting = "My name is " + myname + "I works at" + mywork

# f-Format
# define string template
name ="Noha"
work = "ITI"
greet = f"my name is {name}, I works at {work}"
print(greet)





