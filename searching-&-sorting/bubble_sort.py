#normal way
def bubblesort(array):
    while True:
        flag=0
        for i in range(len(array)-1):
            if array[i+1]<array[i]:
                const=array[i]
                array[i]=array[i+1]
                array[i+1]=const
                flag+=1
        if not bool(flag):
            return array
     
#we know after each parsing through list the biggest element bubbles up to the end, so we can perform one less iteration each time
def bubblesort(array):
    k=0
    while True:
        flag=0
        for i in range(len(array)-1-k):
            if array[i+1]<array[i]:
                const=array[i]
                array[i]=array[i+1]
                array[i+1]=const
                flag+=1
        k+=1
        if not bool(flag):
            return array
