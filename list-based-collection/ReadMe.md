### Linked List
- Every element/node of linked list is a individual object of a class which has an attribute next that points towards the object of next element. Initially it points to none but as we append elements it points to the next.
- Every Linked list has an attribute head which is the first element.
- To append an element we have to loop through the head till the last element as unlike a normal list there is no absolute position for each element.
- More methods other than what I have written can be defined for a linked list.

### Stack
- Stack is also similar to a linked list, the elements do not have an absolute position and have a next attribute.
- But unlike linked list a stack is defined by the top/newest position
- In stack we are not interested in appending at the end but we push an element at top, so push and pop as O(1) time complexity

### Queue
- Queue is pretty straight forward, first in first out, we can use usual list methods to perform the basic peek, enqueue, dequeue methods
