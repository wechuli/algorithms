import { getDigit, digitCount, mostDigits } from "./radixHelpers";

/*
- Define a function that accepts a list of numbers
- Figure out how many digits the largest number has
- Loop from k=0 up to the largest number of digits
- For each iteration of the loop:
    - create buckets for each digit(0 to 9)
    - place each number in the corresponding bucket on it kth digit
- replace our existing array with values in our buckets starting with 0 and going up tp 9
- return the list at the end

*/

function radixSort(numArray: number[]): number[] {
  let maxIterations = mostDigits(numArray);

  for (let i = 0; i < maxIterations; i++) {
    let buckets: any = {
      0: [],
      1: [],
      2: [],
      3: [],
      4: [],
      5: [],
      6: [],
      7: [],
      8: [],
      9: []
    };
    for (let j = 0; j < numArray.length; j++) {
      let bucketPosition = getDigit(numArray[j], i);
      console.log(buckets[bucketPosition].push(numArray[j]));
    }
    console.log(buckets);
  }
  return numArray;
}

radixSort([13, 443, 44, -4, 0, 33]);
