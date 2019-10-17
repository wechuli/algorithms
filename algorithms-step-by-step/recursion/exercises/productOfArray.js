function productOfArray(array) {
  let result = 1;
  let index = 0;
  function calculateProduct() {
    if (index === array.length) {
      return;
    }
    result = result * array[index];
    index++;
    calculateProduct();
  }
  calculateProduct();
  return result;
}

console.log(productOfArray([1, 2, 3]));
console.log(productOfArray([1, 2, 3, 10]));
