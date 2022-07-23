#Функция которая выводит список кличей из словаря по заданному значению.
def ReverseLookup(Dictionary, Value):
    List = []
    for i in Dictionary:
        if Value == Dictionary[i]:
            List.append(i)
    return List
def Main():
    Dictionary = {'Cookies': 10, 'Ice Cream': 17, 'Carrot': 17, 'Beet': 6, 'Candies': 6}
    print('Продукты по одинаковой цене: ',ReverseLookup(Dictionary, 6))
    print('Продукты по одинаковой цене: ', ReverseLookup(Dictionary, 17))
    print('Продукты по одинаковой цене: ', ReverseLookup(Dictionary, 1))
    print('Продукты по одинаковой цене: ', ReverseLookup(Dictionary, 10))
if __name__ == '__main__':
    Main()