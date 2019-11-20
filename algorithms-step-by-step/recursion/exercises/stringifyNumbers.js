// Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings.

function stringifyNumbers(object) {
  for (let key in object) {
    if (typeof object[key] === "object") {
      stringifyNumbers(object[key]);
    } else if (typeof object[key] === "number") {
      object[key] = object[key].toString();
    }
  }
}

let obj = {
  num: 1,
  test: [],
  anotherOne: [
    1,
    2,
    3,
    4,
    5,
    {
      age: 26,
      name: "Wechuli Paul",
      sencounters: 1
    }
  ],
  data: {
    val: 4,
    info: {
      isRight: true,
      random: 66
    }
  }
};

stringifyNumbers(obj);

console.log(obj);
