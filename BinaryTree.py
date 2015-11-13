
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



class TreeNode():
    """the single node including:
       lchild/rchild/parent/data
    """
    def __init__(self,value = None,
                 parent = None,lchild = None,rchild = None):
        self.data = value
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent
    
    def size(self):
        """the nodes number of subtree 
        """
        s=1
        if self.lchild:
            s += self.lchild.size()
        if self.rchild:
            s += self.rchild.size()
    
        return s



class BTree():
    def __init__(self,root = None):
        self.root = root
        self.items = []
    
    def insert_left(self,root,new_node):
        root.lchild = new_node
        new_node.parent = root
    
    def insert_right(self,root,new_node):
        root.rchild = new_node
        new_node.parent = root
        
    def insert(self,new_node):
        root=self.root
        if root == None:
            self.root=new_node
            print "This is the root node"
            return
        while True:
            if new_node.data <= root.data:
                if root.lchild == None:
                    self.insert_left(root,new_node)
                    break
                else:
                    root=root.lchild#以左节点作为根节点继续寻找可插入的点
            else: #插入右节点
                if root.rchild == None:
                    self.insert_right(root,new_node)
                    break
                else:
                    root = root.rchild
    
    def traverse(self,node):
        if  node == None: #if node is None return 
            return
        self.items.append(node.data)
        #x.append(node.data)
        self.traverse(node.lchild)
        self.traverse(node.rchild)
    
    def travPre(self,x):
        s=Stack()
        if x:
            s.push(x)
        while not (s.empty()):
            x=s.pop()
            print x.data #visit the data of root
            if x.rchild:
                s.push(x.rchild)
            if x.lchild:
                s.push(x.lchild)
    
    def AlongLeft(self,x,s):
        while x:
            s.push(x)
            x=x.lchild

    def travIn(self,x):
        s=Stack()
        while True:
            self.AlongLeft(x,s)
            if (s.empty()):
                break
            x=s.pop()
            print x.data
            x=x.rchild
        


if __name__=='main':
    x=BTree()
    l=[0,1,9,2,6,11,3,2,7,9,13]
    for item in l:
        x.insert(TreeNode(value=item))

    print x.travIn(x.root)





