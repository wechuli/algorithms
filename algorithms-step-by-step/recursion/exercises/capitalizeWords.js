// Write a function called capitalizeWords. Given an array of words, returns a new array containing each word

function capitalizeWords(words) {
  for (let i = 0; i < words.length; i++) {
    words[i] = words[i].toUpperCase();
  }
  return words;
}

console.log(capitalizeWords(["i", "am", "learning", "recursion"]));
