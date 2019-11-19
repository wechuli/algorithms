// Write a recursive function called capitalizeFirst. Giveb an array of strings, capitalize the first letter of each string in the array

function capitalizeFirst(array) {
  const newArray = [];

  array.forEach(element => {
   let elementUpper = element[0].toUpperCase();
    let newElement = element.replace(element[0], elementUpper);
    newArray.push(newElement);
  });
  return newArray;
}

console.log(capitalizeFirst(["carc", "taco bell tel", "banana"]));
