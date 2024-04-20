# - 다음과 같이 출력 될 수 있도록 산술연산 계산기를 함수를 이용해서 만들어 보자.
# 1. 덧셈, 2. 뺼셈, 3. 곱셈, 4. 나눗셈, 5. 나머지, 6. 몫, 7. 제곱승, 8. 종료      
# 첫 번째 숫자 입력 : 10      
# 두 번째 숫자 입력 : 3.14      
# num1 + num2 = result (8 입력시 bye 출력)

def calculator(n, n1, n2):
    if n == 1:
        print(f'{n1} + {n2} = {n1 + n2}')

    elif n == 2:
        print(f'{n1} - {n2} = {n1 - n2}')

    elif n == 3:
        print(f'{n1} * {n2} = {n1 * n2}')

    elif n == 4:
        print(f'{n1} * {n2} = {n1 / n2}')

    elif n == 5:
        print(f'{n1} * {n2} = {n1 % n2}')

    elif n == 6:
        print(f'{n1} * {n2} = {n1 // n2}')

    elif n == 7:
        print(f'{n1} * {n2} = {n1 ** n2}')

# 테스트
selectNum = int(input('1. 덧셈, 2. 뺼셈, 3. 곱셈, 4. 나눗셈, 5. 나머지, 6. 몫, 7. 제곱승, 8. 종료'))
if selectNum < 8:
    num1 = int(input('첫 번째 숫자 입력 : '))
    num2 = int(input('두 번째 숫자 입력 : '))
    calculator(selectNum, num1, num2)

else:
    print('bye')
