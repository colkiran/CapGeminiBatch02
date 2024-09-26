"""
first we can read the contents of the file
"""

# read and write mode

FL = open("sample.txt", "r+")

st = FL.read(23)
print(st)

FL.write("This is the new line.\n")

FL.close()