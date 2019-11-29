/*
- Start looping from the end of the array towards the start with a variable called i
- Start an inner loop with a variable called j from the beginning until i-1
- If arr[j] is greater than arr[j+1], swap those two values!
- Return the sorted array
*/

function bubbleSort(array) {
  let lengthOfArray = array.length;
  for (let i = lengthOfArray; i > 0; i--) {
    for (let j = 0; j < i - 1; j++) {
      if (array[j] > array[j + 1]) {
        [array[j], array[j + 1]] = [array[j + 1], array[j]];
      }
    }
  }
  return array;
}

console.log(
  bubbleSort([1, 3243, 554, 346, 75, 44, -1, -1.54, -1.54, 3423, 46, 78, 56])
);
// console.log(bubbleSort([1, 2, 3, 4, 5, 90, 1, 2, 2]));
