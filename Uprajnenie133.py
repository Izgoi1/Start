#Функция которая определяет ялвяется ли один список подсписком другого.
def IsSublist(Lerger, Smaller):
    if len(Smaller) <= 1:
        if len(Smaller) == 0:
            return True
        elif len(Smaller) == 1:
            if Smaller[0] in Lerger:
                return True
            else:
                return False
    for i in Lerger:
        if i == Smaller[0]:
            Index1 = i
            Index1 = Lerger.index(Index1)
        elif i == Smaller[-1]:
            Index2 = i
            Index2 = Lerger.index(Index2)
        elif Smaller[-1] not in Lerger:
            return False
    if Smaller == Lerger[Index1:Index2+1]:
        return True
    else:
        return False
def Main():
    Lerger = [1, 2, 3, 4, 5]
    Smaller = [3, 4]
    Result = IsSublist(Lerger, Smaller)
    if Result:
        print('Список "Smaller" является подсписком списка "Lerger"')
    else:
        print('Список "Smaller" не является подсписком списка "Lerger"')
Main()