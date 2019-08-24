//Iterative example
function collectOddValues(numberArray) {
  let result = [];
  if (numberArray.length == 0) {
    return;
  }
  for (let i = 0; i < numberArray.length; i++) {
    if (numberArray[i] % 2 !== 0) {
      result.push(numberArray[i]);
    }
  }
  return result;
}

// Recursive example

function collectOddValues2(arr) {
  let result = [];
  function helper(helperInput) {
    if (helperInput.length === 0) {
      return;
    }
    if (helperInput[0] % 2 !== 0) {
      result.push(helperInput[0]);
    }
    helper(helperInput.slice(1));
  }
  helper(arr);
  return result;
}

function collectOddValues3(arr) {
  let newArr = [];
  if (arr.length === 0) {
    return newArr;
  }
  if (arr[0] % 2 !== 0) {
    newArr.push(arr[0]);
  }
  newArr = newArr.concat(collectOddValues3(arr.slice(1)));
  return newArr;
}

console.log(collectOddValues([1, 2, 3, 4, 5, 6, 7, 8, 9]));
console.log(collectOddValues2([1, 2, 3, 4, 5, 6, 7, 8, 9]));
