function pivotHelper(array, startIndex = 0, endIndex = array.length - 1) {
  let pivot = array[startIndex];
  let currentPivotIndex = startIndex;
  for (let i = startIndex + 1; i < array.length; i++) {
    if (pivot > array[i]) {
      currentPivotIndex++;

      [array[currentPivotIndex], array[i]] = [
        array[i],
        array[currentPivotIndex]
      ];
    }
  }
  [array[startIndex], array[currentPivotIndex]] = [
    array[currentPivotIndex],
    array[startIndex]
  ];
  //   console.log(array);
  return currentPivotIndex;
}

module.exports = {
  pivotHelper
};
// console.log(pivotHelper([9, 71, 2, 3, 6, -7, 0, 4, -94]));
// console.log(pivotHelper([4, 8, 2, 1, 5, 7, 6, 3]));
