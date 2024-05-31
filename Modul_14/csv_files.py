

import csv


def read_city(text):
    temp = ''
    city = []
    for i in range(len(text)):
        if text[i] == ';':
            city.append(temp)
            temp = ''
        else:
            temp += text[i]
    city.append(temp)
    return city


def write_holiday_cities(first_letter):
    with open('travel-notes.csv', 'r', newline='', encoding='UTF-8') as f:
        data = csv.reader(f, delimiter=',')
        city_visited = []
        city_visit = []
        city_all = []
        for row in data:
            for name_student in row[0]:
                if name_student[0] == first_letter:
                    city_visited += read_city(row[1])
                    city_visit += read_city(row[2])
                city_all += read_city(row[1])
                city_all += read_city(row[2])

        city_visited = sorted(set(city_visited))
        city_visit = sorted(set(city_visit))
        city_all = sorted(set(city_all))
        city_no_visit = sorted(list(set(city_all) - set(city_visited)))


    with open('holiday.csv', 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Посетили: '] + city_visited)
        writer.writerow(['Хотят посетить: '] + city_visit)
        writer.writerow(['Никогда не были в: '] + city_no_visit)
        writer.writerow(['Следующим городом будет: '] + [city_visit[0]])

write_holiday_cities('R')

