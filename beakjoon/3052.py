num_list = []
for i in range(10):
    a = int(input())
    num_list.append(a)

rest = []
for j in range(10):
    b = num_list[j] % 42
    rest.append(b)

rest_dif = set(rest)
print(len(rest_dif))
