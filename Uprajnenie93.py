#Функция которая центрирует строку. S принимает строку а Width задаёт ширину окна в символах.
def Centering(S, Width):
    if len(S) >= Width:
        return S
    else:
        Width = (Width - len(S)) // 2
        Result = " " * Width + S
        return Result
def Start():
    Width = 40
    print(Centering('Когда нибудь я', Width))
    print(Centering('Смогу', Width))
    print(Centering('Выучить пайтон', Width))
    print('Но, это не точно)')
Start()