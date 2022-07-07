#Программа состоящая из функции создающая копию списка с исключенными из него n наибольшими и наименьшими значениями и возвращающую ее в качестве результата.
def Sortlist(List, N = 1):
    List.sort()
    for i in range(N):
        List.pop(0)
        List.pop()
    return List
def Main():
    Number = int(input('Введите целое число: '))
    List = []
    while Number != 0:
        List.append(Number)
        Number = int(input('Введите целое число (для выхода введите "0") : '))
    Newlist = List.copy()
    Sortlist(Newlist, 2)
    if len(List) < 3:
        print('Ошибка, в списке меньше 4 чисел')
        quit()
    else:
        print('Оригинальный список: ',List)
        print('Измененный списко: ', Newlist)
Main()