
# coding: utf-8


class Stack():
    """stack class
       use list class in python
    """
    def __init__(self):
        self.items = []
    
    def stack_size(self):
        return len(self.items)
    
    def empty(self):
        return len(self.items) == 0
    
    def push(self,e):
        self.items.append(e)
    
    def pop(self):
        """相当于一个头朝下的stack，底部在上，头部在下，头部先出栈
           即last in first out
        """
        try:
            return self.items.pop()
        except IndexError:
            print "the stack is empty"
    
    def view(self):
        print self.items



class Tnode():
    """
    """
    def __init__(self,key,val=None,lchild=None,
                 rchild=None,parent=None):
        self.key = key
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent
        self.height = 0
    
    def has_left_child(self):
        return self.lchild
    
    def has_right_child(self):
        return self.rchild
    def is_left_child(self):#判断是该node是其父node的左孩子 还是 右孩子
        return self.parent and self.parent.lchild == self
    def is_right_child(self):
        return self.parent and self.parent.rchild == self
    
    def find_succ(self):#寻找某node的直接后继
        succ = None
        if self.has_right_child():#有右节点则直接沿左侧访问
            succ = self.rchild.find_min()
        else:#没有右节点，则根据父节点判断直接后继
            if self.parent:
                if self.is_left_child:#该节点是左孩子，则直接后继就是父节点
                    succ = self.parent
                else:#是右孩子，则要寻找除这一节点外，父节点的其他直接后继
                    self.parent.rchild = None
                    succ = self.parent.find_succ()
                    self.parent.rchild = self
        return succ
        
    def find_min(self):
        c = self
        while c.has_left_child():
            c = c.lchild
        return c



class BST():
    """
    """
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):#调用len（instance）时返回树的size
        return self.size
    
    def updateHeight(self,x):
        a = x.lchild.height if x.lchild else -1#node存在，则默认h=0，为None，则h=-1
        b = x.rchild.height if x.rchild else -1
        x.height = 1+max(a,b)#某node的高度，即从该node向下的做多node数目
    
    def updateAbove(self,x):
        while x:
            self.updateHeight(x)
            x = x.parent
            
    def search(self,key):
        if self.root:
            return self.searchIn(self.root,key,hot=None)
        else:
            self.root = Tnode(key)
            self.size += 1
            print "This is the root"
    
    def searchIn(self,v,key,hot):
        if (not v ) or (key==v.key):
            return v,hot#失败则返回None以及其父节点
        hot = v#记录当前节点，在插入和删除时用
        if key<v.key:
            return self.searchIn(v.lchild,key,hot)#递归寻找key，实际是二分法
        else:
            return self.searchIn(v.rchild,key,hot)
    
    def Insert(self,key):
        x,_hot = self.search(key)#查找失败返回None及其父节点
        if not x:#只有x是None时才在此插入一个值
            x = Tnode(key,parent=_hot)#封装为新node
            if key<_hot.key:#判断父节点的左侧还是右侧插入
                _hot.lchild = x
            else:
                _hot.rchild = x#右侧插入
            self.size += 1
            self.updateAbove(x)#插入后只影响该节点以上的高度
        return x
    
    def Remove(self,key):
        if self.size>1:
            x,_hot = self.search(key)#先找到要删除节点的位置
            if x:#非空才能删除
                self.RemoveAt(x)
                self.size -=1
                
                
    def RemoveAt(self,x):
        w = x
        succ = None
        #待删除点只有一个孩子的情况
        if not x.has_left_child():#lchild为None时执行
            succ = x.rchild
        elif not x.has_right_child():
            succ = x.lchild
        else:#待删除点有两个孩子
            w = w.find_succ()#寻找待删除节点的直接后继
            temp = x.key#value没有换，可以加入
            x.key = w.key
            w.key = temp
            succ = w.rchild#以上就是要确定succ，即新连接的node（连接到带删除node的父节点）
        
        hot = w.parent
        if w.is_left_child():#建立双向指针，左侧，待删除节点来自父节点的左孩子
            if succ:
                succ.parent = hot
                hot.lchild = succ
            hot.lchild = succ#如果两个孩子均为None，则直接用None替换
        elif  w.is_right_child():#待删除节点来自父节点的左孩子
            if succ:
                succ.parent = hot
                hot.rchild = succ
            hot.rchild = succ
        self.updateHeight(x)
        self.updateAbove(x)
        
    def travIn(self,x):#中序遍历
        s = Stack()
        while True:
            self.AlongLeft(x,s)
            if s.empty():
                break
            x = s.pop()
            print x.key
            x = x.rchild
    
    def AlongLeft(self,x,s):#沿左侧访问
        while x:
            s.push(x)
            x=x.lchild
        


if __name__=="main":
    x=BST()
    x.search(30)
    a=[20,35,17,25,31,40,10,19,21,27,37,42]
    for i in a:
        x.Insert(i)



