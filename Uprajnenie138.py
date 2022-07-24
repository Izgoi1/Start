#Программа в которой пользователь вводит текст и на выходе получает последовательность нажатия кнопок на кнопочном телефона
# что бы на экране телефона появился текст.
Line = input('Введите текст: ')
Line = Line.upper()
A = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}
Result = ''
Res = 0
for i in Line:
    for Key in A:
        String = A[Key]
        if i in A[Key]:
            Len = len(String[:(String.index(i))]) + 1
            Res = str(Key) * Len
    Result += Res
print('Последовательность кнопок для вывода текста на кнопочном телефоне:',Result)

