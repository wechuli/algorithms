function recursiveRange(number) {
  let result = 0;
  let index = 0;
  function addRecursiveRange() {
    if (index > number) {
      return;
    }
    result += index;
    index++;
    addRecursiveRange();
  }
  addRecursiveRange();
  return result;
}

console.log(recursiveRange(10));
