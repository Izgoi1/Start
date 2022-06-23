#Программа которая разлаживает целое число на простые множители.
import math
Number = int(input('Введите число: '))
Factor = 2
while Factor <= Number:
    if Number % Factor == 0:
        N = Factor
        Number = math.floor((Number) / Factor)
        print(N)
    else:
        Factor += 1

