#Функция которая генерирует случайный номерной знак старого или нового образца.
import random
def plateNumber(OldNew):
    PlateNumber = ''
    if OldNew == 1:
        for i in range(1, 8):
            if len(PlateNumber) < 4 :
                Number = random.randint(0, 9)
                PlateNumber += str(Number)
            else:
                Letters = chr(random.randint(65, 90))
                PlateNumber = PlateNumber + Letters
        return PlateNumber
    elif OldNew == 2:
        for i in range(1, 7):
            if len(PlateNumber) < 3:
                Letters = chr(random.randint(65, 90))
                PlateNumber += Letters
            else:
                Number = random.randint(0, 9)
                PlateNumber += str(Number)
        return PlateNumber

def Main():
    OldNew = random.randint(1, 2)
    if OldNew == 1:
        print('Случайный номерной знак нового образца - ',plateNumber(OldNew))
    elif OldNew == 2:
        print('Случайный номерной знак старого образца - ',plateNumber(OldNew))

if __name__ == '__main__':
    Main()