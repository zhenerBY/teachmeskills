from datetime import datetime, date, timedelta
import json
from functools import reduce

def json_date_to_iso(obj):
    """JSON serializer for objects datetime.date by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

def date_hook(json_dict):
    """JSON convert date.isoformat to datetime.date"""
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.strptime(value, "%Y-%m-%d").date()
        except:
            pass
    return json_dict


def welcome_scr() -> None:
    table = (41, 41)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ('LIST OF TASKS' + chr(174)).center(sum(table) + 1), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    for i, ii in enumerate(func_list):
        print(f'|{(" " + str(i + 1) + " - " + func_list[ii][1]).ljust(table[0])}', end='')
        if i % 2 == 1:
            print('|', '\n', end='', sep='')
        if i + 1 == len(func_list):
            print('|'.rjust(table[1] + 2), '\n', sep='', end='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ' e(x)it - Exit'.ljust(sum(table) + 1), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))


def show_tasks() -> None:
    table = (3, 60, 10, 7)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', '#'.center(table[0]), '| ', 'Task name'.ljust(table[1] - 1), '|', 'DEADLINE'.center(table[2]),
          '|', 'OVERDUE'.center(table[3]), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    for c1, tsk in enumerate(task_dict):
        print(
            f'|{str(c1 + 1).center(table[0])}| {tsk.ljust(table[1] - 1)}|{str(task_dict[tsk]["deadline"]).center(table[2])}'
            f'|{str(task_dict[tsk]["deadline"] < date.today()).center(table[3])}|')
    print(''.center(sum(table) + len(table) + 1, '-'))


def show_task_det(task:str = '0') -> None:
    if task == '0':
        show_tasks()
        task = input('Enter the task number')
        while task not in list(map(str, (list(range(1, len(task_dict) + 1))))):
            show_tasks()
            task = input('ERROR!!! Enter the task number')
        # N = list(task_dict.keys())[int(N)-1}
        task = list(task_dict.keys())[int(task) - 1]
    # print(f'Task #{N} - {task} :')
    print(f'Task Name - {task} :')
    for tsk2 in list(task_dict[task].keys()):
        print(f'      {tsk2} - {task_dict[task][tsk2]}')


def add_task() -> None:
    flag = True
    task_tmp = {}
    while flag:
        name_tmp = input('Enter name of new task, or Enter to cancel :')
        if name_tmp == '':
            break
        elif name_tmp in task_dict.keys():
            name_tmp = input('This name already exist. Please enter another one  :')
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
    show_tasks()
    tskdel = input('Enter # task for modification, or Enter to cancel :')
    if tskdel != '':
        while tskdel not in list(map(str, (list(range(1, len(task_dict) + 1))))):
            show_tasks()
            tskdel = (input('Error. Reenter # task! '))
        tskdel = int(tskdel)
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
    show_tasks()
    tskdel = input('Enter # task for rename, or Enter to cancel :')
    if tskdel != '':
        while tskdel not in list(map(str, (list(range(1, len(task_dict) + 1))))):
            show_tasks()
            tskdel = (input('Error. Reenter # task! '))
        tskdel = int(tskdel)
        for c1, tsk in enumerate(task_dict):
            if tskdel == c1 + 1:
                break
        tskren = input(f'Enter new name for "{tsk}"')
        task_dict[tskren] = task_dict.pop(tsk)


def delete_task() -> None:
    show_tasks()
    tskdel = input('Enter # tas for delete, or Enter to cancel :')
    if tskdel != '':
        for c1, tsk in enumerate(task_dict):
            if int(tskdel) == c1 + 1:
                break
        task_dict.pop(tsk)


def search_task() -> None:
    phrase = input('Enter your search phrase :')
    a = set(filter(lambda x: phrase in x, task_dict))
    b = set(filter(lambda x: phrase in task_dict[x]['description'], task_dict.keys()))
    c = a.union(b)
    table = (3, 60, 10, 7)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', ('SEARCHING RESULTS').center(sum(table) + 3), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', '#'.center(table[0]), '| ', 'Task name'.ljust(table[1] - 1), '|', 'DEADLINE'.center(table[2]),
          '|', 'OVERDUE'.center(table[3]), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    filtr_list = []
    for c1, tsk in enumerate(c):
        print(
            f'|{str(c1 + 1).center(table[0])}| {tsk.ljust(table[1] - 1)}|{str(task_dict[tsk]["deadline"]).center(table[2])}'
            f'|{str(task_dict[tsk]["deadline"] < date.today()).center(table[3])}|')
        filtr_list.append(tsk)
    print(''.center(sum(table) + len(table) + 1, '-'))
    if filtr_list:
        ans = input('Do you want see task description? (Y)es, (N)o :')
        if ans in 'yY':
            ans_num = int(input('Enter task number :'))
            while ans_num not in range(1, len(filtr_list) + 1):
                ans_num = int(input('Error!! Enter task number :'))
            # show_task_det(list(task_dict.keys()).index(filtr_list[ans_num - 1]))
            show_task_det(filtr_list[ans_num - 1])
    else:
        print('Nothing found !')


def overdue_sort_task() -> None:
    table = (3, 60, 10, 7)
    print(''.center(sum(table) + len(table) + 1, '-'))
    print('|', '#'.center(table[0]), '| ', 'Task name'.ljust(table[1] - 1), '|', 'DEADLINE'.center(table[2]),
          '|', 'OVERDUE'.center(table[3]), '|', sep='')
    print(''.center(sum(table) + len(table) + 1, '-'))
    sort = sorted(task_dict, key=lambda x: task_dict[x]['deadline'])
    for c1, tsk in enumerate(sort):
        print(
            f'|{str(c1 + 1).center(table[0])}| {tsk.ljust(table[1] - 1)}|{str(task_dict[tsk]["deadline"]).center(table[2])}'
            f'|{str(task_dict[tsk]["deadline"] < date.today()).center(table[3])}|')
    print(''.center(sum(table) + len(table) + 1, '-'))


def reserve():
    None


# list tasks attributes
task_att = ('description', 'created', 'deadline')


func_list = {'1': (show_tasks, 'Show tasks list'),
             '2': (show_task_det, 'Show task details'),
             '3': (add_task, 'Add task'),
             '4': (edit_task, 'Edit task'),
             '5': (rename_task, 'Rename task'),
             '6': (delete_task, 'Delete task'),
             '7': (search_task, 'Search for a task'),
             '8': (overdue_sort_task, 'Display sorted list by DEADLINE'),
             '9': (reserve, 'Not used'),
             }

with open('user1.json', 'r') as file_json:
    task_dict = json.load(file_json, object_hook=date_hook)
action = 0
while action not in ('exit', 'Exit', 'x'):
    welcome_scr()
    action = input('Enter num of operation :')
    while action not in func_list and action not in ('exit', 'Exit', 'x'):
        welcome_scr()
        action = input('Incorrect input. Repeat. :')
    if action not in ('exit', 'Exit', 'x'):
        func_list[action][0]()
        input('Press Enter to continue')
with open('user1.json', 'w') as file_json:
    json.dump(task_dict, file_json, default=json_date_to_iso)


    # print('Nothing happens')
