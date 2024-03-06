file_name = 'task_file.txt'
with open(file_name, mode='r', encoding='UTF-8') as file:
    content = file.read()
    print(content)