// Write a function that accepts an array and a value

// Loop though the array and check if the current array is equal to the value, if it is, return the index at which the element is found. If the value is never found, return -1

function searchArrayForValue(array, value) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === value) {
      return i;
    }
  }
  return -1;
}

console.log(searchArrayForValue(["dsd", 345, "ds", 344, 45], 34));
