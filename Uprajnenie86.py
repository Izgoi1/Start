#Программа которая вычисляет длину гипотенузу по теореме Пифагора с использованием функции.
import math
def Find_hypotenuse():
    Adjacent1 = float(input('Первый катет: '))
    Adjacent2 = float(input('Второй катет: '))
    Hypotenuse = math.sqrt(Adjacent1**2 + Adjacent2**2)
    print('Гипотенуза равна %.2f'% Hypotenuse)
Find_hypotenuse()