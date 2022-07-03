#Функция принимает число и выдаёт первое простое число которое больше введенного числа. Так же для основной программы нужно импортировать функцию из упражнение 98.
from Uprajnenie98 import PrimeNumber
def nextPrime(Number):
    while PrimeNumber(Number) != True:
        if PrimeNumber(Number) == False:
            Number += 1
    return Number

def Start():
    Number = int(input('Введите целое число: '))
    nextPrime(Number)
    if Number < nextPrime(Number):
        print('Ближайшее простое число от {0} является {1}'.format(Number, nextPrime(Number)))
    elif Number == nextPrime(Number):
        print(Number, '- является простым числом')

Start()