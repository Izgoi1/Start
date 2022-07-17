#Программа которая определяет отсортирован ли список изначально по возрастанию или убыванию. Функция принимает список и возвращает
# значение True если список отсортирован и False если нет.
def SortList(List):
    Sort = List.copy()
    Sortreverse = List.copy()
    Sort.sort()
    Sortreverse.sort()
    Sortreverse.reverse()
    if len(List) <= 1:
        return False
    elif Sort == List or List == Sortreverse:
        return True
    else:
        return False
def Main():
    List = []
    Number = int(input('Введите число: '))
    while Number != '':
        Number = int(Number)
        List.append(Number)
        Number = input('Введите число (для оконочания нажмите "Enter"): ')
    TrueFalse = SortList(List)
    if TrueFalse:
        print('Да, список отсортирован')
    else:
        print('Список не отсортирован или его длина меньше одно элемента')
Main()