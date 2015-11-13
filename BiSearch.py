
# coding: utf-8


def BiSearch(x,e):
    """
    """
    low = 0
    hi = len(x)
    while (low<hi):
        mi = (low+hi)//2
        if e<x[mi]:
            hi = mi
        elif x[mi]<e:
            low = mi +1
        else:
            return mi
    return -1


x=[1,2,3,4,5,6,7,7,8,9,10]

print BiSearch(x,5)




