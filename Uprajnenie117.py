#Программа запрашивает у пользователя строку и выводит на экран все составляющие ее слова с удаленными знаками препинания.
def Sorting(Line):
    New = ''
    for i in Line:
        if i == ',' or i == '.' or i == ':' or i == '!' or i == '?' or i == '-':
            continue
        else:
            New += i
    List = New.split(' ')
    return List
def Main():
    Line = input('Введите строку: ')
    List = Sorting(Line)
    print('Все составляющие слова строки:')
    for i in List:
        print(i,end=" ")
if __name__ == '__main__':
    Main()