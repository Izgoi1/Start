#Программа которая случайным образом подбирает шесть чисел от 1 до 49 для лотерейного билета.
import random
List = []
Min = 1
Max = 49
Len = 6
while len(List) != Len:
    Random = random.randint(Min, Max)
    if Random in List:
        continue
    else:
        List.append(Random)
List.sort()
print('Ваше лотерейный билет: ',end=' ')
for i in List:
    print(i, end=' ')