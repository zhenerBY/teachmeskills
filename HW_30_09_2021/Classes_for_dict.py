from datetime import datetime, date, timedelta
import json
import os


class Task:
    counter = 0

    def __init__(self, name: str = 'Test_task', description: str = 'Test_description',
                 deadline=date.today().strftime('%Y-%m-%d'),
                 created=date.today().strftime('%Y-%m-%d'), done=False):
        self.name = name
        self.description = description
        self.created = created
        self.deadline = deadline
        self.done = done
        self.counter = Task.counter
        Task.counter += 1

    @classmethod
    def instances(cls):
        return cls.counter + 1

    @staticmethod
    def att():
        return ['name', 'description', 'created', 'deadline']

    def attributes(self) -> list:
        att = list(self.__dict__.keys())
        att.remove('counter')
        att.remove('done')
        return att


class Tasks:

    def __init__(self, user=None):
        self.task_list = []
        if user == None:
            self.__user = 'Test_user'
            self.task_list.append(Task())  # пустая задача
        else:
            self.__user = user
            self.opentasks()

    @staticmethod
    def userslist() -> list:
        files = os.listdir('./users/')
        return [x[:-5] for x in files if x[-5:] == '.json']

    @staticmethod
    def adduser(name: str):
        newuser = Task().__dict__
        newuser.pop('counter')
        with open('./users/' + name + '.json', 'w') as f:
            json.dump([newuser], f)

    @staticmethod
    def deluser(name: str):
        os.remove('./users/' + name + '.json')

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, name):
        os.remove('./users/' + self.__user + '.json')
        self.__user = name
        self.safetasks()

    def changeuser(self, name):
        self.task_list = []
        self.__user = name
        self.opentasks()

    def addtask(self, *args) -> None:
        if args == ():
            pass
        else:
            self.task_list.append(Task(*args))

    def addlisttasks(self, tasks: list):
        for el in tasks:
            self.task_list.append(Task(**el))

    def deltasks(self, *args: int) -> None:
        ''' args this is Task counters
        '''
        tmp = []
        for el in self.task_list:
            if el.counter not in args:
                tmp.append(el)
        self.task_list = tmp.copy()

    def showtasks(self, lbl=True) -> list:
        tasklist = []
        if lbl == True:
            for task in self.task_list:
                print(task.__dict__)
        else:
            for task in self.task_list:
                tasklist.append(task.__dict__)
            return tasklist

    def tasks2save(self) -> list:
        tasklist = []
        for task in self.task_list:
            tmpdict = {}
            listtemp = list(task.__dict__.keys())
            listtemp.remove('counter')
            for task_2 in listtemp:
                tmpdict[task_2] = task.__dict__[task_2]
            tasklist.append(tmpdict)
        return tasklist

    def opentasks(self) -> None:
        self.task_list = []
        with open('./users/' + self.__user + '.json', 'r') as file_json:
            self.addlisttasks(json.load(file_json))

    def safetasks(self) -> None:
        with open('./users/' + self.__user + '.json', 'w') as file_json:
            json.dump(self.tasks2save(), file_json)

    def sorted(self, attribute: str = 'name') -> list:
        tasklist = []
        [tasklist.append(x.__dict__) for x in self.task_list]
        sorted_second = sorted(tasklist, key=lambda x: x['name'])  # second sort by 'name'
        return sorted(sorted_second, key=lambda x: x[attribute])

    def taskdone(self, *args: int) -> None:
        for el in self.task_list:
            if el.counter in args:
                el.done = True

    def filter(self, key: str, text: str) -> list:
        '''Выводит отсортированный список
        use key - '*' for search in all keys except "counter" and "done" '''
        if key != '*':
            return list(map(lambda x: x.__dict__,
                            list(filter(lambda x: text.lower() in x.__dict__[key].lower(), self.task_list))))
        else:
            tasks = []
            for i in Task.att():
                tasks.append(set(filter(lambda x: text.lower() in x.__dict__[i].lower(), self.task_list)))
            return list(map(lambda x: x.__dict__, list(tasks[0].union(*list(tasks[x] for x in range(1, len(tasks)))))))

    def test(self):
        print(self.task_list)


task1 = Task('Test Task 1!', 'Очень важная задача  ', '2021-09-09', '2021-09-08')
task2 = Task('Test Task 2', 'Очень важная задача2 ', '2021-08-09', '2021-08-08')
task3 = Task('Test Task 3', 'Очень важная задача3', '2021-10-10', '2021-08-08')
task4 = Task('Торжественное открытие', 'не забыть перерезать ленточку и для этого взять ножницы', '2021-10-01',
             '2021-09-08')
a = Tasks()
a.addtask('123', '321', '2021-10-10')
a.addtask('1123', '1321', '2021-10-09')
a.addtask('11123', '1321111', '2021-10-11')
a.addtask('Торжественное открытие', 'не забыть перерезать ленточку и для этого взять ножницы', '2021-10-01',
          '2021-09-08')
