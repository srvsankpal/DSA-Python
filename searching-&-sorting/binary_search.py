#__Iterative Method__#

def binary_search(input_array, value):
    low=0
    high=len(input_array)-1
    while True:
        mid=(low+high)//2
        if value==input_array[mid]:
            return mid
        elif low==high:
            return -1
        elif value>input_array[mid]:
            low=mid+1
        elif value<input_array[mid]:
            high=mid-1
