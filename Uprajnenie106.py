#функция которая определяет количество дней в конкретном месяце.
def Daysinmonth(Month, Year):
    if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
        return 31
    elif Year % 4 == 0 or (Year % 100 != 0 and Year % 400 == 0) and Month == 2:
        return 29
    elif Month == 2:
        return 28
    elif Month == 4 or Month == 6 or Month == 9 or Month == 11:
        return 30
    else:
        print('Такого месяца нет')
def Main():
    Month = int(input('Введите порядковый номер месяца: '))
    Year = int(input('Введите год: '))
    Days = Daysinmonth(Month, Year)
    if Month == 1:
        Month = 'Январе'
    elif Month == 2:
        Month = 'Феврале'
    elif Month == 3:
        Month = 'Марте'
    elif Month == 4:
        Month = 'Апреле'
    elif Month == 5:
        Month = 'Мае'
    elif Month == 6:
        Month = 'Июне'
    elif Month == 7:
        Month = 'Июле'
    elif Month == 8:
        Month = 'Августе'
    elif Month == 9:
        Month = 'Сентябре'
    elif Month == 10:
        Month = 'Октябре'
    elif Month == 11:
        Month = 'Ноябре'
    elif Month == 12:
        Month = 'Декабре'
    elif Days == None:
        print('Повторите попытку')
        quit()
    print(f'В {Year} году в {Month} {Days} дней')
Main()