# 유니코드 표를  참고해서
# 한글의 유니코드 범위, AC00-D7AF, 음절: 44032 (u+ac00) ~ 55203 (u+d7af
# 숫자의 유니코드 범위,
# 영어의 대소문장 유니코드 범위,
# 특수문자의 유니코드 범위,
# 숫자의 유니코드 범위,
# 
a = ord("상")
if a >= 44032 and a <= 55215:
    print("한글 입니다.")
    
print(a)