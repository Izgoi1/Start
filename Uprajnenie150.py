# Программа имитирует утилиту на базе Unix которая отображает последние 10 строк содержимого файла имя которого переданного
# через командную строку в качестве аргумента.
import sys
Num = 1
if len(sys.argv) != 2:
    print('Имя файла необходимо передать в качестве аргумента')
    quit()
try:
    Inf = open(sys.argv[1], 'r')
    Line = Inf.readlines()
    Line.reverse()
    for i in Line:
        if Num > 10:
            break
        i = i.rstrip()
        print(f'{Num}: {i}')
        Num += 1
    Inf.close()
except:
    print('Файл не найден')
    quit()
