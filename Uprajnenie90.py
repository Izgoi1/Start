#Программа которая сама строит куплеты песенки " The twelve days of Christmas " при помощи импорта функции из упражнения 89.
from Uprajnenie89 import Numerals
def Couplets(n):
    print('On the', Numerals(n), 'day of Christmas,\nmy true love sent to me')
    if n >= 2:
        print('Two turtledoves')
    if n >= 3:
        print('Three French hens')
    if n >= 4:
        print('Four calling birds')
    if n >= 5:
        print('Five gold rings(five gold rings)')
    if n >= 6:
        print('Six geese a-laying')
    if n >= 7:
        print('Seven swans a-swimming')
    if n >= 8:
        print('Eight maids a-milking')
    if n >= 9:
        print('Nine ladies dancing')
    if n >= 10:
        print('Ten lords a-leaping')
    if n >= 11:
        print('I sent eleven pipers piping')
    if n >= 12:
        print('Twelve drummers drumming')
    if n == 1:
        print('A', end="")
    else:
        print('And a', end="")
    print('partridge in a pear tree')
    print()

def Song():
    for a in range (1, 12):
        Couplets(a)
Song()