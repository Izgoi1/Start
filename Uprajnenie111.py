#Программа которая запрашивает у пользователя целочисленные значения сохраняет их в виде списка затем программа выводит числа в порядке убывания.
List = []
Number = int(input('Введите число: '))
while Number != 0:
    List.append(Number)
    Number = int(input('Введите число (для выхода введите "0"): '))
List.sort()
for i in reversed(List):
    print(i,end=', ')