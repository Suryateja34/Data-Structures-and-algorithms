class EmptyStackedError(Exception):
  pass

class StackFullError(Exception):
  pass
 
class Stack:
  def __init__(self,max_size = 10):
    self.items = [None] * max_size
    # This will create a list which has no of elements equal to max_size and each element in this list is None
    self.count = 0
    
  def size(self):
    return self.count
  
  def is_empty(self):
    return self.count == 0
  
  def is_full(self):
    return self.count == len(self.items) 
  
  def size(self):
    return len(self.items)
  
  def push(self,x):
    # When you push elements into the list it will replace the already exsisting elements which has the value of none and replace them with with the value we provided 
    if self.is_full():
      raise StackFullError("Stack is full, can't push ")
    
    self.items[self.count] = x
    self.count += 1
  
  def pop(self):
    # When you pop an element from the list then it is replaced it with None
    
    if self.is_empty():
      raise EmptyStackError("Stack is empty, can't pop ")
    
    x = self.items[self.count - 1]
    self.items[self.count - 1] = None
    self.count -= 1
    return x
  
  def peek(self):
    if self.is_empty():
      raise EmptyStackedError("Stack is empty")
    return self.items[self.count - 1]
  
  def display(self):
    print(self.items)
    
##########################################################################################################################

if __name__ == "__main__":
  st = Stack()
  
  while True:
    print("1: Push")
    print("2: Pop")
    print("3: Peek")
    print("4: Size")
    print("5: Display")
    print("6: Quit")
    
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
      x = int(input("Enter the element to be pushed : "))
      st.push(x)
      
    elif choice == 2:
      x = st.pop()
    
    elif choice == 3:
      print("Elements at the top is : " , st.peek())
    
    elif choice == 4:
      print("Size of the stack : " , st.size())
      
    elif choice == 5:
      st.display()
      
    elif choice == 6:
      break
    
    else:
      print("Option is wrong")
    print()
      
    