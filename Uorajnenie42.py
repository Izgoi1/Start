# Программа запрашивает у пользователя обозначение ноты и показывает её частоту.
Note = str(input('Выберите ноту: '))
Number = int(input('Выберите октаву: '))
if Note == 'C':
    Frequency = 261.63 / 2**(4-Number)
elif Note == 'D':
    Frequency = 293.66 / 2 ** (4 - Number)
elif Note == 'E':
    Frequency = 329.63 / 2 ** (4 - Number)
elif Note == 'F':
    Frequency = 349.23 / 2 ** (4 - Number)
elif Note == 'G':
    Frequency = 392.00 / 2 ** (4 - Number)
elif Note == 'A':
    Frequency = 440.00 / 2 ** (4 - Number)
elif Note == 'B':
    Frequency = 493.88 / 2 ** (4 - Number)
print('Частота ноты {0}{1} равна {2} Гц'.format(Note, Number, Frequency))
