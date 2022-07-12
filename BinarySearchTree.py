class TreeEmptyError(Exception):
  pass

class Node:
  def __init__(self,value):
    self.info = value
    self.lchild = None
    self.rchild = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def is_empty(self):
    return self.root == None
  
  def insert(self,x):
    self.root = self._insert(self.root, x)
    
  def _insert(self,p,x):
    if p is None:
      p = Node(x)
    elif x < p.info:
      p.lchild =self._insert(p.lchild, x)
    elif x > p.info:
      p.rchild = self._insert(p.rchild, x)
    else:
      print(x, " already present in the tree")
    return p
  
  def insert1(self,x):
    p = self.root
    par = None
    while p is not None:
      par = p
      if x < p.info:
        p = p.lchild
      elif x > p.info:
        p = p.rchild
      else:
        print(x + " already present in the tree")
        return 
      
      temp = Node(x)
      
      if par == None:
        self.root = temp
      elif x < par.info:
        par.lchild = temp
      elif x > par.info:
        par.rchild = temp
  
  def search(self,p,x):
    if p is None:
      return None #Key not found
    if x < p.info :
      return self._search(p.lchild, x)
    if x  > p.info:
      return self._serach(p.rchild, x)
    return p
  
  def search1(self,x):
    p = self.root
    while p is not None:
      if x < p.info:
        p = p.lchild
      elif x > p.info:
        p = p.rchild
      else:
        return True
    return False
    
  def delete(self,x):
    self.root = self._delete(self.root,x)
    
  def _delete(self, p , x):
    if p is None:
      print(x," not found")
      return p
    
    if x < p.info:
      p.lchild = self._delete(p.lchild, x)
    elif x > p.info :
      p.rchild = self._delete(p.rchild, x)
    else:
      if p.lchild is not None and p.rchild is not None:
        s = p.rchild
        while s.lchild is not None:
          s = s.lchild
        p.info = s.info
        p.rchild = self._delete(p.rchild, s.info)
      else:
        if p.lchild is not None:
          ch = p.lchild
        else:
          ch = p.rchild
        p = ch
    return p
  
  def delete1(self,x):
    p = self.root
    par = None
    
    while p is not None:
      if x == p.info:
        break
      
      par = p
      if x < p.info:
        p = p.lchild
      else:
        p = p.rchild
      
      
      if p == None:
        print(x," not found")
        return 
#Complete it fast !!!!


      
      
        
     