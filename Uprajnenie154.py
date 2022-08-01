#Программа которая способствует дешифрации текста путем вывода на экран частоты появления букв. Имя файла передается
# программе посредством аргумента командной строки.
import sys
if len(sys.argv) != 2:
    print('Передайте имя файла в качестве аргумента')
    quit()
try:
    Inf = open(sys.argv[1], 'r')
    Dictionary = {}
    Line = Inf.readline()
    while Line != '':
        Line = Line.lower()
        Line = Line.split()
        for Word in Line:
            for i in Word:
                if '0' <= i <= '9' or i == ',' or i == '.' or i == ':' or i == '!' or i == '?' or i == '-':
                    continue
                elif i in Dictionary:
                    Dictionary[i] += 1
                else:
                    Dictionary[i] = 1
        Line = Inf.readline()
    print(Dictionary)
    Inf.close()
except FileNotFoundError:
    print('Файл с таким именем не найден')
    quit()

