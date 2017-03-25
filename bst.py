
#A simple class to make nodes for the tree, the nodes will have PARENT,LEFT-CHILD,RIGHT-CHILD and Value
class node(object):
    def __init__(self,value):
        self.left=None
        self.right=None
        self.parent=None
        self.value=value
        
#This class BST will implement a binary search tree, the tree will follow, as suggested by its name, a BST's property.        
class BST(object):
    #Constructor to initialize BST by making a root node in the tree.Root node will have no value initially.
    def __init__(self,nodes):
        self.root=node(None)
        self.nodes=nodes     
        self.add_node(self.nodes)

    def add_node(self,nodes):
        for n in nodes:
            self.insert(n)


    def insert(self,n):
        temp_node=node(n)
        x=self.root
        y=None
        while x!=None:
            y=x
            if temp_node.value<x.value:
                x=x.left
            else:
                x=x.right
        temp_node.parent=y
        if y.value==None:
            self.root=temp_node
        elif temp_node.value<y.value:
            y.left=temp_node
        else:
            y.right=temp_node
     

            
#TRAVERSING PARTS
    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            print x.value
            self.inorder_walk(x.right)
    def pre_order(self,x):
        if x is not None:
            print x.value
            self.pre_order(x.left)
            self.pre_order(x.right)
    def post_order(self,x):
        if x is not None:
            self.post_order(x.left)
            self.post_order(x.right)
            print x.value
            
#Finding the minimum and maximum values of the BST
    def minimum(self,node1):
        x=node1
        if x==None:
            return x
        else:
            while(x.left!=None):
                x=x.left
            return x.value
    def maximum(self,node1):
        x=node1
        if x==None:
            return x
        else:
            while(x.right!=None):
                x=x.right
            return x.value
        
#Getting the root value of the BST
    def get_root(self):
        return self.root.value
    
#searching the particular value node
    def search_node(self,val):
        k=self.root
        if k.value==val:
            return k
        else:
            while k.value!=val:
                if k.value>val: k=k.left
                else:
                    k=k.right
            return k

#a function to return the max value between two node values
    def get_Max_element(self,low,high):
        k=self.search_node(low)
        temp=0
        if k.parent!=None:
            while(k!=self.root and k.parent.value<high ):
                k=k.parent
                if temp<k.value:    temp=k.value

        k=k.right
        temp=k.value
        while k!=None and k.value!=high:
            if k.value<high:
                k=k.right
                temp=k.value
            else:
                temp=k.value
                k=k.left
        if temp<high:
            return high
        else:
            return temp

#node deletion of the tree
    def transplant(self,node1,node2):
        if node1.parent==None:
            self.root=node2
        elif node1==node1.parent.left:
            node1.parent.left=node2
        else:
            node1.parent.right=node2
        if node2!=None:
            node2.parent=node1.parent

    def delete_node(self,z):
         k=self.search_node(z)
         if k.left==None:
             self.transplant(k,k.right)
         elif k.right==None:
             self.transplant(k,k.left)
         else:
             y=self.search_node(self.minimum(k.right))
             if y.parent!=k:
                 self.transplant(y,y.right)
                 y.right=k.right
                 y.right.parent=y
             self.transplant(k,y)
             y.left=k.left
             y.left.parent=y

#to calculate the height of the tree             
    def cal_height(self,root,height):
        if root==None:
            return height-1
        else:
            return max(self.cal_height(root.left,height+1),self.cal_height(root.right,height+1))
            
nodes=[18,36,9,6,12,10,1,8]
first_bst=BST(nodes)

print "Inorder Traversing"
first_bst.inorder_walk(first_bst.root)
print "post_order"
first_bst.post_order(first_bst.root)
print "BST's lowest value:-"+str(first_bst.minimum(first_bst.root))
print "BST's highest value:-"+str(first_bst.maximum(first_bst.root))
print "Root-value:-"+str(first_bst.get_root())
print first_bst.get_Max_element(1,10)
first_bst.delete_node(9)
first_bst.inorder_walk(first_bst.root)

print first_bst.cal_height(first_bst.root,0)
