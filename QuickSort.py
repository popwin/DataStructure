
# coding: utf-8

import numpy as np
import random

class QuickSort(object):
    def __init__(self,x):
        self.x = x
        

    def main(self,lo,hi):
        """
        """
        if hi-lo<2:
            return
        mi = self.Partition(lo,hi)
        self.main(lo,mi)
        self.main(mi+1,hi)
    

    def Partition(self,lo,hi):
        """
        """
        self.swap(lo,random.randint(lo,hi-1))
        pivot = self.x[lo]#以第一个值为轴点
        mi = lo
        for i in range(lo+1,hi):
            if self.x[i]<pivot:#只要＜轴点值 则放到L的后面，即交换G的头和该值
                mi += 1
                self.swap(mi,i)
        self.swap(lo,mi)
        return mi

    def swap(self,a,b):
        temp = self.x[a]
        self.x[a] = self.x[b]
        self.x[b] = temp
    
    


if __name__ == "main":
    x=[-19, 2, 7, -14, 1, 0, -3, 6, 12, -10, 100]
    q=QuickSort(x)
    q.main(0,len(x))




