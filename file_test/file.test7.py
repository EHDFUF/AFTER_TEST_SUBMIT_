inFp, outFp = None, None
inStr = ""

inFp = open("C:\\windows\\win.ini", "r")
outFp = open("C:\\temp\\data1.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("파일복사완료")
