import os

inFp = None 
fName = ""
inList = []
inStr = ""

fName = input("파일명 입력:")

if os.path.exists(fName):
    inFp = open(fName, "r", encoding="UTF8")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")

    inFp.close()

else:
    print(f"{fName} 파일이 없습니다.")