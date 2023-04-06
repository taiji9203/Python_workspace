## 변수 선언 부분 ##
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
select = int(input("1. 두숫자 사이의 합계(단 1씩증가 하지 않고 증가하는 숫자도 입력)"))

if  select == 1 :
    num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    num3 = int(input(" *** 더 할 숫자를 입력하세요 : "))
    for i in range(num1, num2+1, num3) :
        answer = answer + i
    print("%d+...+%d는 %d입니다. " %(num1, num2, answer))

else :
    print("1 또는 2만 입력해야 합니다.")
