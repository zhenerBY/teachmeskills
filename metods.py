def rev_let(letter: str) -> str:
    """Reverse the case of a letter"""
    low = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    if letter in low:
        for c1, let in enumerate(low):
            if let == letter:
                return upp[c1]
    if letter in upp:
        for c1, let in enumerate(upp):
            if let == letter:
                return low[c1]


def upper(phrase: str) -> str:
    """Convert all phrase to uppercase"""
    phrase_list = list(phrase)
    low = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    for c1, lett in enumerate(phrase_list):
        if lett in low:
            phrase_list[c1] = rev_let(lett)
    return ''.join(phrase_list)


def lower(phrase: str) -> str:
    """Convert all phrase to lowercase"""
    phrase_list = list(phrase)
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    for c1, lett in enumerate(phrase_list):
        if lett in upp:
            phrase_list[c1] = rev_let(lett)
    return ''.join(phrase_list)


def capitalize(phrase: str) -> str:
    """Convert first letter uppercase, other letters to lowercase"""
    low = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    phrase_list = list(phrase)
    for c1, lett in enumerate(phrase_list):
        if c1 == 0:
            if lett in low:
                phrase_list[c1] = rev_let(lett)
        else:
            if lett in upp:
                phrase_list[c1] = rev_let(lett)
    return ''.join(phrase_list)


def title(phrase: str) -> str:
    """Convert first letters each words to uppercase, other letters - lowercase"""
    low = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    newphrase = ''
    control = True
    for lett in phrase:
        if lett in low or lett in upp:
            if control and lett in low:
                newphrase += rev_let(lett)
                control = False
            elif control and lett in upp:
                newphrase += lett
                control = False
            elif lett in upp:
                newphrase += rev_let(lett)
            else:
                newphrase += lett
        elif lett == ' ':
            newphrase += lett
            control = True
        else:
            newphrase += lett
    return newphrase


def isdigit(phrase: str) -> bool:
    """Does the string consist only of digits?"""
    digits = ('0','1','2','3','4','5','6','7','8','9')
    control = True
    for lett in phrase:
        if lett not in digits:
            control = False
    return control


def replace(phrase: str, old: str, new: str) -> str:
    """Replaces old with new in a phrase"""
    lenphrase = len(phrase)
    lenold = len(old)
    phrase_list = list(phrase)
    old_list = list(old)
    new_list = list(new)
    phrase_list_new = []
    continue1 = 0
    for c1 in range(lenphrase):
        control = []
        if continue1 <= 0:
            for c2 in range(lenold):
                if lenphrase >= c1 + c2 + lenold:
                    if phrase_list[c1 + c2] == old_list[c2]:
                        control.append(1)
                if sum(control) == lenold:
                    if phrase_list_new:
                        phrase_list_new = phrase_list_new + phrase_list[c3 + lenold:c1] + new_list
                        c3 = c1
                        continue1 = lenold - 1
                    else:
                        phrase_list_new = phrase_list[:c1] + new_list
                        c3 = c1
                        continue1 = lenold - 1
        else:
            continue1 -= 1
    phrase_list_new = phrase_list_new + phrase_list[c3 + lenold:lenphrase]
    return ''.join(phrase_list_new)

phrase = input('Please, input phrase')
methods = ('upper', 'lower', 'capitalize', 'title', 'isdigit', 'replace')
print('Input transformation method', methods)
method = input()
while method not in methods:
    method = input('Incorrect input. Please repeat.')
if method == 'replace':
    old = input('Input what we change :')
    new = input('Input what to change :')
print('Phrase :', phrase)
print('Modified in:')
if method == 'upper':
    print(upper(phrase))
elif method == 'lower':
    print(lower(phrase))
elif method == 'capitalize':
    print(capitalize(phrase))
elif method == 'title':
    print(title(phrase))
elif method == 'isdigit':
    print(isdigit(phrase))
elif method == 'replace':
    print(replace(phrase, old, new))