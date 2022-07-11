#Расширенная версия программы из упражнения 122, в которой текст переводится на поросячью латынь, в которой корректно обрабатываются символы в
# верхнем регистре и знаки препинания, такие как запятая, точка, восклицательный и вопросительный знак.
Line = input('Введите текст: ')
Line = Line.split(' ')
Result = ''
Word = ''
Word2 = ''
for i in Line:
    Check = 0
    Word = str(i)
    Letter = Word[0]
    Word2 = ''
    Wd = ''
    if Word[0] == Letter.upper():
        Word = Word.lower()
        if Word[0] == 'a' or Word[0] == 'e' or Word[0] == 'i' or Word[0] == 'o' or Word[0] == 'u':
            if Word[-1] == '.' or Word[-1] == ',' or Word[-1] == '?' or Word[-1] == '!':
                Result += Word[0].upper() + Word[1:-1] + 'way' + Word[-1]
            else:
                Result += Word[0].upper() + Word[1:]
            continue
        else:
            if Word[-1] == '.' or Word[-1] == ',' or Word[-1] == '?' or Word[-1] == '!':
                while Wd == '':
                    if Word[Check] == 'a' or Word[Check] == 'e' or Word[Check] == 'i' or Word[Check] == 'o' or Word[Check] == 'u':
                        Wd = Word[Check].upper() + Word[Check+1:-1] + Word2 + 'ay' + Word[-1]
                    else:
                        Word2 += Word[Check]
                        Check += 1
            else:
                while Wd == '':
                    if Word[Check] == 'a' or Word[Check] == 'e' or Word[Check] == 'i' or Word[Check] == 'o' or Word[Check] == 'u':
                        Wd = Word[Check].upper() + Word[Check+1:-1] + Word2 + 'ay'
                    else:
                        Word2 += Word[Check]
                        Check += 1
    else:
        if Word[0] == 'a' or Word[0] == 'e' or Word[0] == 'i' or Word[0] == 'o' or Word[0] == 'u':
            if Word[-1] == '.' or Word[-1] == ',' or Word[-1] == '?' or Word[-1] == '!':
                Result += Word[0:-1] + 'way' + Word[-1]
            else:
                Result += Word
            continue
        else:
            if Word[-1] == '.' or Word[-1] == ',' or Word[-1] == '?' or Word[-1] == '!':
                while Wd == '':
                    if Word[Check] == 'a' or Word[Check] == 'e' or Word[Check] == 'i' or Word[Check] == 'o' or Word[Check] == 'u':
                        Wd = Word[Check:-1] + Word2 + 'ay' + Word[-1]
                    else:
                        Word2 += Word[Check]
                        Check += 1
            else:
                while Wd == '':
                    if Word[Check] == 'a' or Word[Check] == 'e' or Word[Check] == 'i' or Word[Check] == 'o' or Word[Check] == 'u':
                        Wd = Word[Check:] + Word2 + 'ay'
                    else:
                        Word2 += Word[Check]
                        Check += 1
    Result += ' ' + Wd
print('Ваш текст на поросячьей латыни:',Result)