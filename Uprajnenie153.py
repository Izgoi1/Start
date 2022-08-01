# Программа которая находит самое длинное слово в файле и выводит его и все слова такой же длины на экран.
Len = 0
LongWord = ''
List = []
Fname = input('Введите имя файла: ')
Inf = open(Fname, 'r')
Line = Inf.readline()
while Line != '':
    Line = Line.split()
    for Word in Line:
        if len(Word) >= Len:
            Len = len(Word)
            List.append(Word)
            LongWord = Word
    Line = Inf.readline()
for Word in List:
    if len(Word) == len(LongWord):
        print(Word, end=' ')

