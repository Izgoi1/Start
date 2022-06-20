# Программа в которой пользователь вводит координаты многоугольника и программа расчитывает его периметр.
from math import sqrt
Perimeter = float()
First_x = float(input('Введите координату x: '))
First_y = float(input('Введите координату y: '))
x = float(First_x)
y = float(First_y)
Line = input('Введите координату x (Нажмите "Enter" для окончаняи ввода): ')
while Line != '':
    X = float(Line)
    Y = float(input('Введите координату y: '))
    Length = sqrt((x - X) ** 2 + (y - Y) ** 2)
    Perimeter = Perimeter + Length
    x = X
    y = Y
    Line = input('Введите координату x (Нажмите "Enter" для окончаняи ввода): ')
Length = sqrt((First_x - X) ** 2 + (First_y - Y) ** 2)
Perimeter = Perimeter + Length
print('Периметр многоугольника равен', Perimeter)