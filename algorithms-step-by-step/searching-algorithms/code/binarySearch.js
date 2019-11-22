/*
This function accepts a sorted array and a value
- Create a left pointer at the start of the array, and a right pointer at the end of the array
- While the left pointer comes before the right pointer
    - Create a pointer in the middle
    - If you find the value you want, return the index
    - If the value is too small, move the left pointer up
    - If the value is too large, move the right pointer down
- If you never find the value, return -1


*/

function binarySearch(array, value) {
  let leftPointer = 0;
  let rightPointer = array.length - 1;
  let currentValuePointer = Math.floor(array.length / 2);

  while (rightPointer > leftPointer) {
    if (array[currentValuePointer] == value) {
      return currentValuePointer;
    }
    if (array[leftPointer] == value) {
      return leftPointer;
    }
    if (array[rightPointer] == value) {
      return rightPointer;
    }
    if (array[currentValuePointer] > array[leftPointer]) {
      leftPointer++;
    } else if (array[currentValuePointer] < array[rightPointer]) {
      rightPointer--;
    }
    currentValuePointer = Math.floor((rightPointer - leftPointer) / 2);
  }
  return -1;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7], 2));

