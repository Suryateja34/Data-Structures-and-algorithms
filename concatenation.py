class Node:
  def __init__(self,value):
    self.info = value
    self.link = None
  
class SingleLinkedList :
  def __init__(self):
    self.start = None 
  
  def display_list(self):
    if self.start is None:
      print("List is empty")
      return
    else:
      # print("List is :  ")
      p = self.start
      while p is not None:
        print(p.info , " " , end = ' ')
        p = p.link
      print()
      
  def insert_in_beginning(self,data):
    temp = Node(data)
    temp.link = self.start
    self.start = temp
  
  def insert_at_end(self,data):
    temp = Node(data)
    if self.start is None:
      self.start = temp
      return
    
    p = self.start
    while p.link is not None :
      p = p.link
    p.link = temp
    
  def create_list(self):
    i = 0
    n = input("Enter the number of nodes : ")
    try:
        n = int(n)
        if n == 0:
          return
        while i < n:
          data = input("Enter the element to be inserted : ")
          try:
            data = int(data)
            i += 1
            self.insert_at_end(data)
            
          except:
            print("Invalid Input!!! Please enter only integers.")
    except:
      print("Invalid Input!! Please enter any integer.")
  
  def concatenate(self,list2):
    if self.start is None:
      self.start = list2.start
      return
    
    if list2.start is None:
      return 
    
    p = self.start
    while p.link is not None:
      p = p.link
    
    p.link = list2.start
##########################################################################################################################


list1 = SingleLinkedList()
list2 = SingleLinkedList()

print("Enter the first list")
list1.create_list()
print("Enter second list ")
list2.create_list()

print("First list is:- ");list1.display_list()
print("Second list :- ");list2.display_list()

list1.concatenate(list2)
print("List after concatenation is : ");list1.display_list()



      