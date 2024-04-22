import pandas as pd
# CCTV 데이터 읽어오기
CCTV_Seoul = pd.read_csv('../data/01. Seoul_CCTV.csv', encoding = 'utf-8')
CCTV_Seoul.head() # head() : 앞부분 5개만 보고 싶어!

CCTV_Seoul.columns

CCTV_Seoul.columns
Index(['순번', '구분', '총 계', '2015년 이전 설치된 CCTV', '2015년', '2016년', '2017년',
       '2018년', '2019년', '2020년', '2021년', '2022년', '2023년'],
      dtype='object')
CCTV_Seoul.columns[0]

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[1] : '구별'}, inplace = True)
CCTV_Seoul.head()

CCTV_Seoul = CCTV_Seoul.drop(['순번'], axis = 1)
CCTV_Seoul.head()

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[2] : '2015년 이전 설치'}, inplace = True)
CCTV_Seoul.head()

# 서울 인구 데이터 읽어오기
pop_Seoul = pd.read_excel('../data/01. Seoul_Population.xlsx')
pop_Seoul.head()
