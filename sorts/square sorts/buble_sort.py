arr = [10,9,4,6,10,4,12,1,0,6]

def buble_sort(arr):
    for n in range(len(arr)):
        for x in range(1,len(arr)-n):
            if arr[x] < arr[x-1]:
                arr[x],arr[x-1] = arr[x-1],arr[x] 
    return(arr)

print(buble_sort(arr))