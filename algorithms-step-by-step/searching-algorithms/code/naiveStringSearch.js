/*
- Loop over the longer string
- Loop over the shorter string
- If the characters don't match, break out of the inner loop
- If the characters do match, keep going
- If you complete the inner loop and find a match increment the count of matches
- return the count

*/
function nativeStringSearch(text, searchString) {
  let searchStringLength = searchString.length;
  let textLength = text.length;
  let occurences = 0;
  for (let i = 0; i < textLength; i++) {
    for (let j = 0; j < searchStringLength; j++) {
      if (searchString[j] !== text[i + j]) {
        break;
      }
      if (j === searchStringLength - 1) {
        occurences++;
      }
    }
  }
  return occurences;
}

console.log(
  nativeStringSearch(
    "abcdefghhgfghdefwiewuedefinwuswpdefdefdefdjsdedkls'o[[[[[[[fdfkdefifdfdfdggfglkl;knflnglfkjbgnfjbgklfd;lgmfd;gklfkjldghfkljnsf;l,d'sfhjbkhjbenrk;erkewrkndedefifdfdfdggfgvcvdfsdfifdfdfdggfggd'hk;defifdfdfdggfgfgkdfkgnflkjlbc agidefifdefdefodefisdssdsfjkldfdsgfhgdeffnldfddefds6gfjdlsfgggggfdfodlfd';fd;'rhreierlerefferfef;eofkidn;sgfdigldogldokfjinfdnfdfgkd;dgkfkhghgkhgfhdgfgh;dflmhfhldf;ghmfkg;mfdg;nkjgr;ketrtrtrtrtr6re",
    "defifdfdfdggfgvcvdfsd"
  )
);
