# Программа которая запрашивает у пользователя год и выводит на экран день недели на который приходится 1 янаваря
import math
Year = int(input('Введите год: '))
Day_of_the_week = ((Year + math.floor((Year - 1) / 4)) - math.floor(((Year - 1) / 100)) + math.floor((Year - 1) / 400)) % 7
Day = str
if Day_of_the_week == 1:
    Day = 'Понедельник'
elif Day_of_the_week == 2:
    Day = 'Вторник'
elif Day_of_the_week == 3:
    Day = 'Среда'
elif Day_of_the_week == 4:
    Day = 'Четверг'
elif Day_of_the_week == 5:
    Day = 'Пятница'
elif Day_of_the_week == 6:
    Day = 'Суббота'
elif Day_of_the_week == 7:
    Day = 'Воскресенье'
print(f' В {Year} году 1 января выпадает на {Day}')
