def notation(N, T):
    if T > 16:
        return 'Основание системы счисления должно быть не больше 16-ти'

    number = ''
    while N > 0:
        N, r = divmod(N, T)
        if r > 9:
            r = chr(ord('A') + r - 10)
        number = str(r) + number
    return number


num = int(input('Десятичное число: '))
base = int(input('Основание (2-16): '))
print(notation(num, base))