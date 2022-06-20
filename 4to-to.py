PENNIES_PER_NICKEL = 5
NICKEL = 0.05
total = 0
line = float(input("Введите цену товара (пустая строка для выхода): "))

while line != '':
    line = float(line)
    total += line
    line = input("Введите цену товара (пустая строка для выхода): ")
print("Полная сумма к оплате: %.02f" % total)

rounding_indicator = total * 100 % PENNIES_PER_NICKEL
if rounding_indicator < PENNIES_PER_NICKEL / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + NICKEL - rounding_indicator / 100
    # Выводим итоговую сумму для оплаты
    print("Сумма для оплаты наличными: %.02f" % cash_total)