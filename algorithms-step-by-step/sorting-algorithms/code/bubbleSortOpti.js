function bubbleSort(array) {
  let lengthOfArray = array.length;
  let noSwaps;
  for (let i = lengthOfArray; i > 0; i--) {
    noSwaps = true;
    for (let j = 0; j < i - 1; j++) {
      if (array[j] > array[j + 1]) {
        [array[j], array[j + 1]] = [array[j + 1], array[j]];
        noSwaps = false;
      }
    }
    if (noSwaps) break;
  }
  return array;
}

console.log(bubbleSort([1, 2, 3, 4]));
