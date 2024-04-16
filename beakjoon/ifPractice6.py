a, b = map(int, input().split())
c = int(input())

if (a < 0 or a > 23) or (b < 0 or b > 59) or (c < 0 or c > 1000):
    result = '잘 못 입력하였습니다.'
else:
    total_minutes = b + c
    hours_to_add = total_minutes // 60
    minutes_after_addition = total_minutes % 60
    a = (a + hours_to_add) % 24 
    result = f'{a} {minutes_after_addition}'

print(result)