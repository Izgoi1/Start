#Программа из двух функций, первая создаёт колоду карт а вторая её тасует, затем выводит результат.
import random
def CreateDeck():
    Deck = []
    for Suit in ['s', 'h', 'd', 'c']:
        for i in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
            Card = i + Suit
            Deck.append(Card)
    return Deck

def Shuffle(List):
    ShuffleDeck = []
    while List != []:
        Random = random.randrange(len(List))
        RandomCard = List[Random]
        ShuffleDeck.append(RandomCard)
        List.pop(Random)
    return ShuffleDeck

def Main():
    Deck = CreateDeck()
    FirstDeck = Deck.copy()
    ShuffleDeck = Shuffle(Deck)
    print('Колода карт до тасования:')
    for i in FirstDeck:
        print(i, end=' ')
    print('\nТасованая колода карт: ')
    for i in ShuffleDeck:
        print(i, end=' ')
if __name__ == '__main__':
    Main()
