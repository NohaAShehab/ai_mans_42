# try:
#     'mode write ---> check if the file exists will overwrite it (empty)'
#     'if the file is not exists --> will create it ---> if permission allow creating files '
#     wfile= open("names.txt", "w")
# except Exception as e:
#     print(f"{e}")
# else:
#     print("file opened with mode write successfully")
#     'write to file'
#     # write from byte 0
#     # wfile.write("my first text\n")
#     # wfile.seek(10)
#     # wfile.write("python track\n")
#     # wfile.write("ITI\n")
#     # wfile.writelines(["my first line\n", "my second line\n", "my third line\n"])
#     myvar = """jkhjkhf
# kljskljklf
#             kljskldfjsklfj
#             klsdjfkjgkdhjkghjkdghjkdghjksdhkjhsjkdhkhgh
#             kjshfjkhkdjfhjksdfhjhsdjshjkhkjhskjdhfkdjfhkjfhkjhfjkfjkf"""
#     wfile.write(myvar)
#
try:
    'mode append ---> check if the file exists will append on it '
    'if the file is not exists --> will create it ---> if permission allow creating files '
    wfile= open("names.txt", "a")
except Exception as e:
    print(f"{e}")
else:
    print("file opened with mode write successfully")
    'write to file'
    myvar = """$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4this is my new string 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
    # wfile.seek(10) # works with read and write
    wfile.write(myvar)

    wfile.close()
