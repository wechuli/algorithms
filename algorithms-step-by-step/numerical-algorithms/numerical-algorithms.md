# Numerical Algorithms

Numerical algorithms calculate numbers. The perform such tasks as radomizing values, breaking numbers into their peime factors, finding greatest common divisors and computing geometric areas.

## Randmozing Data

Randomization plays an important role in many applications. It lets a program simulate random processes, test algorithms to see how many behave with random inputs and search for solutions to difficult problems

### Generating Random Values

Most application use _pseudorandom number generator_(PRNG)
One simple and common method of creating pseudorandom numbers is a linear congruinetial generator, which uses the following relationship to generate numbers:

![](lcg.PNG)


Usually programs need to use a fair PRNG. A fair PRNG is one that produces all of its possible outputs with the same probability. A PRNG that is unfair is called a biased PRNG

### Randomizing Arrays


### Generating Nonuniform Distributions

### Making Random Walks

A random walk is a path generated at random. Usually the path consists of steps with a fixed length that move the path along some sort of lattice, such as a rectangular or hexagoinal grid.

### Making Self-Avoiding Walks

A random self-avoiding walk, which is also called a non-self-intersecting walk is a randomwalk that is not allowed to intersect itselg.Usually the walk continues on a finite lattice unitl no more moves are possible.

### Finding Greatest Common Divisors

The greatest common divisor(GCD) of two integers is the largets integer that evenly divides both of the numbers.