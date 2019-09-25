// Write a function which takes in a string and returns count of each character in the string

function charCount(words) {
  if (!words) {
    return null;
  }
  let string = words.toLowerCase();
  const countChars = {};
  const myReg = new RegExp("[a-z0-9]");

  for (let i = 0; i < string.length; i++) {
    if (!myReg.test(string[i])) {
      continue;
    }
    if (countChars.hasOwnProperty(string[i])) {
      countChars[string[i]] += 1;
    } else {
      countChars[string[i]] = 1;
    }
  }
  return countChars;
}

console.log(
  charCount(
    "This should be fun but what about some other! interesting tezt cases , very intresting stuff 9433 indeed given by this function"
  )
);
