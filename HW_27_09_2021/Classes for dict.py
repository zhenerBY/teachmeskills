from datetime import datetime, date, timedelta
import json

""""sample task_dict
{'Test Task 1!': {'description': 'Очень важная задача  ', 'created': datetime.date(2021, 9, 8),
                  'deadline': datetime.date(2021, 9, 9)},
 'Test Task 2': {'description': 'Очень важная задача2 ', 'created': datetime.date(2021, 8, 8),
                 'deadline': datetime.date(2021, 8, 9)},
 'Test Task 3': {'description': 'Очень важная задача3', 'created': datetime.date(2021, 8, 8),
                 'deadline': datetime.date(2021, 10, 10)},
 'Meting': {'description': 'Очень важная встреча', 'created': datetime.date(2021, 9, 9),
            'deadline': datetime.date(2021, 9, 10)},
 'Торжественное открытие': {'description': 'не забыть перерезать ленточку и для этого взять ножницы',
                            'created': datetime.date(2021, 9, 8), 'deadline': datetime.date(2021, 10, 1)},
 'забрать ребенка из садика': {'description': 'не напиццо!', 'created': datetime.date(2021, 9, 7),
                               'deadline': datetime.date(2021, 10, 1)},
 'Записываем в файл 1': {'description': 'Проверка Проверка Проверка', 'created': datetime.date(2021, 9, 17),
                         'deadline': datetime.date(2021, 9, 18)},
 'test6': {'description': '6test', 'created': datetime.date(2021, 9, 18), 'deadline': datetime.date(2021, 9, 23)},
 'Task name': {'description': 'Task description', 'created': datetime.date(2021, 9, 18),
               'deadline': datetime.date(2021, 9, 18)}}
"""


class Task:

    def __init__(self, name: str = None, description: str = None, deadline=date.today().strftime('%Y-%m-%d'),
                 created=date.today().strftime('%Y-%m-%d'), done=False):
        self.name = name
        self.description = description
        self.created = created
        self.deadline = deadline
        self.done = done


class Tasks:

    def __init__(self):
        self.task_list = []
        self.task_list.append(Task()) #пустая задача

    def addtask(self, *args) -> None:
        if args == ():
            print('None')
        elif len(args) == 1:
            self.task_list.append(*args)
        else:
            self.task_list.append(Task(*args))

    def addlisttasks(self, tasks:list):
        for el in tasks:
            self.task_list.append(Task(**el))

    def showtasks(self, lbl = False) -> list:
        tasklist = []
        if lbl == True:
            for task in list(self.__dict__.items())[0][1]:
                print(task.__dict__)
        else:
            for task in list(self.__dict__.items())[0][1]:
                tasklist.append(task.__dict__)
            return tasklist


    def opentasks(self, filename:str) -> None:
        self.task_list = []
        with open(filename, 'r') as file_json:
            self.addlisttasks(json.load(file_json))


    def safetasks(self, filename:str) -> None:
        with open(filename, 'w') as file_json:
            json.dump(self.showtasks(), file_json)


task1 = Task('Test Task 1!', 'Очень важная задача  ', '2021-9-9', '2021-9-8')
task2 = Task('Test Task 2', 'Очень важная задача2 ', '2021-8-9', '2021-8-8')
task3 = Task('Test Task 3', 'Очень важная задача3', '2021-10-10', '2021-8-8')
task4 = Task('Торжественное открытие', 'не забыть перерезать ленточку и для этого взять ножницы', '2021-10-1',
             '2021-9-8')
a = Tasks()
a.addtask('123', '321', '2021-10-10')
a.addtask('1123', '1321', '2021-10-10')
a.addtask('11123', '1321111', '2021-10-10')
a.addtask(task4)


