# Перевод в различные системы счисления из десятичной


def number_system(x, base):
    if x <= 0:
        return ''
    return str(number_system(x//base, base)) + str(x % base)


print(number_system(1000, 10))
