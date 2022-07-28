#Программа которая создаёт случайное карточное лото и выводит её на экран.
import random
def RandomCard():
    BINGO = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    Numbers = []
    Min = 1
    Max = 15
    for Key in BINGO:
        Numbers = []
        for i in range(1, 6):
           Number = random.randint(Min, Max)
           Numbers.append(Number)
        Min = Max + 1
        Max += 15
        BINGO[Key] = Numbers
    return BINGO
def Print(Bingo):
    print('B  I  N  G  O')
    for i in range(5):
        for d in 'BINGO':
            print(f'{Bingo[d][i]:2d}', end=' ')
        print()
def Main():
    Bingo = RandomCard()
    Print(Bingo)
if __name__ == '__main__':
    Main()