
FW = open("sample.txt", "w+")

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FW.writelines([l1, l2, l3])

FW.seek(0, 0)
st = FW.read()
print(st)

FW.close()