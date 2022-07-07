#Программа которая запрашивает строку у пользователя и оповещает его о том является ли она словесным палиндромом или нет.
from Uprajnenie117 import Sorting
Line = input('Введите строку: ')
Line = Line.lower()
List = Sorting(Line)
Reverse = List.copy()
Reverse.reverse()
if List == Reverse:
    print('Да, это словесный палиндром')
else:
    print('Нет, это не словесный палиндром')
