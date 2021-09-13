def upper(phrase: str) -> str:
    """Convert all phrase to uppercase"""
    low = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    phrase_list = list(phrase)
    for lett in phrase_list:
        if lett in low:
            print('letter index:', phrase_list.index(lett))
            print('ID index :', id(phrase_list.index(lett)))
            print('ID letter :', id(lett))
            phrase_list[phrase_list.index(lett)] = upp[low.index(lett)]
    return ''.join(phrase_list)

# почему метод индекс выводен не индекс первого символа?
upper('hhh')

def aaa(a: str) -> str:
    a = list(a)
    for i in a:
        if i in a:
            print(a.index(i))
            print(id(a.index(i)))
    for i in a:
        if i in a:
            print(a.index(i))
            print(id(a.index(i)))
            a[a.index(i)] = '_'
    return a
print(aaa('aaa'))

# a= list('aaa')
# for i in a:
#     print(a.index(i))