#Функция которая принимает число от 0 до 999 и возвращает его же прописью на английском.
def InWords(Number):
    Units = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
             '9': 'nine'}
    Dozens1 = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
               '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    Dozens2 = {'2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
               '9': 'ninety'}
    Result = ''
    if len(Number) == 1:
        if Number == '0':
            Result = 'zero'
        for Key in Units:
            if Number == Key:
                Result = Units[Key]
    elif len(Number) == 2:
        if '10' <= Number <= '19':
            for Key in Dozens1:
                if Number == Key:
                    Result = Dozens1[Key]
        else:
            for Key in Dozens2:
                if Number[0] == Key:
                    Result = Dozens2[Key]
            for Key in Units:
                if Number[-1] == Key:
                    Result += ' ' + Units[Key]
    else:
        for Key in Units:
            if Number[0] == Key:
                Result = Units[Key] + ' hundred'
        for Key in Dozens2:
            if Number[1] == Key:
                Result += ' ' + Dozens2[Key]
        for Key in Units:
            if Number[-1] == Key:
                Result += ' ' + Units[Key]
    return Result
def Main():
    Number = input('Введите число(от 0 до 999): ')
    Result = InWords(Number)
    print('Введенное число прописью на английском:', Result)
Main()