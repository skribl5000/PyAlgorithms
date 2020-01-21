# Сдвиг массива направо и налево


def cyclic_shift_left(arr):
    """
    arr:list
    func return one iteration shifted array to left direction
    """
    for k in range(len(arr) - 1):
        arr[k - 1], arr[k] = arr[k], arr[k - 1]
    return arr
    pass


A = [0, 1, 2, 3, 4]
print('Исходный массив', A)
print('Сдвиг влево', cyclic_shift_left(A))

B = [0, 1, 2, 3, 4]


def cyclic_shift_right(arr):
    """
    arr:list
    func return one iterration shifted array to right direction
    """
    tmp = arr[-1]
    for k in range(len(arr) - 2, -1, -1):
        arr[k + 1] = arr[k]
    arr[0] = tmp
    return arr


print('Сдвиг вправо', cyclic_shift_right(B))
