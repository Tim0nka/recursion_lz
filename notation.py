nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def notation(N, T):
    if T > 16:
        return 'Основание системы счисления должно быть не больше 16-ти'

    if T > N:
        return str(nums[N % T]) if N % T > 9 else str(N % T)
    return notation(N // T, T) + (str(nums[N % T]) if N % T > 9 else str(N % T))

num = int(input('Десятичное число: '))
base = int(input('Основание (2-16): '))
print(notation(num, base))
