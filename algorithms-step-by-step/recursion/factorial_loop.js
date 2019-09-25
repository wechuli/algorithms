function factorial(num) {
  let total = 1;
  for (let i = num; i > 1; i--) {
    total *= i;
  }
  return total;
}

function factorial(num) {
  if (num < 0) {
    throw new Error("Number must be positive");
  }
  if (num == 1 || num == 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(-5));
