year = int(input())

if year < 1 or year > 4000:
    result = "잘 못 입력하였습니다."
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        result = 1  # 윤년일 경우
    else:
        result = 0  # 윤년이 아닌 경우

print(result)
