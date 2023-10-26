import math
from random import randint as r
import time

_l = [r(0, 100) for i in range(r(4, 20))]
l = _l
print(l)
for i in range(100):
    start_1 = time.perf_counter()
    for i in range(1, len(l)):
        top = i
        bottom = top//2
        while top > bottom:
            d = (bottom - top)//2 +1
            if l[bottom] > l[i]:
                top -= d
                bottom -= d if bottom < 1 else 0
            else:
                bottom += d

        l = l[:bottom] + [l[i]] + l[bottom:]
        l.pop(i+1)

    test_1 = time.perf_counter() - start_1

    l = _l
    start_2 = time.perf_counter()
    l.sort()
    test_2 = time.perf_counter() - start_2
    print(test_1 > test_2)
    print(test_1, test_2)


"""
print(f"top, bottom: {top}, {bottom}")
        print(f"val[i], val[top]: {l[i]}, {l[bottom]}")
        if l[i] < l[bottom]: # fix this shit
            bottom //=2

        print(top, bottom)
        # print(l[(len(l[bottom:top])-1)//2], l[i])
        # if l[(len(l[bottom:top])-1)//2] > l[i]: # fix this shit
        if l[bottom] > l[i]:


        # print(f"top, bottom: {top}, {bottom}")
        # print(f"val[i], val[top]: {l[bottom]}, {l[i]} is {l[bottom] > l[i]}")
        # print(f"len, len//2, roundup: {len(l[bottom:top])}, {len(l[bottom:top])//2}, {math.ceil((len(l[bottom:top]))/2)}")
            
"""

"""
# Bullet Points
- loop over each index
- compare to half sorted
- repeat compare till done

# Pheusdo code
bottom = 0
top = 0
for indexs in the list
    while top > bottom
        if index < list[top:bottom//2]
            top //=2
        else
            bottom //=2

    pop index 
    list = [:top] + [list[index]] + [top:]
"""