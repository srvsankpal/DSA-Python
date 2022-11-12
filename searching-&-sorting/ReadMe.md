### Binary Search
- It works like the bisection method in root finding
- Find the middle element and compare with the value that we need to check, if value>mid take second half, else take first half
- repeat this untill mid=value or low=high
- This can be achieved by both recursive and iterative methods

### Merge Sort
- First the array is bisected and the mergesort function is recursively called for each left and right bisect until the further bisection is not possible. This is top down process
- Then the merge function is called which merges two arrays in a single sorted array. This works in bottom up process
