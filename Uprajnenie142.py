#Программа определяющая количество уникальных символов в введенной пользователем строке.
Line = input('Введите текст: ')
Dictionary = {}
for i in Line:
    Dictionary[i] = ''
print(Dictionary)
print(f'В строке {Line} {len(Dictionary)} уникальных символов')