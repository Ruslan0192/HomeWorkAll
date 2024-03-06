# Использование %
team1_num = 4
print("В команде Мастера кода участников: %s ! " %(team1_num))

team2_num = 3
print("Итого сегодня в командах участников: %s и %s !" %(team1_num, team2_num))
print('')

# Использование format():
score_2 = 3
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team1_time = 10.5
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print('')

# Использование f-строк:
score_1 = 11
score_2 = 12
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды Мастера кода'
print(f'Результат битвы: {challenge_result}')
tasks_total = 10
time_avg = 59.3
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')