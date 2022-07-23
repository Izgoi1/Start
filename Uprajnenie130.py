#Программа ищет унарные операторы + и - в списке лексем и заменяет их на сочетание символов u+ и u- затем выводит на экран
from Uprajnenie129 import *
def Unary(List):
    Result = []
    for i in range(len(List)):
        if i == 0 and (List[i] == '-' or List[i] == '+'):
            Result.append('u' + List[i])
        elif (List[i] == '-' or List[i] == '+') and (List[i-1] == '(' or List[i-1] == '+' or List[i-1] == '-' or\
                                                   List[i-1] == '*' or List[i-1] == '/'):
            Result.append('u' + List[i])
        else:
            Result.append(List[i])
    return Result
def Main():
    Line = input('Введите математическое выражение: ')
    List = Tokenizing(Line)
    Result = Unary(List)
    print('Лексемы:',List)
    print('Лексем с помеченными унарными операторами:',Result)
Main()

