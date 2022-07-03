#Функция проверяет надежный ли пароль. Условия для проверки надежности следующие:
#Должна присувствовать буква из нижнего и верхнего регистра, минимум одна цифра и длина не менее 8 символов.
def CheckPassword(Pass):
    Upper = False
    Lower = False
    Number = False
    for i in Pass:
        A = ord(i)
        if A in range(65, 90):
            Upper = True
        elif A in range(97, 122):
            Lower = True
        elif A in range(48, 57):
            Number = True
        else:
            continue
    if len(Pass) >= 8 and Upper and Lower and Number:
        return True
    else:
        return False

def Main():
    Pass = input('Введите ваш пароль: ')
    if CheckPassword(Pass):
        print('Ваш пароль надежный')
    else:
        print('Ваш пароль не надежный')

if __name__ == '__main__':
    Main()
