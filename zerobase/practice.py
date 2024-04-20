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

# 다음과 같이 출력될 수 있도록 이동거리와 이동시간을 반환하는 함수를 만들어보자.
# ------------------------------------------------------------
# 속도(km/h) 입력 : 90
# 시간(h) 입력 : 2
# 시간(m) 입력 : 45
# 90.0(km/h)속도로 2.0(h)시간 45.0(m)분 동안 이동한 거리 : 247.5(km))
# ------------------------------------------------------------

def getDist(speed, hour, min):
    result = (speed/60)*(60*hour + min)
    return result

print('-' * 60)
s = float(input('속도(km/h) 입력 : '))
h = float(input('시간(h) 입력 : '))
m = float(input('시간(m) 입력 : '))
d = getDist(s, h, m)
print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리 : {d}(km)')
print('-' * 60)


#------------------------------------------------------------
#속도(km/h) 입력 :  90
#거리(km) 입력 :  247.5
#90.0(km/h)속도로 247.5(km) 이동한 시간 : 2(h)시간 45(m)분
#------------------------------------------------------------

def getTime(speed, dist):
    h = int(dist // speed)
    m = int((dist/speed - dist//speed)*60)
    return [h, m]

print('-' * 60)
s = float(input('속도(km/h) 입력 : '))
d = float(input('거리(km) 입력 : '))
t = getTime(s, d)
print(f'{s}(km/h)속도로 {d}(km) 이동한 시간 : {t[0]}(h)시간 {t[1]}(m)분')
print('-' * 60)
