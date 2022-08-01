#Программа имитирует утилиту c OS на базе Unix. Утилита выводит на экран объединенное содержимое нескольикх файлов имена
# которых передаются ей в качестве аргументов командой строки. При этом файлы сцепляются в таком же порядке в котором
# указны в аргументах.
import sys
if len(sys.argv) <= 1:
    print('Передайте имена файлов в качестве аргументов')
    quit()
Inf = list(sys.argv)
Inf.pop(0)
for i in Inf:
    try:
        File = open(i, 'r')
        for Element in File:
            print(Element, end='')
        File.close()
    except FileNotFoundError:
        print('Файл',i,'  не найден')
