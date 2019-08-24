const process = require("process");

function sumAll(n) {
  let result = 0;
  for (let i = 0; i <= n; i++) {
    result += i;
  }
  return result;
}

function sumAll2(n) {
  return (n * (n + 1)) / 2;
}

let startTime = process.hrtime();
console.log("from loop: ", sumAll2(1000000000));
let stopTime = process.hrtime();

console.log([stopTime[0] - startTime[0], stopTime[1] - startTime[1]]);
// console.log("from smaller: ", sumAll2(10000));
