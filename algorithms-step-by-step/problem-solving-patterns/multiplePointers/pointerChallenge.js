// Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.

function countUniqueValues(array) {
  let arrLength = array.length;
  if (arrLength == 0) {
    return 0;
  }
  let count = 1;
  for (let i = 0; i < arrLength - 1; i++) {
    if (array[i + 1] > array[i]) {
      count += 1;
    }
  }
  return count;
}



console.log(countUniqueValues([1, 1, 1, 1, 1, 2]));
console.log(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]));
console.log(countUniqueValues([-2, -1, -1, 0, 1]));
