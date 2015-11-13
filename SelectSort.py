
# coding: utf-8

# In[16]:

def SelectSort(x):
    """
    """
    l = len(x)
    while 0<l:
        maxindex = l-1#最后一个值初始化为最大值
        for i in range(l):
            if x[i]>x[maxindex]:
                maxindex = i
        if maxindex != l-1:
            x[l-1],x[maxindex] = x[maxindex],x[l-1]           
        l -= 1
    return x


# In[19]:

x = [-10,0,4,1,8,3,6,-9,8]


# In[20]:

print SelectSort(x)


# In[ ]:



