#Функция для определения является ли заданное число совершенным. Совершенным числом считается если сумма всех его делителей равна самому числу.
#Программа должна вывести на экран все совершенные числа в диапазоне от 1 до 10000.
from Uprajnenie115 import Dividers
def PerfectNumber(Number):
    Result = Dividers(Number)
    Perfect = 0
    for i in Result:
        Perfect += i
    if Perfect == Number:
        return True
    else:
        return False
def Main():
    for i in range(1, 10000):
        Result = PerfectNumber(i)
        if Result == True:
            print(i,'является совершенным числом')
Main()
