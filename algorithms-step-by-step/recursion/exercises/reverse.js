// Write a recursive function called reverse which aceepts a string and returns a new string in reverse

const reverse = words => {
  let result = "";
  for (let i = words.length - 1; i >= 0; i--) {
    result += words[i];
  }
  return result;
};

function recursiveReverse(words) {
  let result = "";
  let currentIter = words.length - 1;

  function reverse() {
    if (currentIter < 0) {
      return;
    }
    result += words[currentIter];
    currentIter--;
    reverse();
  }
  reverse();
  return result;
}

console.log(reverse("Hi there"));
console.log(recursiveReverse("Hi there"));
console.log(recursiveReverse("awesome"));
console.log(recursiveReverse("rithmschool"));
