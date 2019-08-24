## When to use Objects

- When you are not concerned with order
- When you need fast access/insertion and removal
  - Insertion - O(1)
  - Removal - O(1)
  - Searching - O(N)
  - Access - O(N)

### Object Methods

- Object.keys - O(N)
- Object.values - O(N)
- Object.entries - O(N)
- hasOwnProperty - O(1)

## Why are arrays slow

- Arrays are ordered piece of data
- Use them when you need order, otherwise avoid arrays, they are relatively slow
  - Insertion - it depends
  - Removal - it depends
  - Searching - O(N)
  - Access - O(1)

### Array Operations

- push - O(1)
- pop - O(1)
- shift - O(N)
- unshift - O(N)
- concat - O(N)
- slice - O(N)
- splice - O(N)
- sort - O(N \* log N)
- forEach/map/filter/reduce/etc - O(N)
