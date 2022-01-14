# name = 'iti'  # globalscope ---> can be read ---> from the global scope, and local scope
#
# # varaibles in global scope can be accessed in the local scope ---> as read
#
#
# def goodmorning():
#     global name
#     name = "AI"   # localscope  variable ---> create new variable
#     # test = 2022
#     print("======== start local scope of good morning function =======")
#     print(f"--- from the local scope ---- {name}")
#     print("======== End local scope of good morning function =======")
#
#
# goodmorning()
# print(f"--- from the global scope ---- {name}")
# # print(test)
########################function inside function ###############3
# year = 2022
#
#
# def getYear():
#     year = 'test'  # localscope
#     print(f"get year {year}")
#     def printyear():
#         global year  # access global variables scope
#         year = 'Abc'
#         print(year)
#
#     printyear()
#
#
# getYear()
# print(year)

#############################################################
# def outefunction():
#     track = 'AI'  # localscope  # this a variable defined in the local scope od the function
#     # outer function
#     print(f"get track {track}")
#     def innerfunction():
#         nonlocal track
#         track = "Artificial intelligence"
#         print(track)
#     innerfunction()
#     print(track)
#
#
# outefunction()

##############################################################
### modify the global variable ----> use keyword global
# x = "Ahmed"
# def outt():
#     x = 10  # localscope
#     def inn():
#         # x = "Day03"  #new variable created in the localscope of the inn() function,,,
#         print(f" called from inn scope {x}")
#         def testfunct():
#             global x
#             x = "Mariam"
#             print(f"called from test scope {x}")
#         testfunct()
#
#     inn()
#     print(x)
#
# outt()
#
# print(x)

####################################
def outt():
    x = 10  # localscope
    def inn():
        x = "Ahmed"
        # x = "Day03"  #new variable created in the localscope of the inn() function,,,
        print(f" called from inn scope {x}")
        def testfunct():
            nonlocal x
            x = "Mariam"
            print(f"called from test scope {x}")
        testfunct()
        print(x)

    inn()
    print(x)

outt()

