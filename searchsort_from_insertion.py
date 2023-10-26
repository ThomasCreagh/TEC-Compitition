def search_insertionsort(arr, left, right):
    if arr[left] > arr[left + 1]:
        arr[left], arr[left + 1] = arr[left + 1], arr[left]
    for i in range(left + 2, right + 1):
        pivot = (i + 1)//2
        n = 1
        while pivot > left and pivot < i:

            # pivot = (i - pivot + 1)//2
            if arr[i] >= arr[pivot - 1]:
                if arr[i] <= arr[pivot]:
                    break
                else:
                    pivot += len(arr) - pivot//(2*n)
            else:
                pivot -= pivot//(2*n)
            n +=1

        pivot = 0 if pivot < 0 else pivot
        arr = arr[:pivot] + [arr[i]] + arr[pivot:]
        arr.pop(i+1)
            #  and arr[j] < arr[j - 1] and arr[j] > arr[j +1]
            # arr[j], arr[j - 1] = arr[j - 1], arr[j]
            # swap += 1
            # j -= 1
    return arr