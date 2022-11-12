def merge(l,r,array):
    i=j=k=0
    #looping till we reach end of any list
    while i<len(l) and j<len(r):
      #comparing first element of each list(l & r) and overiding the array with the smallest of the two
        if l[i]<=r[j]:
            array[k]=l[i]
            i+=1
            k+=1
        else:
            array[k]=r[j]
            j+=1
            k+=1
            
    #there might be case where one of a list is exhausted and other is not, so handling those cases
    while i<len(l):
        array[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        array[k]=r[j]
        j+=1
        k+=1

def MergeSort(array):
    if len(array)<2:
        return array
    else:
        mid=len(array)//2
        l=array[0:mid]
        r=array[mid:]
        MergeSort(l)
        MergeSort(r)
        merge(l,r, array)

        
