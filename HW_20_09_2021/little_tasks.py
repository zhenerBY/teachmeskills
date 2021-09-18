def degree(x, y) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * degree(x, y-1)