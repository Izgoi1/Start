#Программа принимает на вход строку содержащую математическое выражение и преобразует его в список лексем. Каждая лексема
# должна быть или оператором либо числом или скобкой.
def Tokenizing(Line):
    Result = []
    Res = ''
    Line = Line.replace(' ', '')
    for i in Line:
        if i == '+' or i == '-' or i == '*' or i == '^' or i == '/' or i == '(' or i == ')':
            if len(Res) > 0:
                Result.append(Res)
                Result.append(i)
                Res = ''
            else:
                Result.append(i)
        else:
            Res += i
    if len(Res) > 0:
        Result.append(Res)
    return Result
def Main():
    Line = input('Введите математическое выражение: ')
    Result = Tokenizing(Line)
    print(Result)
if __name__ == '__main__':
    Main()