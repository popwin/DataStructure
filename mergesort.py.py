
# coding: utf-8


def MergeSort(x):
    """归并算法分为：分组和排序两部分，MergeSort负责递归分组，直到单个元素为止
       无论输入怎样，复杂度为O(NlogN)
    """
    l = len(x)
    if l<=1: #递归机
        return x
    mid = int(l>>1)
    left = MergeSort(x[:mid]) #不断入栈
    right = MergeSort(x[mid:])
    return Merge(left,right)#实现组合排序

def Merge(left,right):
    """Merge部分负责将各个组进行排序组合，
       引入一个新组res，存放两个组别中较小者
    """
    res = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)
    while (i<left_len)and(j<right_len):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == left_len:
        res.extend(right[j:])
    else:
        res.extend(left[i:])
        
    return res

if __name__ == "main":
    x=[22,10,3,4,9,6,1,0]
    MergeSort(x)



