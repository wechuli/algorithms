// Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array thst includes both values that sum to zero or undefined if a ppair does not exist
array = [-4, -3, -2, -1, 0, 1, 2, 5];

// Naive solution
function sumZero(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
  return undefined;
}

function sumZeroOptimized(arr) {
  let left = 0;
  let right = arr.length - 1;
  while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
  return undefined;
}

console.log(sumZero(array));
console.log(sumZeroOptimized(array));
