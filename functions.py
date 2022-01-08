# def myfunction():
#     return
#
# x = myfunction()  # return nothing ---> return None object
# print(type(x), x)


# accept parameters
# def myfunction(x):
#     print(f"Hello World: {x}")
#     return
#
# x = myfunction("Python")  # return nothing ---> return None object
# print(type(x), x)


# def myfunction(x, y):
#     print(f"Hello World: {x}")
#     return x, y   # return inform of tuple
#
#
# # x is the return
# x = myfunction("Python", 10)  # return nothing ---> return None object
# print(type(x), x)
#
# z = myfunction(True, ["ttt", "ggg"])
# print(z)

# overlaoding --->  default arguments or default parameters
# no need to define the data type
# non default argument should be before default arguments
# def myfunction(x=100, m=100):
#     print(f"Hello World: x= {x},  y={m}")
#     return x, m  # return inform of tuple

# myfunction()
# myfunction(10)
# myfunction(10, "python")
# myfunction(m="salma", x="Noha") # keyword ar
# myfunction(,200)
###############################################3
# number of args are unknown
# def myfunction(x=10,*abbas): # *args
#     # zero or more attributes
#     print(f"x = {x}")
#     print(abbas)
#     print("--------------------")
#     return  # return inform of tuple
#
# myfunction()
# myfunction(44)
# myfunction(x=[34,55,6], True,"Mariam")

"-------------------"


# unknow keywords, unknown number of elements
# allow user to call it using different keywords and values.
def myinfo(**abbas):  # zero or more
    print(abbas)
    print("--------------------")
    return  # return inform of tuple


myinfo(name="Noha", track="AI")
myinfo(username="Salma", Faculty="FCI", dept="AI")
myinfo()
