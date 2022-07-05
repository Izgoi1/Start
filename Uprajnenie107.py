#Функция принимает два целых числа представляющих числитель и знаменатель дроби затем выводит на экран максимальное сокращение дроби.
def Divisor(Numerator, Denominator):
    D = min(Numerator, Denominator)
    while Numerator % D != 0 or Denominator % D != 0:
        D -= 1
    return D
def Devision(Numerator, Denominator, Divisor):
    Numerator = Numerator / Divisor
    Denominator = Denominator / Divisor
    return int(Numerator), int(Denominator)
def Main():
    Numerator = int(input('Введите числитель: '))
    Denominator = int(input('Введите знаменатель: '))
    D = Divisor(Numerator, Denominator)
    B = Devision(Numerator, Denominator, D)
    print('Результат максимального сокращения дроби:', B)
Main()