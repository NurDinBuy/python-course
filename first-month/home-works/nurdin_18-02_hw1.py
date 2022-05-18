issylKul = float(input('Температура Иссык-Кульской области: '))
Osh = float(input('Температура Ошской области: '))
Batken = float(input('Температура Баткенской области: '))
DjalalAbad = float(input('Температура ДжалалАбадской области: '))
Naryn = float(input('Температура Нарынской области: '))
Chui = float(input('Температура Чуйской области: '))
Talas = float(input('Температура Таласской области: '))

regions = float(issylKul + Osh + Batken + DjalalAbad + Naryn + Chui + Talas)

average = regions / 7

print(f'Средняя температура в Кыргызстане: {round(average, 1)}')