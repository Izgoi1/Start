#Программа имитирующая утилиту на базе Unix которая выводит первые десять строк содержимого файла имя которого передается
# в качестве аргумента командной строки.
import sys
Num = 1
if len(sys.argv) != 2:
    print('Имя файла необходимо передать в качестве аргумента')
    quit()
try:
    Inf = open(sys.argv[1], 'r')
    Line = Inf.readline()
    while Num != 11 and Line != '':
        Line = Line.rstrip()
        print(f'{Num}: {Line}')
        Num += 1
        Line = Inf.readline()
    Inf.close()
except FileNotFoundError:
    print('Файл не найдет')
    quit()