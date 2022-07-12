class EmptyStackError(Exception):
  pass

class Node:
  def __init__(self,value):
    self.info = value
    self.link = None

class Stack:
  def __init__(self):
    self.top = None
    
  def is_empty(self):
    return self.top == None
  
  def size(self):
    
    if self.is_empty():
      return 0
    
    count = 0
    p = self.top
    while p is not None:
      count +=1 
      p = p.link
    return count
  
  def push(self,data):
    temp = Node(data)
    temp.link = self.top
    self.top = temp
    
  def pop(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    
    popped = self.top.info
    self.top = self.top.link
    return popped


  def evaluate_postfix(postfix):
    st = Stack()
    
    
    for symbol in postfix:
      if symbol.isdigit():
        st.push( int(symbol) )
      else:
        x = st.pop()
        y = st.pop()
        
        if symbol == '+':
          st.push(y + x)
        elif symbol == '-':
          st.push(y - x)
        elif symbol == '*':
          st.push(y * x)
        elif symbol == '/':
          st.push(y / x)
        elif symbol == '%':
          st.push(y % x)
        elif symbol == '**':
          st.push(y ** x)
    return st.pop()
  
# ########################################################################################################################

exp = "231*+9-"
obj = evaluate_postfix(exp)
print(obj)




        