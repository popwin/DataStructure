
# coding: utf-8

# In[15]:

def InsertSort(x):
    """时间复杂度为o(n2)
    """
    l = len(x)
    for i in range(1,l):
        key = x[i]
        j = i-1
        while 0<=j and key<x[j] :
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
    return x



x = [10,4,1,8,3,6,-9,8]
print InsertSort(x)



