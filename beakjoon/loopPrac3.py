n = int(input())
if n < 1 or n > 10000:
    print('잘 못 입력하였습니다')
else:
    for i in range(n):
        i += 1
    print(i)