## 함수 선언 부분 ##
def calc(v1, v2, op) :
     result = 0
     if op == '+' :
          result = v1 + v2
     elif op == '-' :
          result = v1 - v2
     elif op == '*' :
          result = v1 * v2
     elif op == '/' :
          result = v1 / v2
     elif op == '**' :
          result = v1 ** v2
	
     return result

## 전역 변수 선언 부분 ##
res = 0
var1, var2, oper = 0, 0, ""

# 0으로 나누려고 하면 메시지를 출력하고 계산되지 않도록 한다.


## 메인 코드 부분 ##

var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+, -, *, /, **) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))
if (oper == '/' and var2 == 0) :
          print("0으로 나눌 수 없습니다.")
          exit()
else :
      res = calc(var1, oper, var2)

print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))


