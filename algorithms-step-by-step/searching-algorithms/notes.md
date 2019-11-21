# Searching Algorithms

## Objectives

- Describe what a searching algorithm is
- Implement linear search on arrays
- Implement binary search on sorted arrays
- Implement a naive string searching algorithm
- Implement the KMP string searching algorithm

### Linear Search

Given an array, the simplest way to search for a value is to look at every element in the array and check of it's the value we want.

### Binary Search

Binary search is a much faster form of search. Rather than eliminating one element at a time, you can eliminate half of the remaining elements at a time. In computer science, binary search, also known as half-interval search, logarithmic search or binary chop is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

Binary search only works on sorted arrays
