/*
- Start by picking the second element in the array
- Now compare the second element with the one before it and swap if necessary
- Continue to the next element and if it is in the incorrect order, iterate through the sorted portion (.i.e the left side) to place the element in the correct place
- Repeat until the array is sorted
*/

function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    let currentVal = array[i];
    for (var j = i - 1; j >= 0 && array[j] > currentVal; j--) {
      array[j + 1] = array[j];
    }
    array[j + 1] = currentVal;
  }
  return array;
}

console.log(insertionSort([34, 66, 43, 23, 0, 4, 34]));
