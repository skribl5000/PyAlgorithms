arr = [10,9,4,6,10,4,12,1,0,200,11,15,2,6,9,10,113,2,6,54,2]

# direct recurse

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    barier = arr[0]
    L = []
    R = []
    M = []
    for x in arr:
        if x < barier:
            L.append(x)
        elif x == barier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        arr[k] = x
        k += 1
    return arr

print(quick_sort(arr))