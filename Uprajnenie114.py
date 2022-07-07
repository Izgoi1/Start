#Программа запрашивает у пользователя целые числа пока не будет введина пустая строка. После окончания ввода на экран должны быть выведены все отрицательные
#числа, затем нули и после положительные числа. Числа должны быть в порядке в котором были введены.
Number = input('Введите число: ')
Negative = []
Zero = []
Positive = []
while Number != '':
    Number = int(Number)
    if Number < 0:
        Negative.append(Number)
    elif Number == 0:
        Zero.append(Number)
    else:
        Positive.append(Number)
    Number = input('Введите число (для окончания нажмите "Enter"): ')
print(f'''Отрицательные числа: {Negative}
Нули: {Zero}
Положительные числа: {Positive}''')