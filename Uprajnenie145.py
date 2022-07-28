#Программа которая расчитывает и отображает количество очков за слово как в игре эрудит
Points = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
Line = input('Введите слово: ')
Result = 0
Line1 = Line.upper()
for i in Line1:
    for Key in Points:
        if i in Points[Key]:
            Point = Key
            Result += Point
print(f'За слово "{Line}" вы получите: {Result} очков')