/*
- Break up the array into halves unitl you have arrays that are empty or have one element
- Once you have smaller sorted arrays, merge those arrays with other sorted arrays until you are back at the full length of the array
- Once the array has been merged back together, return the merged (and sorted) array
*/
const { merge } = require("./mergeSortFunction");

const myunsortedArray = [0, 3, 4, 21, 3, -43, 1, 232, 4, 3, 56, 35];

function mergeSort(array) {
  // base case to end recursion
  if (array.length === 0 || array.length === 1) {
    return array;
  }
  let divisor = parseInt(array.length / 2);
  let leftSide = array.slice(0, divisor);
  let rightSide = array.slice(divisor, array.length);
  return merge(mergeSort(leftSide), mergeSort(rightSide));
}

console.log(mergeSort(myunsortedArray));
