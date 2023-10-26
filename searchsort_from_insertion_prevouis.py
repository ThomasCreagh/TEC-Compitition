def search_insertionsort(arr, left, right):
    if arr[left] > arr[left + 1]:
        arr[left], arr[left + 1] = arr[left + 1], arr[left]
    for i in range(left + 2, right):
        top = i
        bottom = 0
        while top > bottom:
            # when pivot = 0??
            pivot = bottom + ((top-bottom)//2)
            if arr[pivot] < arr[i]:
                bottom = pivot
            else:
                top = pivot

        arr = arr[:top] + [arr[i]] + arr[top:]
        arr.pop(i+1)

    return arr

# print(search_insertionsort([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 20))