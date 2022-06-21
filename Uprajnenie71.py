#Программа выводящая на экран 15 приближений числа pi.
A = 2
B = 3
C = 4
Pi = 3
for i in range(1, 15):
    if i % 2 == 0:
        Pi = Pi - 4/(A*B*C)
    else:
        Pi = Pi + 4 / (A*B*C)
    A = C
    B += 2
    C += 2
print('Число Pi:',Pi)
