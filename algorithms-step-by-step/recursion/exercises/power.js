// Write a function called power which accepts a base and an exponent. The function should return the power of the base to the exponent

function power(base, exponent) {
  let result = 1;
  let noOfTimes = 0;

  function powerRecursion() {
    if (noOfTimes === exponent) {
      return;
    }
    result = result * base;
    noOfTimes++;
    powerRecursion();
  }
  powerRecursion();
  return result;
}

console.log(power(3, 4));
