import random

## 전역 변수 선언 부분 ##
imageList = []
value = 0
ROW = COL = 3
tt = ((1,2,3),(4,5,6),(7,8,9))

## 메인 코드 부분 ##
if __name__ == "__main__" :
    for i in range(0, ROW) :
        tmpList = []  # 임시 1차원 배열
        for k in range(0, COL) :
            value = random.randrange(0, 10)
            tmpList.append(value)
        imageList.append(tmpList)

    print('## 원본 2차원 배열 ##')
    for i in range(0, ROW) :
        for k in range(0, COL) :
            print("%1d" % imageList[i][k], end = " ")
        print("")
    print("")

 
