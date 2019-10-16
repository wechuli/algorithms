function factorial(number) {
  if (number < 0) {
    throw new Error("Cannot calculate factorial on -ve numbers");
  }
  if (number <= 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(-5));
