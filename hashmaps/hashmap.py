#simple hashmap implementation in python, without collision
class hashmap:
    def __init__(self):
        self.max=100
        self.array=[None for i in range(self.max)]
    
    #This hash function works using sum of ascii of each chars
    def get_hash(self, key):
        total=0
        for ele in key:
            total+=ord(ele) #ord gives ascii value for input
        return total%self.max
    
    def __setitem__(self, key, val): #operator overloading
        index=self.get_hash(key)
        self.array[index]=val
        
    def __getitem__(self, key): #operator overloading
        index=self.get_hash(key)
        return self.array[index]
  
  #design with collisions
  class hashmap:
    def __init__(self):
        self.max=100
        self.array=[[] for i in range(self.max)]
    
    def get_hash(self, key):
        total=0
        for ele in key:
            total+=ord(ele) #ord gives ascii value for input
        return total%self.max
    
    def __setitem__(self, key, val): #operator overloading
        index=self.get_hash(key)
        
        for i,ele in enumerate(self.array[index]): #in case we want to change the value of existing key
            if ele[0]==key:
                self.array[index][i]=(key,val)
                break
        else:
            self.array[index].append((key,val)) #if key doesnt exists appending to the list at that index
        
    def __getitem__(self, key): #operator overloading
        index=self.get_hash(key)
        for ele in self.array[index]:
            if ele[0]==key:
                return ele[1]
 
#This is how the array looks 
# [[],
#  [],
#  [('m', 100), ('march 6', 50)],
#  [],
#  [('march 8', 40)],.......]
