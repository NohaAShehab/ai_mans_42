# emp1 = {"name": "Ahmed", "email": "a@gmail.com", "dept": "OS"}
#
# emp2 = {"name": "Ali", "email": "ali@gmail.com", "dept": "python"}
#
# emp3 = {"name": "omar", "email": "omar@gmail.com", "dept": "iot"}

# object --> abstract datatype --> that can include different proprerties
# and different methods
# factory, blueprint -->
# class --> create your own dataype ==> contain different properties, methods
# class Employee:
#     # constructor --> init_function
#     # def __init__(self):
#     #     print("this function is called during the object creation and used to inialize the object")
#     #     print(self) # refer to the current instance in the memory
#     #     #name, email, salary
#     #     self.name="iti"
#     #     self.email="iti@gmail.com"
#     #     self.salay=1000
#     #     pass
#     # control object structure using constructor __init__ function
#     # control object attributes values ---> __init__(accept different values from the user))
#     def __init__(self, name, email, salary):
#         print("this function is called during the object creation and used to inialize the object")
#         print(self)  # refer to the current instance in the memory
#         # name, email, salary
#         self.name = name
#         self.email = email
#         self.salay = salary
#         pass
#
#
# # object from class
# print("========== before creating object============")
# e = Employee("noha", "nshehab@iti.gov.eg", 1000)
# print("========== after creating object============")
# print(e)  # Employee object
#
# e2 = Employee("Ali", "ali@gmail.com", 1000)
# print(e2)
#
# e3 = Employee() # typeerror

############################# __init__ function --constructor

# class Employee:
#     # introduce ---> multiple constructors
#     # create object from class with different methods
#     # __init__ ---> function ---> can accept default arguments
#     def __init__(self, name, email="iti@iti.com", salary=1000):
#         # define the attributes or properties of the objects
#         # instance variable
#         self.name = name
#         self.email = email
#         self.salay = salary
#
#     #### define behaviour of the object
#     # instance method ---> affect current --> or current object
#     def speak(self):
#         print(f"I am {self.name}, You can reach me at {self.email}")
#
#
# # create object ---> with different calling style
# e1 = Employee("Ali", "a@gmail.com", 1000)
# # you can access the object proprires objectname.propertyname
# print(e1.name)
# e1.name = "Menna"
# e1.speak()
# print("===================================================")
# e2 = Employee("Ahmed", "Ahmed@gmail.com")  # name ,mail
# print(e2.name)
# e2.speak()
# print("===================================================")
# e = Employee("Esraa")
# print(e.name)
# e.speak()
#
# # print("test")


# def abc(x=1,y=2,z=3):
#     print(f"x={x}, y={y},z = {z}")
#
# abc()
# print("============================")
# abc(10,20)
# print("============================

########################### class varaible, class method #########################################
# class Employee:
#     # class variable ---> doesn't depend on the instance ---> can access it using class name
#     # using classname you change the value of the class variables in all instances from value
#     makefaults = True  # variable shared by all instances from the class
#     # if instance variable is accessed by instance --> to modify it 00> value will be modified in the
#     # caller instance only
#     count_emp = 0
#
#     def __init__(self, name, email="iti@iti.com", salary=1000):
#         self.name = name
#         self.email = email
#         self.salay = salary
#         Employee.count_emp += 1
#         self.id = Employee.count_emp
#
#     def speak(self):
#         print(f"I am {self.name}, You can reach me at {self.email}")
#
#
# print(Employee.makefaults)
# print("==========================obj 1========================")
#
# e1 = Employee("Ali", "a@gmail.com", 1000)
# # e1.speak()
# e1.makefaults = "itiittttttiiiiiii"
# print(e1.makefaults)
# print("==========================obj 2=========================")
# e2 = Employee("Ahmed", "Ahmed@gmail.com")  # name ,mail
# print(e2.makefaults)
# print("=======================obj 3============================")
# e = Employee("Esraa")
# print(e.makefaults)
#
# Employee.makefaults = "iti"
# print("test")
# print(f"No of the employees = {Employee.count_emp}")


########################## class method
class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, email="iti@iti.com", salary=1000):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        self.id = Employee.count_emp

    def speak(self):
        print(f"I am {self.name}, You can reach me at {self.email}")

    # methods to define behaviour --> for all class instances-=> and not depend on single instance
    @classmethod  # decorator
    def mymethod(cls):
        # print(cls) # refers to the class -->
        # can be used with the class varibles
        print(cls.makefaults)
        # class methods are used objects factory
        # return Employee("Mona","mona@gmail.com",4555)  # retrun with new  Employee object
        return cls("Mona", "mona@gmail.com", 4555)  # retrun with new  Employee object

    @classmethod
    def addEmployee(cls,emp1,emp2):
        return cls(f'{emp1.name} {emp2.name}', "mergedmail@gmail.com", emp1.salary+emp2.salary)


print("=================== class methods ===================")
# you can call class method using class name
e1 = Employee.mymethod()
print(e1)
print(Employee.count_emp)

e2= Employee("Ali")


mixed=Employee.addEmployee(e1,e2)
print(mixed)

print("==========================obj 1========================")
e1 = Employee("Ali", "a@gmail.com", 1000)
print("==========================obj 2=========================")
e2 = Employee("Ahmed", "Ahmed@gmail.com")  # name ,mail
print("=======================obj 3============================")
e = Employee("Esraa")
