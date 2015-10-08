
# coding: utf-8
# author = popwin 

def bubble(x,low,high):
    """冒泡算法主体，返回最后一次比较的位置
       避免重复比较已排序部分
    """
    last = low
    while(low<high):
        if x[low]>x[low+1]:
            last = low + 1
            temp = x[low+1]
            x[low+1] = x[low]
            x[low] = temp
        low += 1
    return last

def BubbleSort(x,low,hi):
    """无论如何，冒泡算法的最坏复杂度都是O（n2）
    """
    while(low<hi):
        hi=bubble(x,low,hi)





