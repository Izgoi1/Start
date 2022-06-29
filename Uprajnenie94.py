#Функция для определения возможности построения треугольника на основании длин трех его потенциальных сторон.
#Функция принимает три числовых параметра и возвращает булево значение. Если треугольник невозможен функция возвращает False и True если возможен.
def Triangle(A, B, C):
    Value = False
    if A <= 0 or B <= 0 or C <= 0:
        return Value
    if A >= B + C:
        return Value
    elif B >= A + C:
        return Value
    elif C >= A + B:
        return Value
    Value = True
    return Value

def CheckTriangle():
    A = float(input('Введите длину первой стороны: '))
    B = float(input('Введите длину второй стороны: '))
    C = float(input('Введите длину третьей стороны: '))
    Value = Triangle(A, B, C)
    print(Value)

CheckTriangle()


