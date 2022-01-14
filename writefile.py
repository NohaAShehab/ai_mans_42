
# ### open file for wirte
# myfile = open("test.txt", "w")# create it
# # check if the file not exists ---> will create it
# # delete content, overwrite
# # do operation
# myfile.write("Good jfjkdhk\n")
# myfile.write("ijerlkerj\n")
# myfile.write("Adding new line\n")
# myfile.writelines(["test\n","abc\n", "Line x\n"])
# # close file
# myfile.close()



### open file for wirte
myfile = open("abc.txt", "a")# create it
# check if the file not exists ---> will create it
# delete content, overwrite
# do operation
myfile.write("#######################################\n")
print(len('#######################################\n'))
print(len("good morning"))
myfile.seek(10)
myfile.write("good morning")
# myfile.write("Good jfjkdhk\n")
# myfile.write("ijerlkerj\n")
# myfile.write("Adding new line\n")
# myfile.writelines(["test\n","abc\n", "Line x\n"])
# close file
myfile.close()

myf = open("abc.txt")
print(len(myf.read()))
myf.close()