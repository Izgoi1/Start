#Программа выполняющая 1000 симуляций игры в лото с одной картой. В конце выводится максимальное, минимальное и
# среднее количество извлечения номеров требующееся для выигрыша.
from Uprajnenie146 import *
from Uprajnenie147 import Checking
def FindNumber(Card, Number):
    Len = 0
    for Key in Card:
        if Number in Card[Key]:
            Len = len(Card[Key])
            for i in range(Len):
                if Card[Key][i] == Number:
                    Card[Key][i] = 0
    return Card
FirstCard = RandomCard()
Min = 75
Max = 0
Mean = 0

for i in range(1, 1001):
    Card = eval(repr(FirstCard))
    Value = False
    Counter = 0
    AllNumbers = list(range(1, 76))
    random.shuffle(AllNumbers)
    while Value != True:
        Number = AllNumbers[0]
        AllNumbers.remove(Number)
        FindNumber(Card, Number)
        Value = Checking(Card)
        Counter += 1
    Mean += Counter
    if Counter < Min:
        Min = Counter
    if Counter > Max:
        Max = Counter
print(f'''Минимальное количество извлечения номеров: {Min}
Максимальное количество извлечения номеров: {Max}
Среднее количество извлечения номеров: {Mean/1000}''')

