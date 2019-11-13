function isPalindrome(words) {
  let lengthOfString = words.length;
  for (let i = 0, j = lengthOfString - 1; i < lengthOfString; i++, j--) {
    if (words[i] !== words[j]) {
      return false;
    }
  }
  return true;
}

console.log(isPalindrome("awesome"));
console.log(isPalindrome("foobar"));
console.log(isPalindrome("tacocat"));
console.log(isPalindrome("amanaplanacanalpanama"));
console.log(isPalindrome("amanaplanacanalpandemonium"));
