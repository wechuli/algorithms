"use strict";
// returns the digit in num at the given place value
exports.__esModule = true;
function getDigit(num, i) {
  return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
}
exports.getDigit = getDigit;
function getDigit2(num, place) {
  var numberString = num.toString();
  var strLength = numberString.length;
  if (place >= strLength) {
    return 0;
  }
  return parseInt(numberString[strLength - place - 1]);
}
function digitCount(num) {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}
exports.digitCount = digitCount;
function mostDigits(numArray) {
  var largestNumberDigitCount = 0;
  for (var i = 0; i < numArray.length; i++) {
    if (digitCount(numArray[i]) > largestNumberDigitCount) {
      largestNumberDigitCount = digitCount(numArray[i]);
    }
  }
  return largestNumberDigitCount;
}
exports.mostDigits = mostDigits;

function radixSort(nums) {
  let maxDigitCount = mostDigits(nums);

  for (let k = 0; k < maxDigitCount; k++) {
    let digitBuckets = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < nums.length; i++) {
      let digit = getDigit(nums[i], k);
      digitBuckets[digit].push(nums[i]);
    }
    nums = [].concat(...digitBuckets);
  }

  return nums;
}

console.log(radixSort([1, 233, 0, -43, 43]));
