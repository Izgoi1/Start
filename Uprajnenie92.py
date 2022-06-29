# Перевод порядковая дата в григорианский календарь. Основная программа должна состоять из функции из упражнения 91 и этого упражнения
# Основная программа должна например расчитывать какого числа был приобретен товар и через сколько дней истекает гарантия в днях до 1 года.
from Uprajnenie91 import OrdinalDate
from Uprajnenie91 import Dates
def Calendar(Year, Day):
    Ordinal = Day
    Month = int()
    Leap = int()
    if Year % 4 == 0 or (Year % 100 != 0 and Year % 400 == 0):
        Leap = 1
    if Leap == 1 and Day > 366:
        Day = Day - 366
        Year += 1
    elif Leap != 1 and Day > 365:
        Day = Day - 365
        Year += 1
    if Year % 4 == 0 or (Year % 100 != 0 and Year % 400 == 0):
        Leap = 1
    if Day < 31:
        Day = Day
        Month = 1
    elif 31 < Day <= 59 and Leap != 1:
        Day = Day - 31
        Month = 2
    elif 31 < Day <= 60 and Leap == 1:
        Day = Day - 31
        Month = 2
    elif 59 < Day <= 90 and Leap != 1:
        Day = Day - 59
        Month = 3
    elif 60 < Day <= 91 and Leap == 1:
        Day = Day - 60
        Month = 3
    elif 90 < Day <= 120 and Leap != 1:
        Day = Day - 90
        Month = 4
    elif 91 < Day <= 121 and Leap == 1:
        Day = Day - 91
        Month = 4
    elif 120 < Day <= 151 and Leap != 1:
        Day = Day - 120
        Month = 5
    elif 121 < Day <= 152 and Leap == 1:
        Day = Day - 121
        Month = 5
    elif 151 < Day <= 181 and Leap != 1:
        Day = Day - 151
        Month = 6
    elif 152 < Day <= 182 and Leap == 1:
        Day = Day - 152
        Month = 6
    elif 181 < Day <= 212 and Leap != 1:
        Day = Day - 181
        Month = 7
    elif 182 < Day <= 213 and Leap == 1:
        Day = Day - 182
        Month = 7
    elif 212 < Day <= 243 and Leap != 1:
        Day = Day - 212
        Month = 8
    elif 213 < Day <= 244 and Leap == 1:
        Day = Day - 213
        Month = 8
    elif 243 < Day <= 273 and Leap != 1:
        Day = Day - 243
        Month = 9
    elif 244 < Day <= 274 and Leap == 1:
        Day = Day - 244
        Month = 9
    elif 273 < Day <= 304 and Leap != 1:
        Day = Day - 273
        Month = 10
    elif 274 < Day <= 305 and Leap == 1:
        Day = Day - 274
        Month = 10
    elif 304 < Day <= 334 and Leap != 1:
        Day = Day - 304
        Month = 11
    elif 305 < Day <= 335 and Leap == 1:
        Day = Day - 305
        Month = 11
    elif 334 < Day <= 365 and Leap != 1:
        Day = Day - 334
        Month = 12
    elif 335 < Day <= 366 and Leap == 1:
        Day = Day - 335
        Month = 12
    print(Day, Month, Year)

def Request():
    Year = int(input('Введите год: '))
    Day = int(input('Введите порядковую дату: '))
    Day += Date
    Calendar(Year, Day)

Date = Dates()
Request()

