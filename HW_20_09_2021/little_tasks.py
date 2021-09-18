def degree(x, y) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * degree(x, y-1)

def lst_summ(list):
    if len(list) == 1:
        return list.pop(0)
    else:
        a = list.pop(0)
        return a + lst_summ(list)

def lst_summ_negative(list):
    if len(list) == 1:
        return list[0] if list[0] < 0 else 0
    else:
        return (list[0] if list[0] < 0 else 0) + lst_summ_negative(list[1:])

assert degree(2, 16) == 65536
assert lst_summ([2, 16]) == 18
assert lst_summ_negative([2, 16, -16, -2]) == -18