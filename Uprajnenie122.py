#Программа которая запрашивает у пользователя строку и переводит её на поросячью латынь.
Line = input('Введите текст: ')
Line = Line.lower()
Line = Line.split(' ')
Result = ''
Word = ''
Word2 = ''
for i in Line:
    Check = 0
    Word = str(i)
    Word2 = ''
    Wd = ''
    if Word[0] == 'a' or  Word[0] == 'e' or  Word[0] == 'i' or  Word[0] == 'o' or  Word[0] == 'u':
        Result += Word + 'way '
        continue
    else:
        while Wd == '':
            if Word[Check] == 'a' or Word[Check] == 'e' or Word[Check] == 'i' or Word[Check] == 'o' or Word[Check] == 'u':
                Wd = Word[Check:] + Word2 + 'ay '
            else:
                Word2 += Word[Check]
                Check += 1
    Result += Wd
print('Ваш текст на поросячьей латыни: ', Result)
