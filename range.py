def rg(a: int, b: int = '@$^*fhYLu', c: int = '@$^*fhYLu') -> tuple:
    """Замена RANGE (tuple)"""
    if b == c and b == '@$^*fhYLu':
        b = a
        a = 0
        c = 1
    elif c == '@$^*fhYLu':
        c = 1
    list1 = []
    n = int(a)
    b = int(b)
    c = int(c)
    if c == 0:
        return list1
    elif c > 0:
        while n < b:
            list1.append(n)
            n += c
    elif c < 0:
        while n > b:
            list1.append(n)
            n += c
    return tuple(list1)


print(rg(-10, 22, 1))
