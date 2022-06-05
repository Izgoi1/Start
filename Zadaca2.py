# Программа которая принимает текст и вывыодит самое длинное слово и часто встречающееся
Text = ('lorem ipsum dolor sit amet amet amet')
Words = Text.split()
Max = max(Words, key=len)
for i in set(Words):
    if Words.count(i) > 1:
        break
print(Max, i)