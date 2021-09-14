from datetime import datetime
from datetime import date
from datetime import timedelta
from functools import reduce


def welcome_scr() -> None:
    table = (41, 41)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ('LIST OF TASKS'+chr(174)).center(sum(table)+1), '|', sep = '')
    print(''.center(sum(table) + len(table) + 1, '-'))
    for i, ii in enumerate(func_list):
        print(f'|{(" " + str(i+1) + " - " + func_list[ii][1]).ljust(table[0])}', end = '')
        if i%2 == 1:
            print('|', '\n', end = '', sep = '')
        if i + 1 == len(func_list):
            print('|'.rjust(table[1]+2), '\n', sep = '', end = '')
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ' e(x)it - Exit'.ljust(sum(table)+1), '|', sep = '')
    print(''.center(sum(table) + len(table) + 1, '-'))


def show_tasks() -> None:
    table = (3, 60, 10, 7)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', '#'.center(table[0]), '|', 'Task name'.center(table[1]), '|', 'DEADLINE'.center(table[2]),
          '|', 'OVERDUE'.center(table[3]), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    for c1, tsk in enumerate(task_dict):
        print(
            f'|{str(c1 + 1).center(table[0])}|{tsk.ljust(table[1])}|{str(task_dict[tsk]["deadline"]).center(table[2])}'
            f'|{str(task_dict[tsk]["deadline"] < date.today()).center(table[3])}|')
    print(''.center(sum(table) + len(table) + 1, '-'))


def show_task_det(taskN:str = 0) -> None:
    if taskN == 0:
        show_tasks()
        N = input('Enter the task number')
        tasks = list(map(lambda x: x, task_dict.keys()))
        taskN =
    for c1, tsk in enumerate(task_dict):
        print(f'Task #{c1 + 1} - {tsk} :')
        for tsk2 in list(task_dict[tsk].keys()):
            print(f'      {tsk2} - {task_dict[tsk][tsk2]}')


def add_task() -> None:
    flag = True
    task_tmp = {}
    while flag:
        name_tmp = input('Enter name of new task :')
        for att in task_att:
            if att == 'created':
                task_tmp[att] = date.today()
            elif att == 'deadline':
                task_tmp[att] = task_tmp['created'] + timedelta(
                    days=int(input('Enter number of days required to complete the task :')))
            else:
                task_tmp[att] = input(f'Enter task {att} :')
        print('This is correct? ')
        print(f'Task name - {name_tmp}')
        for att in task_att:
            print(f'{att} - {task_tmp[att]}')
        flag = input('(Y)es or (N)o :') not in "yY"
    task_dict[name_tmp] = task_tmp


def edit_task() -> None:
    for c1, tsk in enumerate(task_dict):
        print(f'Task #{c1 + 1} - {tsk} :')
    tskdel = int(input('Enter # task for modification'))
    for c1, tsk in enumerate(task_dict):
        if tskdel == c1 + 1:
            tmpdict = {}
            tmpkey = tsk
            for i, ii in enumerate(task_dict[tsk]):
                print(f'{i + 1} - {ii} - {task_dict[tsk][ii]}')
                tmpdict[i + 1] = ii
    item = int(input(f'Enter # of property {tmpdict} to change :'))
    for i, ii in enumerate(task_dict[tmpkey]):
        if i + 1 == item:
            tmpkey2 = ii
    item_ch = input(f'"{task_dict[tmpkey][tmpkey2]}" replace with : ')
    if tmpkey2 == 'created' or tmpkey2 == "deadline":
        task_dict[tmpkey][tmpkey2] = datetime.strptime(item_ch, "%Y-%m-%d").date()
    else:
        task_dict[tmpkey][tmpkey2] = item_ch


def rename_task() -> None:
    for c1, tsk in enumerate(task_dict):
        print(f'Task #{c1 + 1} - {tsk} :')
    tskdel = int(input('Enter # task for rename'))
    tskren = input('Enter new name task')
    for c1, tsk in enumerate(task_dict):
        if tskdel == c1 + 1:
            break
    task_dict[tskren] = task_dict.pop(tsk)


def delete_task() -> None:
    for c1, tsk in enumerate(task_dict):
        print(f'Task #{c1 + 1} - {tsk} :')
    tskdel = int(input('Enter # tas for delete'))
    for c1, tsk in enumerate(task_dict):
        if tskdel == c1 + 1:
            break
    task_dict.pop(tsk)


def search_task() -> None:
    phrase = input('Enter your search phrase :')
    a = set(filter(lambda x: phrase in x, task_dict))
    b = set(filter(lambda x: phrase in task_dict[x]['description'], task_dict.keys()))
    c = a.union(b)
    table = (41, 41)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ('SEARCHING RESULTS').center(sum(table)+1), '|', sep = '')
    print(''.center(sum(table) + len(table) + 1, '-'))
    for i, ii in enumerate(c):
        print(f'|{(" " + str(i + 1) + " - " + ii).ljust(table[0])}', end='')
        print('|'.rjust(table[1]+2))
    print(''.center(sum(table) + len(table) + 1, '-'))


# list tasks attributes
task_att = ('description', 'created', 'deadline')

# list test tasks
task_dict = {
    'Test Task 1!': {'description': 'Очень важная задача',
                    'created': date(2021, 9, 8), 'deadline': date(2021, 9, 9)},
    'Test Task 2': {'description': 'Очень важная задача2',
                    'created': date(2021, 8, 8), 'deadline': date(2021, 8, 9)},
    'Test Task 3': {'description': 'Очень важная задача3',
                    'created': date(2021, 8, 8), 'deadline': date(2021, 10, 10)},
    'Meting': {'description': 'Очень важная встреча',
               'created': date(2021, 9, 9), 'deadline': date(2021, 9, 20)},
    'Торжественное открытие': {'description': 'не забыть перерезать ленточку',
                               'created': date(2021, 9, 8), 'deadline': date(2021, 10, 1)},
    'забрать ребенка из садика': {'description': 'не напиццо!',
                                  'created': date(2021, 9, 7), 'deadline': date(2021, 10, 1)}
}

func_list = {'1': (show_tasks, 'Show tasks list'),
             '2': (show_task_det, 'Show task details'),
             '3': (add_task, 'Add task'),
             '4': (edit_task, 'Edit task'),
             '5': (rename_task, 'Rename task'),
             '6': (delete_task, 'Delete task'),
             '7': (search_task, 'Search for a task'),
             }

action = 0
while action not in ('exit', 'Exit', 'x'):
    welcome_scr()
    action = input('Enter num of operation :')
    while action not in func_list and action not in ('exit', 'Exit', 'x'):
        action = input('Incorrect input. Repeat. :')
    if action not in ('exit', 'Exit', 'x'):
        func_list[action][0]()
        input('Press Enter to continue')

    # print('Nothing happens')
