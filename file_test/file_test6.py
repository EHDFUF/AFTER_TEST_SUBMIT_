outFp=None
outStr=""

outFp=open("C:\\Users\\LG\\OneDrive\\SUBMIT_\\file_test\\data1.txt", "w")

while True:

    outStr=input("내용입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--정상파일WRITE")