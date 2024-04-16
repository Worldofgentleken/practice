h, m = map(int, input().split())
if (h < 0 or h > 23 ) or (m < 0 or m > 59):
    result = '잘 못 입력하였습니다.'
else:
    if m - 45 < 0:
        h -= 1
        m = 60 + (m - 45)
        if h < 0:
            h = 23       

    else:
        m -= 45
    result = f"{h} {m}"
print(result)

