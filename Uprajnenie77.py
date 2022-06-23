#Таблица умножения
N = int()
while N != 10:
    N += 1
    for i in range(1, 11):
        Answer = N * i
        print('  ',Answer, end=' ')
        if i == 10:
            print(end='\n')