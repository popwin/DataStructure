
# coding: utf-8

# In[1]:

class List_node():
    """链表的node，封装所需元素data、前驱prev、后继succ
    """
    def __init__(self,val,p=None):
        self.data=val
        self.prev=p
        self.succ=p
    


# In[18]:

class Dlink():
    def __init__(self):
        self.head = 0
    
    def __getitem__(self,key): #重定向到字典，返回字典的值,相当于重定向“[]”
        return self.get(key)       
    
    def __setitem__(self,key,item):#重定向[],相当于字典赋值
        return self.insert_after(key,item)
        

######双链表的初始化#########        
    def initlist(self,data):
        self.head = List_node(val=None)#设置头节点为哨兵node
        self.tail = List_node(val=None)
        p = self.head#设置当前指针，这里每个指针其实就是实例
        i=0
        for item in data:
            node = List_node(item)#同样node为实例，里面包括data、prev、succ
            p.succ = node
            node.prev = p#形成双链
            p = p.succ#更改当前指针,尾部指向Null
            i+=1
        p.succ=self.tail#末尾的哨兵节点
        self.tail.prev=p
        self.size=i#求链表的size，在以后的动态操作中更新

######访问接口######
    def get(self,index):
        """从这里也可以看出链表的静态操作要从头开始，复杂度为O(n)
        """
        i = -1 #默认从哨兵头节点开始
        p = self.head
        while (p.succ != None) and (i!=index):
            p = p.succ#指针后移
            i+=1
        if i == index:
            return p
        else:
            print "exsit None"

######插入接口(按index)#####
    def insert_before(self,p,e):
        """在某node前插入一点
           可见，链表对于动态操作主要消耗在查找定位上
        """
        new_node = List_node(e)
        new_node.prev = p.prev
        new_node.succ = p
        p.prev.succ = new_node
        p.prev = new_node
        self.size+=1
        return new_node
    
    def insert(self,p,e):
        """在p指针后插入数据e，返回新节点
        
        """
        new_node = List_node(val=e)
        new_node.prev = p
        new_node.succ = p.succ
        p.succ.prev = new_node
        p.succ = new_node
        self.size += 1
        return new_node
        

####删除接口(按index删除)####
    def remove_index(self,index):
        p=self.head
        i=-1
        while (p.succ != None) and (i != index):
            i+=1
            p=p.succ
        if i==index:
            p.prev.succ=p.succ
            p.succ.prev=p.prev
            self.size -= 1
        else:
            print "exist None"
        return p.data

####删除接口（按指针删除）
    def remove(self,p):
        """删除指定节点，并返回所删除的元素
        """
        e=p.data
        p.succ.prev=p.prev
        p.prev.succ=p.succ
        del p
        self.size-=1
        return e
        
####search接口####
    def search(self,e,n,p):
        """在p节点之前的n个node中，寻找不大于e的最后一个数据
           返回该节点
        """
        while n>0:   
            p = p.prev
            if( p.data <= e ):
                break
            n -= 1
            
        if n == 0:
            return p.prev
        else:
            return p
                    
    def InsertSort(self,p,n):
        """对从p节点开始的后n个node插入排序
        """
        for l in range(n):
            self.insert(self.search(p.data,l,p),p.data)
            p=p.succ
            self.remove(p.prev)  
   
    def SelectSort(self,p,n):
        """对从p开始的n个节点(包括p)进行选择排序
        """
        head=p.prev
        tail=p
        for i in range(n):
            tail=tail.succ
        while(1<n):
            self.insert_before(tail,self.remove(self.SelectMax(head.succ,n)))
            tail=tail.prev
            n-=1
        

    def SelectMax(self,p,n):
        Max=p
        while(1<n):
            if p.succ.data>p.data:
                Max=p.succ
            p=p.succ
            n-=1
        return Max
        


# In[21]:

x.size


# In[28]:

x=Dlink()


# In[29]:

x.initlist([1,9,8,7,6,10,4,3,2,1,0])


# In[31]:

x.SelectSort(x[0],11)


# In[30]:

print x[0].data,x[1].data,x[2].data,x[3].data,x[4].data,x[5].data,x[6].data,x[7].data,x[8].data,x[9].data,x[10].data


# In[32]:

print x[0].data,x[1].data,x[2].data,x[3].data,x[4].data,x[5].data,x[6].data,x[7].data,x[8].data,x[9].data,x[10].data


# In[ ]:



