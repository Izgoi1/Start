# Программа запрашивает у пользователя месяц в текстовом варианте затем номер дня на выходе программа должна выдать название сезона
# Начало каждого сезон весна - 20 марта, лето 21 июня, осень 22 сентября, зима 21 декабря.
Month = str(input('Выберите месяц: '))
Day = int(input('Выберите день: '))
if Day < 1:
    print('Нет такого дня')
elif Month == 'Март' and Day > 20 or Month == 'Июнь' and Day < 21 or Month == 'Апрель' or Month == 'Май':
    if Month == 'Март' and Day > 31 or Month == 'Май' and Day > 31:
        print('Нет такого дня')
    elif Month == 'Апрель' and Day >= 30 or Month == 'Июнь' and Day > 30:
        print('Нет такого дня')
    elif Month == 'Март' and Day >= 20 or Month == 'Июнь' and Day <= 20 or Month == 'Апрель' or Month == 'Май':
        print('Сейчас весна')
elif Month == 'Июнь' and Day > 20 or Month == 'Сентябрь' and Day < 22 or Month == 'Июль' or Month == 'Август':
    if Month == 'Июль' and Day > 31 or Month == 'Август' and Day > 31:
        print('Нет такого дня')
    elif Month == 'Июнь' and Day > 30 or Month == 'Сентябрь' and Day > 30:
        print('Нет такого дня')
    elif Month == 'Июнь' and Day >= 21 or Month == 'Сентябрь' and Day <= 21 or Month == 'Август' or Month == 'Июль':
        print('Сейчас лето')
elif Month == 'Декабрь' and Day < 21 or Month == 'Сентябрь' and Day > 21 or Month == 'Ноябрь' or Month == 'Октябрь':
    if Month == 'Октябрь' and Day >= 31 or Month == 'Декабрь' and Day >= 31:
        print('Нет такого дня')
    elif Month == 'Сентябрь' and Day > 30 or Month == 'Ноябрь' and Day > 30:
        print('Нет такого дня')
    elif Month == 'Сентябрь' and Day >= 22 or Month == 'Декабрь' and Day <= 20 or Month == 'Октябрь' or Month == 'Ноябрь':
        print('Сейчас осень')
elif Month == 'Декабрь' and Day > 20 or Month == 'Март' and Day < 21 or Month == 'Январь' or Month == 'Февраль':
    if Month == 'Декабрь' and Day > 31 or Month == 'Январь' and Day > 31 or Month == 'Март' and Day > 31:
        print('Нет такого дня')
    elif Month == 'Февраль' and Day > 28:
        print('Нет такого дня')
    elif Month == 'Декабрь' and Day > 20 or Month == 'Март' and Day < 20 or Month == 'Январь' or Month == 'Февраль':
        print('Сейчас зима')
else:
    print('Нет такого месяца')
















