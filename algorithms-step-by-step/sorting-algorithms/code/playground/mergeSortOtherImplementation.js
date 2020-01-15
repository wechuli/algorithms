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

function merge(arr1, arr2) {
  let results = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length && arr2.length) {
    if (arr2[j] >= arr1[i]) {
      results.push(arr1[i]);
      i++;
    } else {
      results.push(arr2[j]);
      j++;
    }
  }
  while (i < arr1.length) {
    results.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    results.push(arr2[j]);
    j++;
  }
  return results;
}

console.log(merge(input1, input2));
console.log(merge([1, 23, 56], [0]));
