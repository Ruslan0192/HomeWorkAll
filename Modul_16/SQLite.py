# Создайте базу данных students.db
# В базе данных должны существовать 2 таблицы: students и grades
# В таблице students должны присутствовать следующие поля: id, name, age
# В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade
# Так же нужно создать класс University со следующими атрибутами и методами:
# name - имя университета
# add_student(name, age) - метод добавления студента.
# add_grade(sudent_id, subject, grade) - метод добавления оценки.
# get_students(subject=None) - метод для возврата списка студентов в формате[(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)],где subject, если не является None(по умолчанию) и если такой предмет существует, выводит студентов только по этому предмету.
# Описание полей:
# id - в обеих таблицах обязательно PRIMARY KEY
# name - STR
# age - INT
# subject - STR
# grade - FLOAT
# и самое интересное student_id - INT (или внешний ключ)
#
# Внешний ключ - это данное в поле указывающее на id в другой таблице, оно может быть реализовано следующей командой в SQL: FOREIGN KEY (student_id) REFERENCES students(id), при создании таблицы.
# При этом поле student_id - существует как INT.


import sqlite3
import random

class University():
    def __init__(self, name):
        self.name_univer = name
        self.conn = sqlite3.connect('students.db')
        # self.conn.text_factory = bytes
        self.cursor = self.conn.cursor()

        # создаем таблицу students
        try:
            self.cursor.execute("""CREATE TABLE students 
                                    ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                      name TEXT(50) NOT NULL,
                                      age INTEGER NOT NULL);""")
            self.conn.commit()
            print("Таблица students создана")
        except:
            print('Таблица students уже существует')
        # создаем таблицу grades
        try:
            self.cursor.execute("""CREATE TABLE grades 
                                    ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                      student_id INTEGER NOT NULL,
                                      subject TEXT(50) NOT NULL,
                                      grade REAL);""")
            self.conn.commit()
            print("Таблица grades создана")
        except:
            print('Таблица grades уже существует')

    def add_student(self, name, age):
        self.cursor.execute(f"INSERT INTO students "
                            f"(name, age) "
                            f"VALUES ('{name}', '{age}');")
        self.conn.commit()
    def add_grade(self, sudent_id, subject, grade):
        self.cursor.execute(f"INSERT INTO grades "
                            f"(student_id, subject, grade) "
                            f"VALUES ('{sudent_id}', '{subject}', '{grade}');")
        self.conn.commit()
    def get_students(self, subject=None):
        if subject == None:
            str_request = (f"SELECT students.name, students.age, grades.subject, grades.grade "
                           f"FROM students JOIN grades ON students.id = grades.student_id;")
        else:
            str_request = (f"SELECT students.name, students.age, grades.subject, grades.grade "
                           f"FROM students JOIN grades ON students.id = grades.student_id  "
                           f"WHERE grades.subject = '{subject}';")

        self.cursor.execute(str_request)
        self.conn.commit()
        students = self.cursor.fetchall()
        return students


u1 = University('Urban')

u1.add_student('Ivan', random.randint(20,30)) # id - 1
u1.add_student('Ilya', random.randint(20,30)) # id - 2
u1.add_student('Anna', random.randint(20,30)) # id - 1
u1.add_student('Maks', random.randint(20,30)) # id - 2
for i in range(4):
    u1.add_grade(i+1, 'Python', round(random.uniform(4,5),1))
    u1.add_grade(i+1, 'PHP', round(random.uniform(4,5),1))

print(u1.get_students())
print(u1.get_students('Python'))
u1.conn.close()


