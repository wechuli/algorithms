// Write a recursive function called flatten which accepts an array of arrrays and return a new array with all values flattened

function flatten(array) {
  const newArray = [];

  function flattenArray(unflattenedArray) {
    unflattenedArray.forEach(element => {
      if (typeof element !== "object") {
        newArray.push(element);
      } else {
        flattenArray(element);
      }
    });
  }
  flattenArray(array);
  return newArray;
}

console.log(flatten([1, 2, 3, [3]]));
console.log(flatten([1, 2, 3, [4, 5]]));
console.log(flatten([1, [2, [3, 4], [[5]]]]));
console.log(flatten([[1], [2], [3]]));
console.log(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]));
