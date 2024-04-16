x = int(input())
y = int(input())
if (1000 < x, y < -1000) and x == 0 and y == 0:
    result = '잘 못 입력 하였습니다.'
else:
    if (-1000 <= x, y <= 1000 and x != 0):
        if 0 < x and 0 < y:
            result = 1
        elif x < 0 and y > 0:
            result = 2
        elif x < 0 and y < 0:
            result = 3
        else:
            result = 4
print(result)
        