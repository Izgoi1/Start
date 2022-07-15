#Программа которая запрашивает у пользователя координаты коллекции точек ввод координат продолжается пока пользователь не оставит
# ввод координаты X пустым, затем по формуле производится расчет линии наилучшего соответствия.
Xlist = []
Ylist = []
SumX = 0
SumY = 0
SumXY = 0
Check = 0
SumX2 = 0
N = 0
X = float(input('Введите точку X (для окончания нажмите "Enter"): '))
while X != '':
    X = float(X)
    Xlist.append(X)
    Y = float(input('Введите точку Y: '))
    Ylist.append(Y)
    X = input('Введите точку X (для окончания нажмите "Enter"): ')
for i in Ylist:
    XY = i * Xlist[Check]
    SumXY += XY
    Check += 1
for i in Xlist:
    X2 = i**2
    SumX2 += X2
N = len(Xlist)
SumX = sum(Xlist)
SumY = sum(Ylist)
M = (SumXY - (N * (SumY / N) * (SumX / N))) / (SumX2 - N * (SumX / N)**2)
B = (SumY / N) - M * (SumX / N)
print(f'Итоговая формула: y = {M:.2f}x + {B:.2f}')