#Программа запрашивающая у пользователя сдачу в центах а затем расчитывает сколько и каких момент потребуется для выдачи указаной суммы.
Change = int(input('Сумма сдачи в центах: '))
Toonie = Change // 200
Change = Change % 200
Loonie = Change // 100
Change = Change % 100
Cent_25 = Change // 25
Change = Change % 25
Cent_10 = Change // 10
Change = Change % 10
Cent_5 = Change // 5
Change = Change % 5
Cent_1 = Change // 1
Change = Change % 1
print(f'Ваша сдача в виде {Toonie} двухдолларовых монет, {Loonie} однодолларовых монет, {Cent_25} двадцатипятицентовых монет '
      f'{Cent_10} десятицентовых монет, {Cent_5} пятицентовых монет, {Cent_1} одноцентовых монет')
