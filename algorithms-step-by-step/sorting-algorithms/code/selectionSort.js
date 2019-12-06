/*
- Store the first element as the smallest value you've seen so far
- Compare this item to the next item in the array until you find a smaller number
- If a smaller number is found, designate that smaller number to be the new minimum and continue unti the end of the array.
- If the minimum is not the value(index) you initially began with, swap the two values
- Repeat this with the next element until the array is sorted

*/

function selectionSort(array) {
  let lengthOfArray = array.length;
  for (let i = 0; i < lengthOfArray; i++) {
    let smallestIndex = i;
    for (let j = i + 1; j < lengthOfArray; j++) {
      if (array[j] < array[smallestIndex]) {
        smallestIndex = j;
      }
    }
    if (smallestIndex !== i) {
      [array[smallestIndex], array[i]] = [array[i], array[smallestIndex]];
    }
  }
  return array;
}

let unSortedArray = [10, 8, 5, 1, 2, 4, 6, 6, 545, 4, 23, 56, 6745, 434, 32, 4];
let anotherUnsortedArray = [10, 1, 2, 20];
console.log(selectionSort(unSortedArray));
console.log(selectionSort(anotherUnsortedArray));
