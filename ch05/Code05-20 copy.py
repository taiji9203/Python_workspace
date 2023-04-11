inFp = None 
inList, inStr = [], ""
lineNum = 1

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
# 각 문자열 앞에 줄 번호를 붙여서 출력

#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print("%d : %s" %(lineNum, inStr), end = "")
    lineNum += 1

inFp.close()
