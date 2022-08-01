#Программа которая считывает содержимое файла добавляя к считанным строкам порядковый номер и сохраняет их в таком в виде
# в новом файле.
import sys
Inf = sys.argv
if len(sys.argv) != 3:
    print('Необходимо передать два аргумента, имя файла для чтения и имя файла для записи')
    quit()
Inf = open(sys.argv[1], 'r')
Outf = open(sys.argv[2], 'w')
Line = Inf.readline()
Num = 1
while Line != '':
    Line = Line.rstrip()
    Outf.write(f'{Num}: {str(Line)} \n')
    Line = Inf.readline()
    Num += 1
Inf.close()
Outf.close()
