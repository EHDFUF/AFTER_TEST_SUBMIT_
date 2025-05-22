inFp = None
inStr = ""

inFp = open("C:\\Users\\LG\\OneDrive\\SUBMIT_\\file_test\\data1.txt", "r", encoding='UTF8')

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()