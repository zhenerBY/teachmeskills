from datetime import datetime
from datetime import date
from datetime import timedelta


def welcome_scr():
    print('|----------------------------------------------------------------|')
    print('|                     LIST OF TASKS                              |')
    print('|----------------------------------------------------------------|')
    print('| 1 - Show tasks list                                            |')
    print('| 2 - Show task details                                          |')
    print('| 3 - Add task                                                   |')
    print('| 4 - Edit task                                                  |')
    print('| 5 - Rename task                                                |')
    print('| 6 - Delete task                                                |')
    print('|----------------------------------------------------------------|')
    print('|----------------------------------------------------------------|')
    print('| exit - Exit the programm                                       |')
    print('|----------------------------------------------------------------|')


task_att = ('description', 'created', 'deadline')
task_dict = {
    'Test Task 1': {'description': 'Очень важная задача',
                    'created': date(2021, 9, 8), 'deadline': date(2021, 9, 9)},
    'Test Task 2': {'description': 'Очень важная задача2',
                    'created': date(2021, 8, 8), 'deadline': date(2021, 8, 9)},
    'Test Task 3': {'description': 'Очень важная задача3',
                    'created': date(2021, 8, 8), 'deadline': date(2021, 10, 10)}
}

action = 0
while action != 'exit' and action != 'Exit':
    welcome_scr()
    action = input('Enter num of operation :')
    if action == '1':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk} : DEADLINE - {task_dict[tsk]["deadline"]}'
                  f' : OVERDUE - {task_dict[tsk]["deadline"] < date.today()}')
        input('Press Enter to continue')

    elif action == '2':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk} :')
            for tsk2 in list(task_dict[tsk].keys()):
                print(f'      {tsk2} - {task_dict[tsk][tsk2]}')
        input('Press Enter to continue')

    elif action == '3':
        name_tmp = input('Enter name of new task :')
        task_tmp = {}
        flag = True
        while flag:
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
            flag = input('(Y)es or (N)o :') != "Y"
        task_dict[name_tmp] = task_tmp

    elif action == '4':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk} :')
        tskdel = int(input('Enter # task for modification'))
        for c1, tsk in enumerate(task_dict):
            if tskdel == c1 + 1:
                tmpdict = {}
                tmpkey = tsk
                for i, ii in enumerate(task_dict[tsk]):
                    print(f'{i+1} - {ii} - {task_dict[tsk][ii]}')
                    tmpdict[i+1] = ii
        item = int(input(f'Enter # of property {tmpdict} to change :'))
        for i, ii in enumerate(task_dict[tmpkey]):
            if i+1 == item:
                tmpkey2 = ii
        item_ch = input(f'"{task_dict[tmpkey][tmpkey2]}" replace with : ')
        if tmpkey2 == 'created' or tmpkey2 == "deadline":
              task_dict[tmpkey][tmpkey2] = datetime.strptime(item_ch, "%Y-%m-%d").date()
        else:
            task_dict[tmpkey][tmpkey2] = item_ch

    elif action == '5':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk} :')
        tskdel = int(input('Enter # task for rename'))
        tskren = input('Enter new name task')
        for c1, tsk in enumerate(task_dict):
            if tskdel == c1 + 1:
                break
        task_dict[tskren] = task_dict.pop(tsk)

    elif action == '6':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk} :')
        tskdel = int(input('Enter # tas for delete'))
        for c1, tsk in enumerate(task_dict):
            if tskdel == c1 + 1:
                break
        task_dict.pop(tsk)

    elif action == 'exit' or action == 'Exit':
        None
    else:
        print('Incorrect input. Repeat.')

        # print('Nothing happens')
