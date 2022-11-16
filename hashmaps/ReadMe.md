## Hash maps
- define some n dimensional array
- design a hash function to return an index number out of n and store the value into array[index]
- An ideal sceanrio will be to create array of a large number lets say 1M, so almost every element will have an unique index but this could lot of space even when you dont need it.
- So we allow collisions and now will create array of array and store both key, values. We append tuple of key, value in array of array and when a collision occurs we just simple append to the array. This is called **chaining**
- Time Complexity
Best case: O(1)
Worst case: O(n)
