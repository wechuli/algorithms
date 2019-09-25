const array = [1, 2, 3, 2];
const arraySquared = [9, 1, 4, 4];

function same(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    if (arr2.indexOf(arr1[i] ** 2) === -1) {
      return false;
    }
    console.log(arr2);
    arr2.splice(arr2.indexOf(arr1[i] ** 2), 1);
  }
  return true;
}

console.log(same(array, arraySquared));
