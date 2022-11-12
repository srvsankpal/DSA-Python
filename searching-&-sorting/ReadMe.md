### Binary Search
- It works like the bisection method in root finding
- Find the middle element and compare with the value that we need to check, if value>mid take second half, else take first half
- repeat this untill mid=value or low=high
- This can be achieved by both recursive and iterative methods
- Time Complexity: O(logn)

### Bubble Sort
#### Normal way
- We keep comparing adjacent elements from zeroth to last trough a loop and exchange postitions if element to the right is smaller than lef
- keep repeating the process untill no exchange is possible

#### Efficient way
- it is same as normal way, but we take advantage of the fact that after each parse through complete list, biggest element buubles up to the end
- Now we can perform one less iteration each time, as bigger elements keep accumulating in the end

### Merge Sort
- First the array is bisected and the mergesort function is recursively called for each left and right bisect until the further bisection is not possible. This is top down process
- Then the merge function is called which merges two arrays in a single sorted array. This works in bottom up process
- Time Complexity: O(nlogn)
