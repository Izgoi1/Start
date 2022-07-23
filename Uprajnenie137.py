#Программа в которой симулируется определенное количество выбрасывание двух игральных костей. Программа хранит все результаты
# с частотой их выпадения. Затем на экран выводится результат выпадения числа в процентах.
import random
Number = 1000
def RandomDice():
    First = random.randint(1, 6)
    Second = random.randint(1, 6)
    return First + Second
def Ejections():
    Dictionary = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for i in range(0, Number + 1):
        Result = RandomDice()
        Dictionary[Result] = Dictionary[Result] + 1
    return Dictionary
def Main():
    Result = Ejections()
    print('Число Процент')
    for i in Result:
        print('%i, %2.f'%(i, Result[i]/ Number * 100))
Main()
