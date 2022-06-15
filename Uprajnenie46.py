# Программа которая запрашивает координаты клетки шахматной доски и выдаёт какого цвета клетка
Letter = str(input('Буква: '))
Number = int(input('Цифра: '))
if Letter == 'a' or Letter == 'c' or Letter == 'e' or Letter == 'g':
    Number %= 2
    if Number == 0:
        print('Клетка белая')
    else:
        print('Клетка чёрная')
else:
    Number %= 2
    if Number == 0:
        print('Клетка чёрная')
    else:
        print('Клетка белая')
