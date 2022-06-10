#Программа в которой пользователь задает радиус цилиндра и его высоту а в ответ получать объем.
import math
Radius = float(input('Введите радиус: '))
Height = float(input('Введите высоту: '))
Area = math.pi * Radius**2
Volume = Area * Height
print(f'Объём цилиндра равен {Volume:.1f}')