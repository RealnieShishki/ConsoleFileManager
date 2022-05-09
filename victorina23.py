def victorina():
    print('ВИКТОРИНА "Угадай дату рождения"')
    birthday_dict = {'Толстой Л.Н.': '09.09.1828',
                     'Пушкин А.С.': '26.05.1799',
                     'Гоголь Н.В.': '01.04.1809',
                     'Чехов А.П.': '29.01.1860',
                     'Есенин С.А.': '03.10.1895',
                     'Лермонтов М.Ю.': '15.10.1814',
                     'Гумилёв Н.С.': '15.04.1886',
                     'Тютчев Ф.И.': '05.12.1803',
                     'Фет А.А.': '05.12.1820',
                     'Пастернак Б.Л.': '10.02.1890'}
    month_list = {'01': 'январь',
                  '02': 'февраль',
                  '03': 'март',
                  '04': 'апрель',
                  '05': 'май',
                  '06': 'июнь',
                  '07': 'июль',
                  '08': 'август',
                  '09': 'сентябрь',
                  '10': 'октябрь',
                  '11': 'ноябрь',
                  '12': 'декабрь'}
    import random
    famous_persons = list(birthday_dict.keys())
    result = random.sample(famous_persons, 5)
    points = 0
    for i in result:
        print(i)
        date = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        print(date in birthday_dict.setdefault(i))
        if date == birthday_dict.setdefault(i):
            points += 1
        else:
            another_date = birthday_dict.setdefault(i)
            another_date = another_date.replace('.', ' ').split()
            print(another_date[0], month_list.setdefault(another_date[1]), another_date[2])
    print('-------------------------')
    print('Поздравляем!!!')
    print('Набранно ', points, ' баллов')
