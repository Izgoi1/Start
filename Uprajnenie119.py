#Программа которая запрашивает у пользователя ряд чисел пока он не пропустит ввод. На экран должно быть выведенно среднее значение введенных числе, затем
#числе ниже среднего, равных среднему и выше среднего.
Number = int(input('Введите числов: '))
Midle = 0
Average = 0
List = []
Below = []
Equal = []
Above = []
while Number != '':
    Number = int(Number)
    List.append(Number)
    Number = input('Введите числов (для оканчания нажмите "Enter"): ')
List.sort()
Average = len(List) // 2
Midle = List[Average]
for i in List:
    if i < Midle:
        Below.append(i)
    elif i > Midle:
        Above.append(i)
    else:
        Equal.append(i)
print(f'''Среднее значения ряда чисел: {Midle}
Список числе ниже среднего: {Below}
Список чисел равных среднему: {Equal}
Список чисел выше среднего: {Above}''')