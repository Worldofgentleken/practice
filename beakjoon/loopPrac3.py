n = int(input())
sum = 0
if n < 1 or n > 10000:
    print('잘 못 입력하였습니다')
else:
    for i in range(1,n+1):
      sum += i
    print(sum)