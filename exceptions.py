# error
# 1- syntax error

# print(x

# 2- logical error
print("The sum of 3 ,4 = ", 3*4)
# 3- runtime error  ---> exception
# print(x)  # Name , runtime

'Exception: event which occurs during execution, ' \
'distrub the normal flow of the application, and the program stop working'
############ Exception handling
# try, except block
'open file ---> file not exists'
#
# # x = open("test.ffff")  #exeption ---> FileNotFoundError
# # 'connect to the database'
# m =10
# # print(m)
# # x = open("test3.txt")
# # x = [3,5,6]
# # print(x[10])
# try:
#     x = open("test.txt")  # get object --> refer to the file
#     print(m)
# except Exception as n:
#     print("This name is not found|||", n)
# except FileNotFoundError as f:
#     print("This is an exception", f)
# except NameError as e:
#     print("Error msg:", e)
# else:
#     # will be executed when the script in the try block executed sucessfully
#     data = x.read()
#     print(data)
# finally:
#     print("This line will be called always")
#
# # exception ---> object from class exceptions
# # raise

# print("Hello world")

'application allow some behaviours '

x =int(input("Enter num1: "))
y = int(input("Enter num2: "))
if y == 5:
    raise ZeroDivisionError("5 is not available her")
else:
    z = x /y  # ZeroDivisionError
    print(z)

print('tessssssssssst')

print(xx)