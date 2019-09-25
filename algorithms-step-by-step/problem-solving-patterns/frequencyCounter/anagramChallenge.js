// Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word , phrase or name formed by rearranging the letter of another such as cinema formed from iceman

let myString1 = "texttwist time";
let myString2 = "t imetwisttext ";

function anagram(arg1, arg2) {
  let str1 = arg1.toLowerCase();
  let str2 = arg2.toLowerCase();
  if (str1.length !== str2.length) {
    return false;
  }
  const letterFrequency1 = {};
  const letterFrequency2 = {};

  for (let item of str1) {
    letterFrequency1[item] = (letterFrequency1[item] || 0) + 1;
  }
  for (let item of str2) {
    letterFrequency2[item] = (letterFrequency2[item] || 0) + 1;
  }
  for (let item in letterFrequency1) {
    if (letterFrequency1[item] !== letterFrequency2[item]) {
      return false;
    }
  }
  return true;
}

console.log(anagram(myString1, myString2));
