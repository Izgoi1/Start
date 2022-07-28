#Функция которая принимает на вход карточку(словарь) в качестве параметра и если карточка содержит 5 нулей по вертикале,
# горизонтали или диагонали, функция должна возвращать True в ином случае False
def Checking(Card):
    List = []
    Res = []
    Len = 0
    Len2 = 0
    Result = 0
    D = 0

    for Key in Card:
        Res = []
        for i in Card[Key]:
            Res.append(i)
        List.append(Res)
        if sum(Card[Key]) == 0:
            return True
    Len = len(List)
    Len2 = len(List[0])

    for d in range(0, Len2):
        for i in range(0, Len):
            Number = List[i][d]
            Result += Number
        if Result == 0:
            return True
        Result = 0
    Result = 0

    for i in range(Len):
        Number = List[i][D]
        Result += Number
        D += 1
    if Result == 0:
        return True
    Result = 0
    D = 0
    for i in reversed(range(Len)):
        Number = List[i][D]
        Result += Number
        D += 1
    if Result == 0:
        return True
    return False

def Main():
    A = {'B': [1, 2, 3, 4, 5], 'I': [0, 0, 0, 0, 0], 'N': [31, 32, 33, 34, 35], 'G': [46, 47, 48, 49, 50],
         'O': [61, 62, 63, 64, 65]}
    B = {'B': [1, 2, 3, 4, 0], 'I': [16, 17, 18, 19, 0], 'N': [31, 32, 33, 34, 0], 'G': [46, 47, 48, 49, 0],
         'O': [61, 62, 63, 64, 0]}
    C = {'B': [0, 2, 3, 4, 5], 'I': [16, 0, 18, 19, 20], 'N': [31, 32, 0, 34, 35], 'G': [46, 47, 48, 0, 50],
         'O': [61, 62, 63, 64, 0]}
    D = {'B': [1, 2, 3, 4, 5], 'I': [16, 17, 18, 19, 20], 'N': [31, 32, 33, 34, 35], 'G': [46, 47, 48, 49, 50],
         'O': [61, 62, 63, 64, 65]}
    if Checking(A):
        print('Да, карточка "A" выиграшная')
    else:
        print('На карточка "A" выигрыш не выпал')
    if Checking(B):
        print('Да, карточка "B" выиграшная')
    else:
        print('На карточка "B" выигрыш не выпал')
    if Checking(C):
        print('Да, карточка "C" выиграшная')
    else:
        print('На карточка "C" выигрыш не выпал')
    if Checking(D):
        print('Да, карточка "D" выиграшная')
    else:
        print('На карточка "D" выигрыш не выпал')
if __name__ == '__main__':
    Main()



