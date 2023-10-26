def sort_2(array):
    comparisons = 0
    odd, even = [], []
    for x in array:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    comparisons += 1
    if odd[0] > odd[1]:
        odd[0], odd[1] = odd[1], odd[0]
    first = 0
    last = 1

    odd, first, last, comparisons = compare(odd, 2, first, last, comparisons)
    array, _, _, comparisons = compare(odd+even, last+1, first, last, comparisons)
    return f"{array} with {comparisons} comparisons"


def compare(array, start, first, last, comparisons):
    i = start
    while i < len(array):
        comparisons += 1
        if array[last] < array[i]:
            last = i
        else:
            comparisons+=1
            if array[first] > array[i]:
                array.insert(0, array[i])
                array.pop(i+1)
                last = i
            else:
                comparisons += 1
                if array[first+1] > array[i]:
                    array.insert(first+1, array[i])
                    array.pop(i+1)
                    first = 0
                    last += 1
                else:
                    first += 1
                    i -= 1
        i+=1

    return array, first, last, comparisons




print(sort_2([5, 1, 4, 2, 10, 9, 8, 3, 7, 6]))
