class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        ele=self.head
        for i in range(1, position):
            ele=ele.next
        if bool(ele) and position>0:
            return ele
        else:
            return None
    
    def insert(self, new_element, position):
        ele=self.get_position(value-1)
        new_element.next=ele.next
        ele.next=new_element
    
    
    def delete(self, value):
        ele=self.get_position(value-1)
        if ele:
            ele.next=ele.next.next
        else:
            self.head=self.head.next
