// Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which contain nested objects

function nestedEvenSum(obj) {
  let runningSum = 0;
  function nestedEvenRec(nestedObjects) {
    for (let key in nestedObjects) {
      //check if we have reached the end
      if (typeof nestedObjects[key] !== "object") {
        if (
          typeof nestedObjects[key] === "number" &&
          nestedObjects[key] % 2 === 0
        ) {
          runningSum += nestedObjects[key];
        }
      } else {
        nestedEvenRec(nestedObjects[key]);
      }
    }
  }
  nestedEvenRec(obj);
  return runningSum;
}

const obj = {
  name: "him",
  all: 4045
};

var obj1 = {
  outer: 2,
  obj: {
    inner: 2,
    otherObj: {
      superInner: 2,
      notANumber: true,
      alsoNotANumber: "yup"
    }
  }
};

var obj2 = {
  a: 2,
  b: { b: 2, bb: { b: 3, bb: { b: 2 } } },
  c: { c: { c: 2 }, cc: "ball", ccc: 5 },
  d: 1,
  e: { e: { e: 2 }, ee: "car" }
};

console.log(nestedEvenSum(obj));
console.log(nestedEvenSum(obj1));
console.log(nestedEvenSum(obj2));