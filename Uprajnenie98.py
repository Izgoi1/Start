#Функция для определения того, является ли введенное число простым. Возвращаемое значение должно быть True или False.
def PrimeNumber(Number):
    if Number <= 1:
        return False
    elif Number == 2 or Number == 3:
        return True
    elif Number % Number == 0 and Number % 2 != 0 and Number % 3 != 0:
        return True
    elif Number % Number == 0 and Number % 2 == 0 or Number % 3 == 0:
        return False

def Start():
    Number = int(input('Введите целое число: '))
    if PrimeNumber(Number):
        print(Number, '- простое число')
    else:
        print(Number, '- не является простым числом')

if __name__ == '__main__':
    Start()
