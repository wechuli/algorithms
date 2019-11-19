// Write a recursive function called someRecursive which accepts an array and a callback. The function returns true if a single value in the array returs true when passed to the callback. Otherwise it returns false

const isOdd = number => number % 2 !== 0;

function someRecursive(array, callback) {
  return array.some(callback);
}

console.log(someRecursive([1, 2, 3, 4], isOdd));
console.log(someRecursive([4, 6, 8, 9], isOdd));
console.log(someRecursive([4, 6, 8], isOdd));
console.log(someRecursive([4, 6, 8], val => val > 10));
