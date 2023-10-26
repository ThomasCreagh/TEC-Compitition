import time
import random
from tim_sort import tim_sort as ori_tim
from tim_sort_plus import tim_sort as new_tim
from searchsort_from_insertion_prevouis import search_insertionsort as ss

l_1, l_2, l_3 = 0, 0, 0

for i in range(10):
    l = [random.randint(0, 100) for x in range(15)]
    l = [16, 44, 22, 17, 94, 46, 27, 2, 83, 48, 13, 47, 67, 37, 65]
    print(l)
    start_1 = time.perf_counter()
    test_list_1 = ss(l, 0, len(l) - 1)
    test_1 = round(time.perf_counter() - start_1, 10)
    
    start_2 = time.perf_counter()
    test_list_2 = ori_tim(l)
    test_2 = round(time.perf_counter() - start_2, 10)
    
    l.sort()

    if l != test_list_1:
        print("LIST NOT SORTED!")
        print(test_list_1)

        print(l)
        break

    if test_1 < test_2:
        l_1 += 1
    else :
        l_2 += 1
    # print(i, test_1 < test_2, test_1, test_2)

print(f"l_1: {l_1}, l_2: {l_2}")


"""
def insertionSort(arr, left, right):
    if left != right:
        if arr[left] > arr[left+1]:
            arr[left], arr[left+1] = arr[left+1], arr[left]
    for i in range(left+2, right+1):
        top = i
        bottom = top//2
        while top > bottom:
            d = (top - bottom)//2 + 1
            if arr[bottom] > arr[i]:
                top -= d
                bottom -= d
                if bottom < 1:
                    bottom = 0
                    break
            else:
                bottom += d

        arr = arr[:bottom] + [arr[i]] + arr[bottom:]
        arr.pop(i+1)
    return arr
"""