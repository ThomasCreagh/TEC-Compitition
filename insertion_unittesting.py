import time
from searchsort import searchsort
from straight_inserstionsort import straight_insertionsort

for i in range(2, 3):
    l = [x for x in range(i)[::-1]]
    l = [79, 37, 80, 100, 49, 16, 25, 12, 96, 15, 9, 79, 54, 47, 58, 100, 35, 57, 83, 80, 52, 55, 95, 87, 61, 17, 63, 5, 90, 58, 32, 17]
    start_1 = time.perf_counter()
    test_list, swap_amount_1 = searchsort(l)
    test_1 = time.perf_counter() - start_1
    # print(test_1)

    l = [x for x in range(i)[::-1]]
    l = [79, 37, 80, 100, 49, 16, 25, 12, 96, 15, 9, 79, 54, 47, 58, 100, 35, 57, 83, 80, 52, 55, 95, 87, 61, 17, 63, 5, 90, 58, 32, 17]
    start_2 = time.perf_counter()
    swap_amount_2 = straight_insertionsort(l)[1]
    test_2 = time.perf_counter() - start_2
    # print(test_2)

    # l = [x for x in range(i)[::-1]]
    # start_3 = time.perf_counter()
    # l.sort()
    # test_3 = time.perf_counter() - start_3
    # # print(test_3)



    print(f"Test with length of {i}:")
    # print(f"List: {[x for x in range(i)[::-1]]}")
    print(f"Swap amount (1), (2): {swap_amount_1}, {swap_amount_2}")
    print(f"Times (1), (2): {test_1}, {test_2}")
    # print(f"Improvement: {test_1 < test_2}")


    # if test_1 < test_2 and test_1 < test_3:
    #     print("test 1:", test_1)
    # elif test_2 < test_1 and test_2 < test_3:
    #     print("test 2:", test_2)
    # elif test_3 < test_1 and test_3 < test_1:
    #     print("test 3:", test_3)
    # else:
    #     print("ermm")