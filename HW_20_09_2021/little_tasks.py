def degree(x, y) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * degree(x, y - 1)


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


def prime_number(num: int, div = None) -> bool:
    if div is None:
        div = num - 1
    while div >= 2:
        if num % div == 0:
            return False
        else:
            div -= 1
            # return prime_number(num, div-1)
    else:
        return True


def palindrome(a: str) -> bool:
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True


def bin_dec(fn):
    def wrapped(n):
        return '0b' + fn(n)
    return wrapped


@bin_dec
def dec_bin(n :int = 73) -> str:
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    n_list = list()
    while n >= 2:
        n_list.append(str(n%2))
        n //= 2
    return str(n) + ''.join(n_list[::-1])


@bin_dec
# чертовы рекурсии запередекорируются
# я тебя убедю делать как надо!
def dec_bin_rec(n :int) -> str:
    def dec_bin_rec_1(n :int) -> str:
        if n == 0:
            return '0'
        elif n == 1:
            return '1'
        while n >= 2:
            return dec_bin_rec_1(n//2) + str(n%2)
    return dec_bin_rec_1(n)


assert degree(2, 16) == 65536
assert lst_summ([2, 16]) == 18
assert lst_summ_negative([2, 16, -16, -2]) == -18
assert prime_number(73) == True
assert palindrome('123454321') == True
assert dec_bin(73) == '0b1001001'
