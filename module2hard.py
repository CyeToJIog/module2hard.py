n = int(input('Первое число: '))
result = ''

for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0:
            if str(j) == str(i):
                continue
            result = result + str(i) + str(j)

print('Пароль: ', result)
