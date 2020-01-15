/*
- create an empty array, take a look at the smallest values in each input array
- while there are still values we haven't looked at
    - if the value in the first array is smaller than the value in the second array, push the value in the first array into our results and move on to the next value in the first array
    - if the value in the first array is larger than the value in the second array, push the value in the second array into our results and move on to the next value in the second array
    - once we exhaust one array, push in all remaining values from the other array

*/

input1 = [
  34,
  67,
  78,
  90,
  97,
  100,
  101,
  102,
  103,
  104,
  105,
  107,
  107,
  108,
  200,
  201
];
input2 = [-34, 0, 5, 12, 89, 98, 1002, 4564, 5000];

function merge(array1, array2) {
  let results = [];
  let i = 0;
  let j = 0;
  while (i <= array1.length && j <= array2.length) {
    //If both arrays have reached the end of the loop, break out of the loop
    if (i === array1.length && j === array2.length) {
      break;
    }
    // If we have reached the end of array1 and array2 has more elements still, copy the remaining elements of array2 into the results and then break
    if (i === array1.length) {
      results.push(...array2.slice(j));
      break;
    }
    // If we have reached the end of array2 and array1 has more elements still, copy the remaining elements of array1 into the results and then break
    if (j === array2.length) {
      results.push(...array1.slice(i));
      break;
    }

    if (array1[i] <= array2[j]) {
      results.push(array1[i]);
      i++;
    } else {
      results.push(array2[j]);
      j++;
    }
  }
  return results;
}

module.exports = {
  merge
};

// console.log(mergeSortFunction(input1, input2));
// console.log(mergeSortFunction([1, 23, 56], [0]));
// console.log(mergeSortFunction([0], [0]));
// console.log(mergeSortFunction([], []));
// console.log(mergeSortFunction([], [1]));
// console.log(mergeSortFunction([1], []));
