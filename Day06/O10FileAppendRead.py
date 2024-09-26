

FW = open("sample.txt", "a+")

l1 = "This is the fourth line.\n"
l2 = "This is the fifth line.\n"


FW.writelines([l1, l2])

FW.seek(0, 0)
st = FW.read()
print(st)

FW.close()