def array_inverse(arr):
    """
    func inverses array
    returns another inversed array

    arr:inversing array - list
    """
    B = [0] * len(arr)
    for k in range(len(arr)):
        B[len(arr) - k - 1] = arr[k]
    return (B)


A = [1, 2, 3, 4, 5]
array_inverse(A)


# eta rabotaet s dop massivom

def array_inverse_v2(arr):
    """
    func inverses array
    returns the same array but inversed

    arr:inversing array - list
    """
    for k in range(0, len(arr) / 2):
        arr[k], arr[len(arr) - 1 - k] = arr[len(arr) - 1 - k], arr[k]
    return (arr)


# ^^^^^^^^
# THE BEST
# eta rabotaet bez dop massiva

#  tests for examples
def test_array_inverse():
    A1 = [1, 2, 3]
    t = array_inverse(A1)
    if t == [3, 2, 1]:
        print('v1 passed')
    else:
        print('v1 failed')

    A2 = [1, 2, 3]
    t = array_inverse_v2(A2)
    if t == [3, 2, 1]:
        print('v2-1 passed')
    else:
        print('v2-1 failed')

    A3 = [1, 2, 10, 0]
    t = array_inverse_v2(A3)
    if t == [0, 10, 2, 1]:
        print('v2-2 passed')
    else:
        print('v2-2 failed')


test_array_inverse()
