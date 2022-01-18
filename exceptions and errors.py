print("Exceptions and errors")

"""
1- sysntax error 
x = 10
print(x
2- logical error
def summnum(x,y):
    print(x*y)

summnum(2,2)
summnum(2,3)

3- runtime , exception 
"""
# eception ---> name x  ---> is not defined
# print(x)
# print("ggggg")
# 'handle exception using try,except block'
#
# print(5/0)
# try:
#     # x = 10
#     print(x)
#     # print(5/0)
# # except NameError as ne:
# #     print(f"Variable not found {ne}")
# except ZeroDivisionError as de:
#     print(f"Division error {de}")
# except Exception as e:  # class ---> Exceptions
#     print(f"Cannot print the variable====> {e}")
# else:
#     print("no exceptions")
# finally:
#     print("The try block is ended")
#
# print("#####################")
'I need to raise exception '
x = input("Plz enter num1 ")
#0
if x.isdigit():
    x = int(x)

# if y.isdigit():
#     y= int(y)
#     if(y==0):
#         raise ZeroDivisionError("Zero here is not accepted")
# while True:
#     y = input("Plz enter num2 ")
#     if y.isdigit():
#         y = int(y)
#         if y!=0:
#             break
# z = x/y



def myfun(x,y):
    if y==0:
        raise ZeroDivisionError("zero not found")
    
    else:
        return x/y

try:
    t=myfun(5,0)
except:
    print("Error")
print(t)