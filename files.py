

# deal with files ----> formats ,, simple files text, csv files , json files
# read , # write
# file ---
#
# # 1- open file --> specify if the file --> read , wirte
# myfileobj = open("tips.py")  ### open file for read
# # change mode --> file opened with
# # myfileobj = open("tips.py", "r")  # open file for read
# print(myfileobj)
# print(type(myfileobj))  # _io.TextIOWrapper
# print(myfileobj.mode)
# print(myfileobj.closed)  # status of the file --> closed
# ### machine 011104234235523 ---> A , $ ,
# # --- read, write,
# # data = myfileobj.read()  # read all the file in one string
# data = myfileobj.read(100)  # read all the file in one string
# print(data)
# print(len(data))
#
# # close file
# myfileobj.close()  # close file
# print(myfileobj.closed)


################## read
# fileobject = open("read.txt", "r")
#
# # read--- read file into one string
# l = fileobject.read()
# print(l)
# fileobject.seek(0)
# l = fileobject.readline()
# print(l)
#
# fileobject.close()

##### readlines

# fileobject = open("read.txt", "r")
#
# # read--- read file into one string
# l = fileobject.readlines(15)  # read file into a list --> each line is represented by list time
# print(l)
# for myl in l:
#     myl=myl[:-1]
#     print(len(myl))
#     print(myl)
#
# fileobject.close()


##### file
# mydata = open("read.txt")
# for l in mydata:  # itertable
#     print(l)   # retrun line of the file


