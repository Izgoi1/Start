#Программа для определния площади комнаты
Length = float(input())
Width = float(input())
Square = Length * Width
if Square % 1 == 0: # Проверка если площадь равна числу без остатка тогда выводиться будет целое число
    Square = int(Square)
print('Площадь комнаты равна =', Square, 'квадратных метров')