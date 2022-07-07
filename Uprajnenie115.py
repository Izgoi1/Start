#Функция которая возвращает список всех собственных делителей заданного числа.
def Dividers(Number):
    Result = []
    for i in range(1, Number):
        if Number % i == 0:
            Result.append(i)
    return Result
def Main():
    Number = int(input('Введите число: '))
    Result = Dividers(Number)
    print('Список собственных делителей от числа', Number)
    for i in Result:
        print(i,end=', ')
if __name__ == '__main__':
    Main()