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

# 다음과 같이 출력 될 수 있도록 비행기 티켓 영수증 출력 함수를 만들어 보자
# childPrice(24개월 미만) : 18,000원
# infrantPrice(만 12세 미만) : 25,000원
# adaltPrice(만 12세 이후) : 50,000원
# 국가 유공자 및 장애우 할인 : 50%

# 유아 입력 : 1
# 할인대상 유아 입력 : 1
# 소아 입력 : 2
# 할인대상 소아 입력 : 1
# 성인 입력 : 2
# 할인대상 성인 입력 : 0

# 출력
# ====================================
# 유아 1명 요금 : 18,000원
# 유아 할인 대상 1명 요금 : 9,000원
# 소아 2명 요금 : 50,000원
# 소아 할인 대상 1명 요금 : 12,500원
# 성인 2명 요금 : 100,000원
# 성인 할인 대상 0명 요금 : 0원
# ====================================
# Total : 7명
# TotalPrice : 189,500원
# ====================================

#함수
def childPrice(c1, c2):
    childDiscPrice = 0
    childBasicTotal = 18000 * c1
    if c1 >= 1 and 1 <= c2 <= c1:
        childDiscPrice = 18000 * c2 * 0.5
    childTotalPrice = childBasicTotal + childDiscPrice
        
    return [childBasicTotal, childDiscPrice, childTotalPrice]

def infrantPrice(i1, i2):
    infrantDiscPrice = 0
    infrantBasicTotal = 25000 * i1
    if i1 >= 1 and 1 <= i2 <= i1:
        infrantDiscPrice = 25000 * i2 * 0.5
    infrantTotalPrice = infrantBasicTotal + infrantDiscPrice
        
    return [infrantBasicTotal, infrantDiscPrice, infrantTotalPrice]

def adultPrice(a1, a2):
    adultDiscPrice = 0
    adultBasicTotal = 50000 * a1
    if a1 >= 1 and 1 <= a2 <= a1:
        adultDiscPrice = 50000 * a2 * 0.5
    adultTotalPrice = adultBasicTotal + adultDiscPrice

    return [adultBasicTotal, adultDiscPrice, adultTotalPrice]

#입력
child = int(input('유아 입력 : '))
childDisc = int(input('할인대상 유아 입력 : '))
infrant = int(input('소아 입력 : '))
infrantDisc = int(input('할인대상 소아 입력 : '))
adult = int(input('성인 입력 : '))
adultDisc = int(input('할인대상 성인 입력 : '))

#변수 설정
ctp = childPrice(child, childDisc)
itp = infrantPrice(infrant, infrantDisc)
atp = adultPrice(adult, adultDisc)
totalCustomer = child + infrant + adult
totalPrice = atp[2] + itp[2] + ctp[2]

#출력
print('='*40)
print(f'유아 {child}명 요금 : {int(ctp[0]):,}원')
print(f'유아 할인 대상 {childDisc}명 요금 : {int(ctp[1]):,}원')
print(f'소아 {infant}명 요금 : {itp[0]:,}원')
print(f'소아 할인대상 {infantDisc}명 요금 : {int(itp[1]):,}원')
print(f'성인 {adult}명 요금 : {atp[0]:,}원')
print(f'성인 할인대상 {adultDisc}명 요금 : {int(atp[1]):,}원')
print('='*40)
print(f'Total : {totalCustomer}명')
print(f'TotalPrice : {int(totalPrice):,}원')

# 다음과 같이 출력될 수 있도록 재귀함수를 이용해서 팩토리얼 함수를 만들어보자
# 출력
# input number : 5
# 120

def myself(n1):
    if n1 == 1:
        return 1
    else:
        return n1*myself(n1-1)

n = int(input('input number : '))
myself(n)


# 다음과 같이 출력 될 수 있도록 단리/월복리 게산기 함수를 만들어보자.
# 입력
# 예치금(원) : 10000000
# 기간(년) : 3
# 연 이율(%) : 3
# [단리 계산기]
# ==============================
# 예치금 : 10,000,000원
# 예치기간 : 3년
# 연 이율 : 3%
# ------------------------------
# 3년 후 총 수령액 : 10,900,000원
# ==============================

# [월복리 계산기]
# ==============================
# 예치금 : 10,000,000원
# 예치기간 : 3년
# 연 이율 : 3%
# ------------------------------
# 3년 후 총 수령액 : 10,940,514원
# ==============================

# 함수
def interestCalculator(b, y, r):
    simpleInterest = b + b*r/100*3
    monthly_rate = r / 100 / 12
    compoundInterst = b * (1 + monthly_rate) ** (12*y)
    return [simpleInterest, compoundInterst]

# 입력
base = int(input('예치금(원): '))
year = int(input('기간(년): '))
rate = int(input('연 이율(%): '))

# 실행
ic = interestCalculator(base, year, rate)

# 출력
print('[단리 계산기]')
print('='*30)
print(f'예치금 : {base:,}원')
print(f'예치기간 : {year}년')
print(f'연 이율 : {rate}%')
print('-'*30)
print(f'3년 후 총 수령액 : {int(ic[0]):,}원')
print('='*30)
print('')
print('[월복리 계산기]')
print('='*30)
print(f'예치금 : {base:,}원')
print(f'예치기간 : {year}년')
print(f'연 이율 : {rate}%')
print('-'*30)
print(f'3년 후 총 수령액 : {int(ic[1]):,}원')
print('='*30)


# 다음과 같이 출력 될 수 있도록 등차 수열의 n번쨰 값과 합을 출력하는 함수를 만들어 보자.
# a1 입력 : 2
# 공차 입력 : 3
# n 입력 : 7
# 1번째 항의 값 : 2
# 1번쨰 항까지의 합 : 2
# 2번째 항의 값 : 5
# 2번째 항까지의 합 : 7
# 3번째 항의 값 : 8
# 3번째 항까지의 합 : 15
# 4번째 항의 값 : 11
# 4번째 항까지의 합 : 26
# 5번째 항의 값 : 14
# 5번째 항까지의 합 : 40
# 6번째 항의 값 : 17
# 6번째 항까지의 합 : 57
# 7번째 항의 값 : 20
# 7번째 항까지의 합 : 77

# 함수
def numList(n1, n2, n3):
    n1_List = []
    for i in range(1, n3 + 1):
        i = n1 + (i - 1)*n2
        n1_List.append(i)
    
    for j in range(n3):
        print(f'{j+1}번째 항의 값 : {n1_List[j]}')
        print(f'{j+1}번째 항까지의 합 : {sum(n1_List[:j+1])}')

# 입력
a1 = int(input('a1 입력 : '))
b1 = int(input('공차 입력 : '))
n = int(input('n 입력 : '))

# 실행
result = numList(a1, b1, n)
result


# 다음과 같이 출력 될 수 있도록 등비 수열의 n번째 값과 합을 출력하는 함수를 만들어 보자.
# a1 입력 : 2
# 공비 입력 : 3
# n 입력 : 5
# 1번째 항의 값 : 2
# 1번째 항까지의 합 : 2
# 2번째 항의 값 : 6
# 2번째 항까지의 합 : 8
# 3번째 항의 값 : 18
# 3번째 항까지의 합 : 26
# 4번째 항의 값 : 54
# 4번째 항까지의 합 : 80
# 5번째 항의 값 : 162
# 5번째 항까지의 합 : 242

# 함수
def sequenceCel(a, b, c):
    i = 1
    sumN = 0
    while i <= c:
        if i == 1:
            valueN = a
            sumN += valueN
            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sumN}')
    
            i += 1
            continue
    
        valueN *= b
        sumN += valueN
        print(f'{i}번째 항의 값 : {valueN}')
        print(f'{i}번째 항까지의 합 : {sumN}')
        i += 1

# 입력
a1 = int(input('a1 입력 : '))
b1 = int(input('공비 입력 : '))
n = int(input('n 입력 : '))

# 실행
sequenceCel(a1,b1,n)
