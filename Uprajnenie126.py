#Программа в которой создаётся колода карт и тасутеся(функции импортируемые с упражнения 125) затем пользователь вводит
# количество игроков и количество розданных им карт на руки далее программа выводит карты каждого игрока и оставшиеся карты в колоде.
from Uprajnenie125 import *
def Deal(Players, Cards, Deck):
    Result = []
    for i in range(Players):
        Result.append([] * Players)
    for i in range(1, Cards+1):
        Check = 0
        for d in Result:
            Card = Deck[0]
            Result[Check].append(Card)
            Check += 1
            Deck.remove(Card)
    Result.append(Deck)
    return Result
def Main():
    Players = int(input('Введите количество игроков: '))
    Cards = int(input('Введите количество раздаваемых карт на руки: '))
    Number = 0
    Deck = CreateDeck()
    ShuffleDeck = Shuffle(Deck)
    Result = Deal(Players, Cards, ShuffleDeck)
    for i in Result:
        Number += 1
        if i == Result[-1]:
            print('Оставшиеся карты в колоде:',end=' ')
            for d in i:
                print(d, end=' ')
            print()
        else:
            print('Карты игрока №{0}:'.format(Number), end=' ')
            for d in i:
                print(d, end=' ')
            print()
Main()

