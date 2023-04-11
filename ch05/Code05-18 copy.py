inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

num = 1
while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d : %s" %(inStr), end = "")
    num += 1

inFp.close()
