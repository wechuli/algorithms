// returns the digit in num at the given place value

export function getDigit(num: number, i: number): number {
  return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
}
function getDigit2(num: number, place: number): number {
  let numberString: string = num.toString();
  let strLength: number = numberString.length;
  if (place >= strLength) {
    return 0;
  }

  return parseInt(numberString[strLength - place - 1]);
}

export function digitCount(num: number): number {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

export function mostDigits(numArray: number[]): number {
  let largestNumberDigitCount = 0;
  for (let i = 0; i < numArray.length; i++) {
    if (digitCount(numArray[i]) > largestNumberDigitCount) {
      largestNumberDigitCount = digitCount(numArray[i]);
    }
  }

  return largestNumberDigitCount;
}
