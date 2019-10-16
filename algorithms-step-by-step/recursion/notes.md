# Recursion

One way to describe repetition within a computer program is the use of loops.An entirely different way to achieve repetition is through a process know as recursion.

Recursion is a technique by shich a function makes one or more calls to itself during execution, or by which a data structure relies upon smaller instances of the very same type od tructure in its representation.

In computing, recursion provides an elegant and powerful alternative for performing repetitive tasks. Recursion is an important technique in the study of data structures and algorithms,.

## Common Pitfalls

- No or incorrect base case
- Forgetting to return or returning the wrong thing!
- Stack overflow!

### Pure Recursion Tips

- For arrays, use methods like slice, the spread operator and concat that make copies of arrays so you do not mutate them
- Remember that strings are immutable so you will need to use methods like slice, substr or substring to make copies of strings
- To make copies of objects use Object.assign or the spread operator
