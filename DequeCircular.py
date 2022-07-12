class EmptyQueueError(Exception):
  pass

class Deque:
  
  def  __init__ (self,default_size = 10):
    self.items = [None] * default_size
    self.front = 0
    self.count = 0
    
  def is_empty(self):
    return self.count == 0
  
  def size(self):
    return self.count
  
  def insert_front(self, item):
    if self.count == len(self.items):
      self.resize(2 * len(size.items))
      
    self.front = (self.front - 1) % len(self.items)
    self.items[self.front] = item
    self.count += 1
    
  def insert_rear(self, item):
    if self.count == len(self.items):
      self.resize(2*len(self.items))
      
    i = (self.front + self.count) % len(self.items)
    self.items[i] = item
    self.count += 1
    
  def delete_front(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is Empty! ")
    
    x = self.items(self.front)
    self.items[self.front] = None
    self.front = (self.front + 1) % len(self.items)
    self.count -= 1
    return x
  
  def delete_rear(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty!!")
    
    rear = (self.front + self.count - 1) % len(self.items)
    x = self.items[rear]
    self.items[rear] =None
    self.count -= 1
    return x
  
  def first(self):
    if self.is_empty():
      raise EmptyQueueError("Queue is empty")
    return self.items[self.front]
  
  def last(self):
    if self.is_empty():
      raise EmptyQueueError("Queue i-s empty")
    return self.items[rear]
  
  def display(self):
    print(self.items)
    

# Do it later!!!

