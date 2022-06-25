#Программа выводи последовательность из чисел от 1 до 100 при этом отображает максимальное значение и показывает когда оно было обновлено
import random
N = int()
Greatest = int()
Quantity = int()
while N != 99:
    N += 1
    Random = random.randint(1, 100)
    if Random > Greatest:
        print(Random,'<=== Обновление')
        Quantity += 1
        Greatest = Random
    else:
        print(Random)
print('Количество обновлений максимального значения: ',Quantity)
