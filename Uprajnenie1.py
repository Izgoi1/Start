# Вывод имени и почтового адресса
Name = 'Petyr'
Last_Name = 'Baelish'
Date = '03.16.2077'
MA = {
    'Country': 'Republic Moldova',
    'City': 'Chisinau',
    'Street': 'Maxim Gorki',
    'Telephone Code': 22,
    'Postcode': 2072
}
Text = f'''Здравствуйте {Name} {Last_Name}, ваша посылка будет на месте {Date} числа по адресу {MA['Country']},
{MA['City']}, {MA['Street']}, телефонный код: {MA['Telephone Code']},почтовый индекс: {MA['Postcode']}'''

print(Text)