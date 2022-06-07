# Программа которая запращивает два целых числа и производит с ними математические операции.
import math
A = int(input('Первое число: '))
B = int(input('Второе числа: '))
Sum = A + B
Difference = A - B
Multiplication = A * B
Division = A / B
Remainder = math.fmod(A, B)
Log10 = math.log10(A)
Degree = A**B
print(f'''Сумма A и B = {Sum}
Разница между A и B = {abs(Difference)}
Произведение числе A и B = {Multiplication}
Частное от деления A на B = {Division:.2f}
Остаток от деления A на B = {Remainder}
Десятичный логарифм числа A = {Log10:.2f}
Резуьтат возведения числа A в степень B = {Degree}
''')
