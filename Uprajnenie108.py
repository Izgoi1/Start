#Программа которая выражает заданный объем ингридиентов с использованием минимальных возможных замеров.
#Программа принимает количество единиц измерения а так же их тип(стакан, столовая ложка и чайная ложка).
def Teaspoons(Quantity):
    Result = Quantity % 3
    return Result
def Tablespoons(Quantity):
    Quantity = Quantity // 3
    Result = Quantity % 16
    return Result
def Cup(Quantity):
    Quantity = Quantity // 3
    Result = Quantity // 16
    return Result
def Main():
    Type = input('Выберите тип единиц измерения(1- чайная ложка, 2 - столовая, 3 - стакан: ')
    Quantity = int(input('Введите количетсво: '))
    Teasp = 'teaspoon'
    Tablesp = 'tablespoon'
    Cups = 'cup'
    if Type == '1':
        A = Teaspoons(Quantity)
        B = Tablespoons(Quantity)
        C = Cup(Quantity)
        if A > 1:
            Teasp = 'teaspoons'
        if B > 1:
            Tablesp = 'tablespoons'
        if C > 1:
            Cups = 'cups'
        print(A, Teasp, B, Tablesp, C, Cups )
    elif Type == '2':
        B = Tablespoons(Quantity)
        C = Cup(Quantity)
        if B > 1:
            Tablesp = 'tablespoons'
        if C > 1:
            Cups = 'cups'
        print(B, Tablesp, C, Cups)
    elif Type == '3':
        if Quantity > 1:
            Cups = 'cups'
        print(Quantity, Cups)
Main()
