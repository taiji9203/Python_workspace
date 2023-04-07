#95점 이상: A+, 90점 이상: A0, 85점 이상: B+, 80점 이상: B0, 
#75점 이상: C+, 70점 이상: C0, 65점 이상: D+, 60점 이상: D0, 60점 미만: F
score = int(input("점수를 입력하세요 : "))

if score >= 95 :
    print("A+")
elif score >= 90 :
    print("A0")
elif score >= 85 :
    print("B+")
elif score >= 80 :
    print("B0")
elif score >= 75 :
    print("C+")
elif score >= 70 :
    print("C0")
elif score >= 65 :
    print("D+")
elif score >= 60 :
    print("D0")
else :
    print("F")

print("학점입니다. ^^")

# 딕셔너리를 사용한 코드
# score = int(input("점수를 입력하세요 : "))

# grades = {
#     "A+": 95,
#     "A0": 90,
#     "B+": 85,
#     "B0": 80,
#     "C+": 75,
#     "C0": 70,
#     "D+": 65,
#     "D0": 60,
#     "F": 0
# }

# for grade, min_score in grades.items():
#     if score >= min_score:
#         print(grade)
#         break

# print("학점입니다. ^^")
