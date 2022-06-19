# Прграмма для подсчета среднего значения всех введенных чисел. Если первое число равно нулю тогда
# программа должна выдать сообщение об ошибке. Индикатором окончания ввода чисел служит ноль
Number = int(input('Введите число: '))
N = int()
Average = int()
Numbers = int()
while Average == 0:
    N += 1
    Numbers += Number
    if Number == 0 and N < 2:
        print('Первое число не должно равняться нулю')
        break
    elif Number == 0 and N > 1:
        N -= 1
        Average = Numbers / N
        print('Среднее значение всех введеных чисел равно: ',Average)
        break
    Number = int(input('Введите число: '))