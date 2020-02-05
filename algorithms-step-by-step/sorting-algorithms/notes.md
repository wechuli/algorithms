# Sorting Algorithm

## What is Sorting ?

Sorting is the process of rearranging the items in a collection so that the items are in some kind of order.

### Why Learn Sorting

- Sorting is an incredibly commo task, so it's good to know how it works
- There are many different ways to sort things, and different techniques have their own advantage and disadvantages

## Bubble Sort

A sorting algorithm where the largest values bubble up to the top!

Big OH Complexity for Bubble Sort = O(N^2)

## Selection Sort

Similar to bubble sort, but instead of first placing large values into sorted position, it places small values into sorted position.
Big Oh Complexity for Selection Sort = O(N^2)

## Insertion Sort

Builds up the sort by gradually creating larger left half which is always sorted.

## Merge Sort

- It's a combination of two things - merging and sorting
- Exploits the fact that arrays of 0 or 1 element are always sorted
- Works by decomposing an array into smaller arrays of smaller arrays of 0 or 1 elements, then building up a newly sorted array

## Quick Sort

- Like merge sort, exploits the fact that arrays of 0 or 1 element are always sorted
- Works by selecting one element (called the "pivot") and finding the index where the pivot should end up in the sorted array
- Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot


## Radix Sort

Radix sort is a special sorting algorithm that works on lists of numbers. It never makes comparisons between elements. It exploits the fact that information about the size of a number is encoded in the number of digits. More digits means a bigger number