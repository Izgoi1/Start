#Программа которая условно подбрасывает монетку пока не выпадет три раза подряд одно значение из 10 симуляций бросков. А так же среднее количество подбрасывания монеты.
import random
Random = int()
Check = int()
General = int()
Attempts = int()
for i in range(0, 10):
    print('\n')
    Attempts = 0
    Check = 0
    while Check != 3:
        N = Random
        Random = random.randint(0, 1)
        General += 1
        if Random == 0:
            print('0',end=" ")
            if N == Random:
                Check += 1
            else:
                Check = 0
        if Random == 1:
            print('P',end=" ")
            if N == Random:
                Check += 1
            else:
                Check = 0
        Attempts += 1
print('\nСреднее количество подбрасывания = ',General / 10)


