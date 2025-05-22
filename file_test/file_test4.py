inFp = None
inStr = ""

inFp = open("C:\\Users\\LG\\OneDrive\\SUBMIT_\\file_test\\data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()