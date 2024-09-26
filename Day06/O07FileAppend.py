
"""
append mode - we can only write data into the file at the end

if the file exists then it will append data into the file without disturbing the old contents. If the file does not exist then creates a new file and writes into the file
"""

FA  = open("myfile.txt", "a")

st = input("Enter the content for the file :")

FA.write(st + "\n")

FA.close()