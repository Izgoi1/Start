#Функция которая генерирует случайный пароль от 7 до 10 символов. Символы должны быть выбраны в случайном порядке от 33 до 126 в таблице ASCII.
import random
def Password():
    A = random.randint(7, 10)
    password = ''
    for i in range(1, A+1):
        Chr = chr(random.randint(33, 126))
        password = password + Chr
    return password
def Main():
    print('Ваш случайный пароль:', Password())

if __name__ == '__main__':
    Main()