# Небольшой компании срочно нужен тот, кто может умело обращаться с JSON фалами, т.к. вся их база данных, к сожалению, основана на хранении именно в таком формате.
# Менять всё и организовывать реляционную базу данных слишком долго и дорого, да и данных многовато, нужно быстрое и дешёвое решение, хоть и не самое правильное... Ну а что поделать, задача есть, нужно решать.
#
# Напишите функцию employees_rewrite(sort_type), которая:
# Принимает параметром тип сортировки (ключ) - sort_type.
# Функция должна:
# Получить данные из employees.json и записать в employees_[sort_type]_sorted.json:
# Формат записи должен быть как в исходном файле.
# Если сортировка производится по строковым значения, то в алфавитном порядке.
# Если сортировка производится по числовым значениям, то в порядке убывания.
#
# Если в функцию передаётся ключ, которого нет в словарях, то должно выбрасываться исключение - ValueError('Bad key for sorting')
# Строки lastName, LASTNAME, Lastname и т.д. являются одними и те же ключами, старайтесь привести всё к одному формату при получении данных из файла и их записи.
# Строки lastName и last_Name уже являются разными ключами, т.к. имею разное кол-во символов.

import json

def employees_rewrite(sort_type):
    sort_type = sort_type.lower()
    with open('employees.json','r') as read_json:
        load_employees = json.load(read_json)

        try:
            employee = load_employees["employees"][0] #выборка одной служащего
            for i in employee:
                if i.lower() == sort_type:          #поиск ключа без учета регистра
                    sort_type = i
                    break

            if isinstance(employee[sort_type], int): #сортировка внутри employees в зависимости от типа данных
                json_sorted = sorted(load_employees['employees'], key=lambda x: x[sort_type], reverse=True)
            else:
                json_sorted = sorted(load_employees['employees'], key=lambda x: x[sort_type])
            json_sorted = {'employees' : json_sorted} #возврат employees

            with open(f'employees_{sort_type}_sorted.json', 'w') as write_json:
                json.dump(json_sorted, write_json, indent=4)

        except KeyError:
            print('Bad key for sorting')



key_sort = input('Введите наименование ключа сортировки ')
# key_sort = 'firstName'
# key_sort = 'lastName'
# key_sort = 'department'
# key_sort = 'salary'
# key_sort = 'Error'

employees_rewrite(key_sort)


