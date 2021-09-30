from Classes_for_dict import Task, Tasks, a
import click


def set_and_val(text: str, conditions: list = None, texterr: str = None, check=False, checkconditions=True):
    """
    text - start message text
    texterr - error text
    conditions - условия
    check - подтверждение
    checkconditions - checkconditions
    """
    if texterr == None:
        texterr = 'Error!!! ' + text
    while True:
        value = input(f'{text}')
        if checkconditions:
            while value not in conditions:
                value = input(f'{texterr}')
        if check:
            valuecheck = input(f'Your value is - {value}. Are you sure ? (Y)es/(N)o :')
            if valuecheck in [*'YyNn']:
                return value
        else:
            return value


def table(func):
    def wrapper(title: str, bottom_line: str, data):
        length = 90
        print(''.center(length, '-'))
        print('|', (title).center(length - 2), '|', sep='')
        print(''.center(length, '-'))
        func(data)
        print(''.center(length, '-'))
        print('|', (bottom_line).center(length - 2), '|', sep='')
        print(''.center(length, '-'))

    return wrapper


@table
def show_list(lit: list):
    for i in range(len(lit)):
        print('|', str(i + 1).center(3), '- ', lit[i].ljust(38), sep='', end='')
        if i % 2 == 1 and i != 0:
            print(' |')
    print()


def show_dict(dct: dict):
    pass


def user_select(name: str = None) -> str:
    if name == None:
        while True:
            show_list('Users list', ' (a)dd User, (d)elete User     or     E(x)it ', Tasks.userslist())
            action = set_and_val(
                'Enter user number, or command :',
                [*list(map(str, range(1, len(Tasks.userslist()) + 1))), *'aAdDxX'],
            )
            if action in 'aA':
                if r_o:
                    input('!!!Operation is prohibited!!! Press Enter')
                else:
                    name = set_and_val("Enter the name of the new user :", check=True, checkconditions=False)
                    Tasks.adduser(name)
            if action in 'dD':
                if r_o:
                    input('!!!Operation is prohibited!!! Press Enter')
                else:
                    name = set_and_val("Enter the name NUMBER to delete :",
                                       [*list(map(str, range(1, len(Tasks.userslist()) + 1)))],
                                       check=True)
                    Tasks.deluser(Tasks.userslist()[int(name) - 1])
            if action in 'xX':
                exit()
            if action in [*list(map(str, range(1, len(Tasks.userslist()) + 1)))]:
                return Tasks.userslist()[int(action) - 1]
    elif name in Tasks.userslist():
        return name
    else:
        Tasks.adduser(name)
        return name


@table
def show_tasks(dct: dict):
    print('|', '#'.center(3), '- ', sep='', end='')
    print('Task name'.center(48), sep='', end='')
    print('Created'.center(10), '  ', sep='', end='')
    print('Deadline'.center(10), '  ', sep='', end='')
    print('Status'.center(11), sep='', end='')
    print('|')
    for num, el in enumerate(dct):
        if el['done']:
            status = 'completed'
        else:
            status = 'in progress'
        print('|', str(num + 1).center(3), '- ', sep='', end='')
        print(el['name'][0:48].ljust(48), sep='', end='')
        print(el['created'].ljust(10), '  ', sep='', end='')
        print(el['deadline'].center(10), '  ', sep='', end='')
        print(status.center(11), sep='', end='')
        print('|')


def show_task_det(dct: dict):
    show_tasks('Task list', 'You can do it all!', dct)
    action = set_and_val('Enter task NUMBER :', list(func_list.keys()))


@click.command()
@click.option('-n', 'name', help="user's file name in ./users/ (without extension)")
@click.option('-r/-w', 'r__o', default=False, help="r - for read-only mode")
def main(name: str = None, r__o: bool = False):
    global r_o
    r_o = r__o
    global user
    user = Tasks(user_select(name))
    while True:
        show_list('LIST OF TASKS' + chr(174),
                  ' L(O)GOUT - Change user    or     E(x)it ',
                  [func_list[x][1] for x in func_list.keys()])
        action = set_and_val('Enter num of operation :',
                             [*func_list.keys(), *'xXoO'])
        print(action)
        if action in 'xX':
            if not r_o:
                user.safetasks()
            exit()
        if action in 'oO':
            if not r_o:
                user.safetasks()
            user = Tasks(user_select(name))
        if action in func_list.keys():
            if action == '1':
                func_list[action][0]('Task list', 'You can do it all!', user.showtasks(False))
            if action == '2':
                func_list[action][0](user.showtasks(False))
        input('Press Enter to continue')


func_list = {'1': (show_tasks, 'Show tasks list'),
             '2': (show_task_det, 'Show task details'),
             '3': ('add_task', 'Add task'),
             '4': ('edit_task', 'Edit task'),
             '5': ('rename_task', 'Rename task'),
             '6': ('delete_task', 'Delete task'),
             '7': ('search_task', 'Search for a task'),
             '8': ('overdue_sort_task', 'Display sorted list by DEADLINE'),
             '9': ('reserve', 'Not used'),
             }

main()
