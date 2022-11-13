#Quick Sort
def quicksort(array):
    if len(array)<2:
        return array
    l=0
    r=len(array)-1
    while l!=r:
        if array[l]>=array[r]:
            k=array[r]
            array[r]=array[l]
            array[l]=array[r-1]
            array[r-1]=k
            r-=1
        else:
            l+=1
    array[0:r]=quicksort(array[0:r])
    array[r+1:]=quicksort(array[r+1:])
    return array
