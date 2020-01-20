arr = [10,9,4,6,10,4,12,1,0,6]

def choise_sort(arr):
    for n in range(len(arr)-1):
        for x in range(n,len(arr),1):
            if arr[x]<arr[n]:
                arr[x],arr[n] = arr[n],arr[x]
    return(arr)
print(choise_sort(arr))