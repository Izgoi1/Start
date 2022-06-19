#Программа запрашивает у пользователя цены пока не будет введина строка. Праграмма должна выводит общую сумму и
# Сумму наличными которая округлена до ближайших пяти центов.
Price = float(input('Введите цену: '))
Sum = float()
while Price != '':
    Price = float(Price)
    Sum += Price
    Price = input('Введите цену или нажмите "enter" для окончания ввода: ')
Price_cash = Sum
Price_cash = Price_cash * 100 % 5
if Price_cash < 2.5:
    Sum *= 100
    Price_cash = Sum - Price_cash
    Price_cash /= 100
elif Price_cash > 2.5:
    Price_cash = 10 - (Price_cash + 5)
    Sum *= 100
    Price_cash = Sum + Price_cash
    Price_cash /= 100
Sum /= 100
print(f'Общая сумма покупок составляет: {Sum}$. Сумма оплаты наличными составляет: {Price_cash}$')