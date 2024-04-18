#QUIZ#8
#함수 - 369 게임¶
#다음은 369게임입니다. 369게임은 다음과 같습니다.
#1부터 시작해 숫자를 하나씩 센다.
#숫자에 3이나 6이나 9 배수일 경우 박수(clap)를 친다.
#지정한 최대 숫자까지 도달하면 프로그램을 종료한다
def game(n):
    for i in range(1, n + 1):
        count = 0
        for j in str(i):
            if j in ['3', '6', '9']:
                count += 1
        if count > 0:
            print('clap')
        else:
            print(i)
          
#QUIZ#9
#점수 채점하기
#총 12명의 레벨테스트 점수가 파이썬의 리스트(List)로 담겨져 있고,
#이를 score라는 이름의 변수에 할당하였습니다.
#score = [80, 60, 70, 50, 100, 95, 40, 75, 90, 65, 90, 100]
#이 score 변수에 담겨져 있는 값을 활용하여 아래 문제를 풀어보세요.
#1.전체 점수의 평균을 구하는 코드를 작성해보세요.
#2.전체 점수 중 가장 높은 점수를 구하는 코드를 작성해보세요.
#3.전체 점수 중 가장 낮은 점수를 구하는 코드를 작성해보세요.
score = [80, 60, 70, 50, 100, 95, 40, 75, 90, 65, 90, 100]
#1
import pandas as pd
pd.DataFrame(score).mean()
total = sum(score)
avg = total/len(score)
print(avg)
#2
print(max(score))

#3
print(min(score))

#QUIZ10
#레벨 3 문제
#다음과 같은 형태의 배열을
#> [a1,a2,a3...,an,b1,b2...bn]
#다음과 같은 형태로 바꾸시오
#> [a1,b1,a2,b2.....an,bn]
#( 문제 원문을 보니 should be in-place라 되어 있네요. )
#입력을 저장하는 저장소 이외에 추가적인 저장장소를 사용치 않는다는게 제약조건입니다.
def rearr(arr):
    n = len(arr) // 2 
    for i in range(n):
        arr.insert(i * 2 + 1, arr.pop(n + i))
#테스트
arr = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5']
rearr(arr)
print(arr)
