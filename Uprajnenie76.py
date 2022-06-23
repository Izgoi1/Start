#Проверка на многословные палиндромы
Word = input('Введите слово:')
while Word != '':
    Word = Word.lower()
    Word = Word.replace(' ', '')
    Word = Word.replace(',', '')
    Word = Word.replace(' ', '')
    Word = Word.replace('.', '')
    Reversed = ''.join(reversed(list(Word)))
    if Word == Reversed:
        print('Да, это палиндром')
    else:
        print('Нет, это не палиндром')
    Word = input('Введите слово:')