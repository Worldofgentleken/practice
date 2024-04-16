a = int(input())
if a < 1 or a > 9:
  print('잘 못 입력하였습니다.')
else:
  for j in range(1,10):
      print(f'{a} * {j} = {a*j}')