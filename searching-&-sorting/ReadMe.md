### Binary Search
- It works like the bisection method in root finding
- Find the middle element and compare with the value that we need to check, if value>mid take second half, else take first half
- repeat this untill mid=value or low=high
- This can be achieved by both recursive and iterative methods
- Time Complexity: O(logn)
- Space Complexity: O(1)

### Bubble Sort
#### Normal way
- We keep comparing adjacent elements from zeroth to last trough a loop and exchange postitions if element to the right is smaller than lef
- keep repeating the process untill no exchange is possible

#### Efficient way
- it is same as normal way, but we take advantage of the fact that after each parse through complete list, biggest element buubles up to the end
- Now we can perform one less iteration each time, as bigger elements keep accumulating in the end

- Time Complexity: O(n^2)
- Space Complexity: O(1) as no extra lists are needed, it is an in place operation

### Merge Sort
- First the array is bisected and the mergesort function is recursively called for each left and right bisect until the further bisection is not possible. This is top down process
- Then the merge function is called which merges two arrays in a single sorted array. This works in bottom up process
- Time Complexity: O(nlogn)
- Space Complexity: O(n) n extra lists are created when we split the into 2

### Quick Sort
- First we create an pivot at end and keep comparing with first element, if first element is bigger we bring that in last.
- We keep doing until pivot reaches the point where all elements in left are smaller and on right are bigger than pivot.
- We make a recursive call for the function to repeat the same with elements on the left and right of the pivot.
- Time complexity:
  worst case: O(n^2) This is because on average case pivot comes to the middle (some elements were bigger and some smaller to the left of pivot), so it performs like merge sort divide and conquer. but when list is near sorted or reverse sorted, the means pivot reaches to first or stays last which requires more iterations.
  best case: O(nlogn) when pivot comes near middle
- Space complexity: 0(1)
