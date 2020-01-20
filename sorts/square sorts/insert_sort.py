array = [10,9,4,6,10,4,12,1,0,6]

def insert_sort(arr):
    counter = 0
    for n in range(1,len(arr)):
        if arr[n]< arr[n-1]:
            for x in range(n,0,-1):
                if arr[x] < arr[x-1]:
                    arr[x],arr[x-1] = arr[x-1],arr[x]
                counter += 1
    print(counter)
    return(arr)

print(insert_sort(array))