#Функция определяет представляет ли введенная строка целочисленное значение.
def isInteger(Line):
    Line = Line.strip()
    if (Line[0] == '+' or Line[0] == '-') and Line[1].isdigit() == True:
        print('Да, это целочисленная строка')
    elif Line.isdigit() == True:
        print('Да, это целочисленная строка')
    elif Line.isdigit() == False:
        print('Нет, это не целочисленная строка')
def Start():
    Line = input('Введите число: ')
    isInteger(Line)

if __name__ == '__main__':
    Start()