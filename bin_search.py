# Бинарный поиск

arr = [1, 1, 1, 1, 3, 4, 5, 6, 7, 7, 7, 7, 11, 11, 11, 90]


def left_bound(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] < key:
            left = middle
        else:
            right = middle
    return left


print(left_bound(arr, 11))
print(arr[left_bound(arr, 51) + 1])
