def array_search(arr,N,x):
    """
        array_search() - searching 'x' in array 'arr' for 0 till N-1 
        returns index of searching element
        or '-1' is x is not found
        if a few searching elements - returns first index

        arr - looked array - list
        N - looked interval - int
        x - searched value - int
    """ 
    for k in range(0,N):
        if arr[k] == x:
            return(k)
    return(-1)


# tests for example
def test_array_search():
    A1 = [1,2,3,4,5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('Test 1 Passed')
    else:
        print('Test 1 Failed')

    A2 = [-1,-2,-3,-4,-5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('Test 2 Passed')
    else:
        print('Test 2 Failed')

    A3 = [10,20,30,40,10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print('Test 3 Passed')
    else:
        print('Test 3 Failed')

test_array_search()

