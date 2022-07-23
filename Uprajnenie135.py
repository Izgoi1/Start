#Программа которая реализует алгортим Решето Эратосфена и выводит все простые числа от 2 до указанного значения.
Number = 1000000
List = list(range(0, Number+1))
List[1] = 0
p = 2
while p < Number:
    for i in range(p * 2, Number+1, p):
        List[i] = 0
    p += 1
    while p < Number and p == 0:
        p += 1

for i in List:
    if i != 0:
        print(i)