monthly = 100
tax = 0.1
year = monthly * 12
actual = year - (year * tax)
print(f'연봉 : {actual}')