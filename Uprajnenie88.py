#Функция которая определяет медиану из трех значений.
def Median(Number1, Number2, Number3):
    Max = max(Number1, Number2, Number3)
    Min = min(Number1, Number2, Number3)
    Mid = (Number1 + Number2 + Number3) - (Max + Min)
    print(Mid)
Median(1, 2, 3)
