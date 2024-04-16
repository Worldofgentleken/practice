x = int(input())
n = int(input())
if (x < 1 or x > 1000000000) or (n < 1 or n > 100):
    print('잘못 입력 하였습니다.')
else:
    for i in range(n):
        a, b = map(int, input().split())
        i = a + b
        sum += i
        