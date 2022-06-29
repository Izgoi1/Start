#Функция принимающая на вход три целых числа: день, месяц и год затем возвращает порядковый номер заданного дня в указанном году.
def OrdinalDate(Day, Month, Year):
    global Ordinal
    Ordinal = int()
    Leap = int()
    if Day > 31:
        Day = 31
    if Month > 12:
        Month = 12
    if Year % 4 == 0 or (Year % 100 != 0 and Year % 400 == 0):
        Leap = 1
    if Month == 1:
        Ordinal = Day
    elif Month == 2:
        Ordinal = 31 + Day
    elif Month == 3:
        Ordinal = 59 + Day
    elif Month == 4:
        Ordinal = 90 + Day
    elif Month == 5:
        Ordinal = 120 + Day
    elif Month == 6:
        Ordinal = 151 + Day
    elif Month == 7:
        Ordinal = 181 + Day
    elif Month == 8:
        Ordinal = 212 + Day
    elif Month == 9:
        Ordinal = 243 + Day
    elif Month == 10:
        Ordinal = 273 + Day
    elif Month == 11:
        Ordinal = 304 + Day
    elif Month == 12:
        Ordinal = 334 + Day
    if Leap == 1 and Month > 2:
        Ordinal += 1
    print('Номер порядкового дня: ', Ordinal)
    return Ordinal

def Dates():
    Day = int(input('Введите день: '))
    Month = int(input('Введите месяц (в числовом варианте): '))
    Year = int(input('Введите год: '))
    Date = OrdinalDate(Day, Month, Year)
    return Date

