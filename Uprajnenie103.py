#Программа которая генерирует случайный надежный пароль и выводит его на экран вместе с количеством попыток.
#Для выполнения нужно импортировать функции из упражнения 100 и 102.
from Uprajnenie100 import Password
from Uprajnenie102 import CheckPassword

M = False
Check = 0
Pass = ''
while M != True:
    Check += 1
    Pass = Password()
    if CheckPassword(Pass):
        M = True
print(f'Случайный надёжный пароль "{Pass}" сгенерирован с {Check} раза')