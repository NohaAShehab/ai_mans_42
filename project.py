### entry point
def login():
    pass


def register():
    firstname = input("Enter firstname ")
    lastname = input("Enter lastname ")
    info = ":".join([firstname,lastname])
    print(info)
    pass


def mainMenu():
    while True:
        option = input("Please choose l for login, r for registeration")
        if option == "l" or option == 'r':
            break

    if option == "l":
        login()

    else:
        register()



mainMenu()