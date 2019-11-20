// Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string

function collectStrings(obj) {
  const stringArray = [];

  function collectStringRec(obj) {
    for (let key in obj) {
      if (typeof obj[key] === "object") {
        collectStringRec(obj[key]);
      } else if (typeof obj[key] === "string") {
        stringArray.push(obj[key]);
      }
    }
  }
  collectStringRec(obj);
  return stringArray;
}

const obj = {
  stuff: "foo",
  data: {
    val: {
      thing: {
        info: "bar",
        moreInfo: {
          evenMoreInfo: {
            weMadeIt: "baz",
            reret: [
              {
                trere: {
                  sdsde: {
                    esdsds: ["yes", "no", 1234, 443]
                  }
                }
              },
              { arr: [1, 3, 4] }
            ]
          }
        }
      }
    }
  }
};

console.log(collectStrings(obj));
