#Программа из двух функций. Функция "Hex2int" принимает значение с единственным символом шестнадцатеричной системе счисления
#и переводит в десятичную систему от 0 до 15.
def Hex2int(Number):
    Result = 0
    if Number.isalpha == True:
        Number = Number.upper()
    if '0' <= Number <= '9':
        Result = Number
    elif Number == 'A':
        Result = 10
    elif Number == 'B':
        Result = 11
    elif Number == 'C':
        Result = 12
    elif Number == 'D':
        Result = 13
    elif Number == 'E':
        Result = 14
    elif Number == 'F':
        Result = 15
    else:
        print('Ошибка, введенное значение выходит за допустимые границы.')
    return Result
def Int2hex(Number):
    Number = int(Number)
    Result = 0
    if 0 <= Number <= 9:
        Result = Number
    elif Number == 10:
        Result = 'A'
    elif Number == 11:
        Result = 'B'
    elif Number == 12:
        Result = 'C'
    elif Number == 13:
        Result = 'D'
    elif Number == 14:
        Result = 'E'
    elif Number == 15:
        Result = 'F'
    else:
        print('Ошибка, введенное значение выходит за допустимые границы.')
    return Result

def Main():
    Number = input('Введите значение в шестнадцатеричной системе счисления: ')
    Result = Hex2int(Number)
    Result2 = Int2hex(Result)
    print('Число {1} из шестадцатеричной системы в десятичной равняется {0}'.format(Result, Result2))
if __name__ == '__main__':
    Main()