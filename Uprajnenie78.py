#Программа которая запрашивает у пользователя целое число и выводит все числа при помощи гипотезы Коллатца, начиная с веденного числа и заканчивая единицей.
Number = int(input('Введите число: '))
while Number >= 0:
    W = Number
    while Number != 1:
        if W == Number:
            print(W, end=' ')
        if Number % 2 > 0:
           Number = Number * 3 + 1
        elif Number % 2 == 0:
            Number = Number / 2
        print(Number, end=' ')
    Number = int(input('\nВведите число ("Для выхода введите ноль или отрицательное число): '))
