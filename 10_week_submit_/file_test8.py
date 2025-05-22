inFp, outFp, = None, None 
inStr, outStr = "", ""

index = 0 
secure = 0

secureYN = input("1. 암호화 2. 암호 해석 :")
inFname = input("입력 파일명 입력 : ")
outFname = input("출력 파일명 입력")

if secureYN == "1":
    secure = 100
elif secureYN == "2":
    secure = -100 
    
    
inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break 
    
    outStr = ""
    for i in range(0, len(inStr)):
        ch = inStr[index]
        chNum = ord(ch)
        chNum = chNum + secure
        ch2 = chr(chNum)
        outStr = outStr + ch2 
        
        
    outFp.write(outStr)
    
outFp.close()
inFp.close()
print(f"{inFname} --> {outFname} 변환 완료")  