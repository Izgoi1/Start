#Программа которая определяет високосный ли год
Year = int(input('Введите год: '))
Year %= 400
Year %= 100
Year %= 4
print(Year)
if Year == 0:
    print(Year, 'Является високосным годом')
else:
    print(Year, 'Не является високосным годом')