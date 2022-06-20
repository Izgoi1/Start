# Программа которая расчитывает среднюю оценку по произвольному количеству введеных буквенных оценок
Letter = input('Введите онцеку: ')
Cycle = int()
Grade = int()
while Letter != '':
    Letter = Letter.upper()
    Cycle += 1
    if Letter == 'A':
        Grade += 4
    elif Letter == 'A-':
        Grade += 3.7
    elif Letter == 'B+':
        Grade += 3.3
    elif Letter == 'B':
        Grade += 3
    elif Letter == 'B-':
        Grade += 2.7
    elif Letter == 'C+':
        Grade += 2.3
    elif Letter == 'C':
        Grade += 2
    elif Letter == 'C-':
        Grade += 1.7
    elif Letter == 'D+':
        Grade += 1.3
    elif Letter == 'D':
        Grade += 1
    elif Letter == 'F': 0
    Letter = input('Введите онцеку (Нажмите "Enter" для окончания ввода): ')
Grade /= Cycle
print('Средняя оценка в числовом виде равна:', Grade)
