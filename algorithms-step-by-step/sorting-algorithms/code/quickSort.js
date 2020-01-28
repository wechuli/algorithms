const { pivotHelper } = require("./playground/pivotHelperQuicksort");

function quickSort(array, left = 0, right = array.length - 1) {
  if (left < right) {
    let pivotIndex = pivotHelper(array, left, right);
    //left
    quickSort(array, left, pivotIndex - 1);
    //right
    quickSort(array, pivotIndex + 1, right);
  }
  return array;
}

console.log(quickSort([4, 6, 9, 1, 2, 5, 3]));
