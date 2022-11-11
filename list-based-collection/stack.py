import linkedlist as ll

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
  def __init__(self, top_element):
    self.stack=ll.LinkedList(top_element)
    
   def push(self,new_element):
    new_element.next=self.stack.head
    self.stack.head=new_element
    
    def pop(self):
      try:
        first_ele=self.stack.head
        self.stack.head=self.stack.head.next
        first_ele.next=None
       except:
        raise
