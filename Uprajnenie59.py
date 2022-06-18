# Программа которая принимает дату и выводит дату следующую за ней.
Year = int(input('Введите год: '))
Month = str(input('Введите месяц: '))
Day = int(input('Введите день: '))
Day += 1

Leap_Year = Year # Проверка на високосный год
Leap_Year %= 400
Leap_Year %= 100
Leap_Year %= 4

if Month == 'Январь' and Day > 31:
    Day = 1
    Month = 'Февраля'
elif Month == 'Февраль':
    if Leap_Year == 0 and Day > 29:
        Day = 1
        Month = 'Марта'
    elif Leap_Year != 0 and Day > 28:
        Day = 1
        Month = 'Марта'
elif Month == 'Март' and Day > 31:
    Day = 1
    Month = 'Апреля'
elif Month == 'Апрель' and Day > 30:
    Day = 1
    Month = 'Май'
elif Month == 'Май' and Day > 31:
    Day = 1
    Month = 'Июня'
elif Month == 'Июнь' and Day > 30:
    Day = 1
    Month = 'Июля'
elif Month == 'Июль' and Day > 31:
    Day = 1
    Month = 'Августа'
elif Month == 'Август' and Day > 31:
    Day = 1
    Month = 'Сентября'
elif Month == 'Сентябрь' and Day > 30:
    Day = 1
    Month = 'Октября'
elif Month == 'Октябрь' and Day > 31:
    Day = 1
    Month = 'Ноября'
elif Month == 'Ноябрь' and Day > 30:
    Day = 1
    Month = 'Декабрь'
elif Month == 'Декабря' and Day > 31:
    Day = 1
    Year += 1
    Month = 'Январь'
print('Следующая дата:', Day, Month, Year  )
