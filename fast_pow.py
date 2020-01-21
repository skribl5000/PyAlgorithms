# Быстрое возведение в степень, сравнений с обычным алгоритмом.
# Сложность old_pow() - O(n)
# Сложность pow() - O(sqrt(n) в лучшем случае
x = 2
n = 100

# чисто чтобы посчитать итеррации
i = 0
k = 0


def fast_pow(x, n):
    global i
    if n == 0:
        i += 1
        return 1  # крайний случай рекурсии
    elif n % 2 == 0:
        i += 1
        return fast_pow(x * x, n / 2)  # если степень четная
    else:
        i += 1
        return fast_pow(x, n - 1) * x  # это происходит если степень нечетная


print(fast_pow(x, n))
print('fast pow - ' + str(i) + "  итераций в алгоритме")


def pow_old(x, n):
    global k
    if n == 0:
        k += 1
        return 1
    else:
        k += 1
        return pow_old(x, n - 1) * x


print(pow_old(x, n))
print('just pow - ' + str(k) + '  итераций в алгоритме')
