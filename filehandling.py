print("###########################################")
'python support writing and reading on the files'
"""
To deal with file 
1- open file  ---> specify --You want to are opening the file for read or write or append 
2- read or write from the file
3- close file
"""

#open file
# fileobj = open("myfile.txt", 'r')  # file mode , ===> 'r', 'w', 'a'
try:
    fileobj = open("myfile.txt")
except Exception as e:
    print(f"{e}")
else:
    # print(fileobj)
    print(fileobj.mode)  #attribute
    # print(fileobj.name)
    # print(type(fileobj))
    if fileobj.mode =='r':
        # read data from the file
        # # read all file content into one string
        # data = fileobj.read()
        # print(type(data))
        # print(data)

        # read file content line by line into list
        # filelines = fileobj.readlines()
        # print(type(filelines))
        # print(filelines)

        ### read part from the file
        # partt = fileobj.read(10)  # read 10 bytes
        # print(partt)

        # read file content line by line into list
        # filelines = fileobj.readlines(10)
        # print(type(filelines))
        # print(filelines)

        # read line
        # line = fileobj.readline() # read line by line
        # print(line)
        # line = fileobj.readline()
        # print(line)
        # line = fileobj.readline()
        # print(line)

        # check this
        # data = fileobj.read()  # read all data into string
        # print(f"file content is {data}")
        # fileobj.seek(30)
        # line = fileobj.readline()
        # print(f"line content is {line}")

        # loop over file lines
        for l in fileobj:  # line 
            print(l)





    #close file
    fileobj.close()