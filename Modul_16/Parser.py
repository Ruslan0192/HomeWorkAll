import csv
import datetime
from selenium import webdriver
import bs4
from time import sleep

def parser() -> dict:
    driver = webdriver.Edge()
    driver.get('https://coinmarketcap.com/')
    driver.maximize_window()
    px = 0
    for i in range(10):
        px += 1000
        driver.execute_script(f'window.scrollTo(0, {px})')
        sleep(0.1)

    html = driver.page_source
    driver.close()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup

def to_num(values):
    # перевод значение капитализации в число
    temp = values[1:]
    values = ''
    for i in range(len(temp)):
        if temp[i] != ',':
            values += temp[i]
    return int(values)


def write_csv(map, summa):
    # запись данных в csv
    # H.M    dd.mm.yyyy, где    H - Часы, M - минуты, dd - день, mm - месяц, yyyy - год.
    date_now = datetime.datetime.now()
    date_now_str = date_now.strftime('%H.%M %d.%m.%y')
    with open(date_now_str+'.csv', 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(['Name', 'MC', 'MP'])
        for i in range(len(map)):
            row = map[i]
            row[2] = str(round(row[2]/summa * 100, 2))+'%'
            writer.writerow(row)


soup = parser()

# получаем все элементы
table_coin = soup.find_all('div', class_='sc-ae0cff98-2 tLNRm')
ad = table_coin[0]
# находим наименование
list_of_names = ad.find_all('p', class_='sc-71024e3e-0 ehyBa-d')
# находим цену
list_of_values = ad.find_all('span', class_='sc-11478e5d-1 hwOFkt')

map = []
summa = 0
# запись данных в массив
for names, values in zip(list_of_names, list_of_values):
    value = to_num(values.text)
    summa += value
    map.append([names.text, values.text[1:], value])

write_csv(map, summa)
