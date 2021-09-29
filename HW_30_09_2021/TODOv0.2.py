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
    def wrapper(title: str, bottom_line: str, list: list):
        length = 90
        print(''.center(length, '-'))
        print('|', (title).center(length - 2), '|', sep='')
        print(''.center(length, '-'))
        func(list)
        print(''.center(length, '-'))
        print('|', (bottom_line).ljust(length - 2), '|', sep='')
        print(''.center(length, '-'))

    return wrapper


@table
def show_list(list: list) -> str:
    for i in range(len(list)):
        print('|', str(i + 1).center(3), '- ', list[i].ljust(38), sep='', end='')
        if i % 2 == 1 and i != 0:
            print(' |')
    print()


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
                    input('!!!Operation is prohibited!!! Press any key')
                else:
                    name = set_and_val("Enter the name of the new user :", check=True, checkconditions=False)
                    Tasks.adduser(name)
            if action in 'dD':
                if r_o:
                    input('!!!Operation is prohibited!!! Press any key')
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


@click.command()
@click.option('-n', 'name', help="user's file name in ./users/ (without extension)")
@click.option('-r/-w', 'r__o', default=False, help="r - for read-only mode")
def main(name: str = None, r__o: bool = False):
    global r_o
    r_o = r__o
    global user
    user = Tasks(user_select(name))

    user.showtasks()
    input()






main()
