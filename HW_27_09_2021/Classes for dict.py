from datetime import datetime, date, timedelta
import json


class Task:

    def __init__(self, name: str = 'Test_task', description: str = 'Test_description',
                 deadline=date.today().strftime('%Y-%m-%d'),
                 created=date.today().strftime('%Y-%m-%d'), done=False):
        self.name = name
        self.description = description
        self.created = created
        self.deadline = deadline
        self.done = done


class Tasks:

    def __init__(self, user=None):
        self.task_list = []
        if user == None:
            self.task_list.append(Task())  # пустая задача
        else:
            self.opentasks(user+'.json')


    def addtask(self, *args) -> None:
        if args == ():
            pass
        elif len(args) == 1:
            self.task_list.append(*args)
        else:
            self.task_list.append(Task(*args))

    def addlisttasks(self, tasks: list):
        for el in tasks:
            self.task_list.append(Task(**el))

    def showtasks(self, lbl=False) -> list:
        tasklist = []
        if lbl == True:
            for task in list(self.__dict__.items())[0][1]:
                print(task.__dict__)
        else:
            for task in list(self.__dict__.items())[0][1]:
                tasklist.append(task.__dict__)
            return tasklist

    def opentasks(self, filename: str) -> None:
        self.task_list = []
        with open('./users/' + filename, 'r') as file_json:
            self.addlisttasks(json.load(file_json))

    def safetasks(self, filename: str) -> None:
        with open('./users/' + filename, 'w') as file_json:
            json.dump(self.showtasks(), file_json)

    def sorted(self, attribute: str = 'name') -> list:
        tasklist = []
        [tasklist.append(x.__dict__) for x in list(self.__dict__.items())[0][1]]
        sorted_second = sorted(tasklist, key=lambda x: x['name'])  # second sort by 'name'
        return sorted(sorted_second, key=lambda x: x[attribute])


task1 = Task('Test Task 1!', 'Очень важная задача  ', '2021-09-09', '2021-09-08')
task2 = Task('Test Task 2', 'Очень важная задача2 ', '2021-08-09', '2021-08-08')
task3 = Task('Test Task 3', 'Очень важная задача3', '2021-10-10', '2021-08-08')
# task4 = Task('Торжественное открытие', 'не забыть перерезать ленточку и для этого взять ножницы', '2021-10-01',
#              '2021-09-08')
task4 = Task('Торжественное открытие', 'не забыть перерезать ленточку и для этого взять ножницы', '2021-10-01',
             '2021-09-08')
a = Tasks()
a.addtask('123', '321', '2021-10-10')
a.addtask('1123', '1321', '2021-10-09')
a.addtask('11123', '1321111', '2021-10-11')
a.addtask(task4)
