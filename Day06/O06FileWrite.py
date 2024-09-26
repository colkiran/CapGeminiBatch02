"""
write mode - we can only write data into the file
if the file exists then it will delete the contents of the file and strart writing newly into the file. If the file does not exist then creates a new file and writes into the file
"""

FW = open("myfile.txt", "w")
# txt = input("Enter the content of the file :")
# FW.write(txt)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FW.writelines([l1, l2, l3])

FW.close()