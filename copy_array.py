# Копирование массива (создание нессылочной версии)

A = [1, 2, 3, 4, 5]


def copy_array(arr):
    """
        arr - input array - list
    """
    B = [0] * len(arr)
    for n in range(len(arr)):
        B[n] = A[n]
    return B


print(copy_array(A))

# IMPORTANT
# Если сделать как ниже, получается ссылка => меняем А и меняется C

# C = A
# A[0] = 228
# print(A)
# print(C)

# ALTERNATIVA
# C = list(A)
