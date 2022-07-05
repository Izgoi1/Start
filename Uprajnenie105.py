#Программа которая переводит число с десятичной системы счисления в произвольную систему в диапазоне от 2 до 16 и наоборот.
from Uprajnenie104 import *
def Dec2r(Number, System):
    Result = ''
    while Number > 0:
        R = Number % System
        Number //= System
        Result += str(Int2hex(R))
    Result = ''.join(reversed(Result))
    return Result
def R2dec(Number, System):
    Number = str(Number)
    N = 0
    Result = 0
    for i in reversed(Number):
        i = int(i)
        R = i * System**N
        Result += R
        N += 1
    return Result
def Main():
    Choice = input('''Нажмите '1' если вы хотите перевести из десятичной системы счисления в любую другую
Нажмите '2' если вы хотите перевести из любой системы счисления в десятичную
: ''')
    if Choice == '1':
        Number = int(input('Введите число: '))
        System = int(input('Введите систему счисления от 2 до 16: '))
        if System < 2 or System > 16:
            return print('Вы вышли за границы допустимого диапазона')
        Res = Dec2r(Number, System)
        print('Результат числа {0} по основанию 10 равняется: {1} по основанию {2}'.format (Number, Res, System))
    elif Choice == '2':
        Number = int(input('Введите число: '))
        System = int(input('Выберите систему счисления от 2 до 16: '))
        if System < 2 or System > 16:
            return print('Вы вышли за границы допустимого диапазона')
        Res = R2dec(Number, System)
        print(f'Результат числа {Number} по основанию {System} равняется: {Res} по основанию 10')
Main()