"""
opening the file in read mode which is the default mode, when we open the file in read mode we can only read the contents of the file
"""
FL = open("data.txt", "r")

# st = FL.read(1000)
# st = FL.readline(500)

st = FL.readlines(853)
print(st)

# for line in st:
#     print(line)


FL.close()