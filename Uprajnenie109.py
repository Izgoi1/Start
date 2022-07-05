#Функция опеределяющая является ли введенная дата магической в 20 веке.
from Uprajnenie106 import Daysinmonth
def Magicdate(Day, Month, Year):
    Year = Year % 100
    if Year == Day * Month:
        return True
    else:
        return False
def Main():
    Day = 1
    Month = 1
    Year = 1900
    while Year != 2000:
        Check = Daysinmonth(Month, Year)
        if Day == Check:
            Day = 1
            Month += 1
            continue
        elif Month == 12:
            Month = 1
            Year += 1
            continue
        if Magicdate(Day, Month, Year) == True:
            print(Day, Month, Year,'Магическая дата')
        Day += 1
Main()