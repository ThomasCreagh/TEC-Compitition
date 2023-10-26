def searchsort(l):
    if l[0] > l[1]:
        l[0], l[1] = l[1], l[0]
    swap = 0
    for i in range(2, len(l)):
        top = i
        bottom = top//2
        while top > bottom:
            d = (top - bottom + 1)//2 
            if l[bottom] > l[i]:
                top = bottom
                bottom -= d
                if bottom < 1:
                    bottom = 0

            else:
                bottom += d

        l = l[:bottom] + [l[i]] + l[bottom:]
        l.pop(i+1)
        swap += 1
    return l, swap
