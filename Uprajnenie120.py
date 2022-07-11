#Функция которая принимает список из строк и возвращает собранную строку из его элементов в следующей манере "яблоки, апельсины, бананы и лимоны".
def Assembly(List):
    Result = ''
    And = ' и '
    Comma = ', '
    if len(List) == 0:
        return 'Пустой список'
    elif len(List) == 1:
        return str(List[0])
    for i in range(0, len(List) - 2):
        Result += str(List[i]) + Comma
    Result += str(List[len(List) - 2]) + And
    Result += str(List[len(List) - 1])
    return Result
def Main():
    List = []
    Line = input('Введите слово (для окончания нажмите "Enter"): ')
    while Line != '':
        List.append(Line)
        Line = input('Введите слово (для окончания нажмите "Enter"): ')
    print('Ваш список: {0}.'.format(Assembly(List)))
Main()