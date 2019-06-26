# Algorithm Analysis

Simply puy, a data structure is a systematic way or organizing and accessing data, and an algorithm is a step-by-step procedure for performing some task in a finite amount of time. To be able to classify some data structures and algorithms as good, we must have precise ways of analyzing them.

## Stuff that can influence the running time of an algorithm

- input size
- hardware environment
- software environment
- implementation of the code (e.g either compiled or interprated)

In spite of the possible variations that come from different environmental factors, we would like to focus on the relationship between the running time of an algorithm and the size of its input. We are interested in characterizing an algorithm's running time as a function of the input size.

## Experimental Studies

If an algorithm has been implemented, we can study its running time by executing. An elapsed time measured is a decent reflection of the algorithm efficiency but it is by no means perfect. The rime function measures relative to what is known as the 'wall clock'. Because many processes share use of a computer'c central processing unit(or CPU), the time elaspsed will depend on what other processes are running on the computer used by the algorithm. A fairer metric is the number of CPU cycles that are used by the algorithm.This can be determined using the clock function of the time module, but even this measure might not be consistent if repeating the identical algorithm on the identical input, and its granularity will depend upon the computer system. Python includes a more advanced module, named timeit, to help automate such evaluations with repetition to account for such variance among trials.

### Challenges of Experimental Analysis

While experimental studies of running times are valuable, especially when fine tuning production-quality code, there are 3 major limitations to their use for algorithm analusis

- Experimental running times of two algorithms are difficult to direclty compare unless the experiments are performes in the same hardware and software environments
- Experiments can be done only on alimited set of test inputs; hence they leave out the running times of inputs not included in the experiment
- Am algorithm must be fully implemented in order to execute it to study its running time experimentally

Our goal is to develop an approach to analyzing the efficiecy of algorithms that:

- Allow us to evaluate the relative efficiency of any two algorithms in a way that is independent of the hardware and sofware environment
- Is performed by studying a high-level description of the algorithm without need for implementation
- Takes into account all possible inputs

## Moving Beyond Experimental Analysis

### Counting Primitive Operations

We define a set of primitive operations such as the following - Assigning an identifier to an object - Determingin the object associated with an identifier - Performing an arithmetic operation - Comparing two numbers - Accessing a single element is a list or array - Calling a function(excluding operations executed within the function) - Returning from a function
Formally, a primitive operation corresponds to a low-level instruction with an execution time that is constant.
This operation count will correlate to an actual running time in a specific computer, for each primitve operation corresponds to a constant number of instructions and there are only a fixed number of primitive operations

### Measuring Operations as a function of Input Size

To capture the order of growth of an algorithm's running time, we will associate with each algorithm, a function f(n) that characterizes the number of primitive operations that are performed as a function of the input size n.

### Focusing on the Worst-Case Input

An algorithm may run fatser on some inputs yhan it does on others of the same size. Thus we may wish to express the running time of an algorithm as the function of the input size obtained by taking the average over all possible inputs of the same size.Unfortunately, such an average-case analysis is typically quite challenging. As a result, we will characterize runninf times in terms of the worst case, as a function of the input size, n, of the algorithm. Worst case analysis is much easier than average-case analysis, as it requires only the ability to identify the worst-case input which is often simple.Also, this approach typically leads to better algorithms.

## Important Functions Used in the analysis of Algorithms.

### The Constant Function

The simplest function we can think of is the constant function.

    f(n) = c

That is, for any argument n, the constant function f(n) assigns the value c, therefore, no matter what value of n is; f(n) will always be equal to the constant value c.

    f(n) = cg(n)
    g(n) = 1

### The Logarithmic Function

One of the interesting and sometimes even surprising aspects of the analysis of data structures and algorithms is the ubiquitous presence of the logarithmic function

    x = logb n if and only if bx = n.

The value b is known as the base of the logarithm. The most common base for the logarithm function in computer science is 2 as computers store integers in binary, and because a common operation in many algorithms is to repeatedly divide an input in half.

#### Propositional Logarithmic rules

    logb(ac) = logba + logbc
    logb(a/c) = logba - logbc
    logb(a^c) = clogba
    logba = logda/logdb
    b^(logd1) = a^(logdb)

By convention, the unparenthesized notation log n^c denoted the value log(n^c). We use a notational shorthand, log^c n to denote the quantity (log n)^c, in which the result of the logarithm is raised to a power

### The Linear Function

Another simple yet important function is the linear function

        f(n) = n

That is, given an input value n, the linear function f assigns the vlue n itself. This function arises in algorithm analysis any time we have to do a single basic operation for each of n elements. The linear function also represents the best running time we can hope to achieve for any algorithm that processes each of n objects that are not already in the computer's memory, because reading in the n objects already requires n operations.

### The N-Log-N Function

        f(n) = nlogn

that is, the function that assigns to an input n the value of n times the logarithm base-two of n. This function grows a little more rapidly than the linear function and a lot less rapidly than the quadriatic function.

### The Quadriatic Function

Another function that appears often in algorithm analysis is the quadratic function

        f(n) = n^2

That is, given an input value n, the function f assigns the product of n with itself.
The main reason why the quadriatic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed a linear number of times.

The quadriatic function can also arise in the context of nested loops where the first iteration of a loop uses one operation, the second uses two operations, the third uses three operations and so on.

        1+ 2+3+..+(n-2)+(n-1)+n = n(n+1)/2

### The Cubic Function and Other Polynomials

Consider the cubic function

        f(n) = n^3

#### Polynomials

Most of the functions we have listed so far can each be viewed as being part of a larger class of functions, the polynomials. A polynomial function has the form

        f(n) = a0+a1n+a2n^2+a3n^3+...+adn^d

where a0,a1,...,ad are constants, called the coefficients of the polynomial and ad =/ 0 . Integer d, which indicates the highest power in the polynomial is called the degree of the polynomial

### the Exponential Function

Another function used in the analysis of algorithms is the exponential function

        f(n) = b^n

where b is a positive constant, called the base, and the argument n is the exponent. That is, function f(n) assigns to the input argument n the value obtained by multiiplying the base b by itself n times. As was the case with the logarithm function, the most common base for the exponential function is algorithm analysis is b =2.

        (b^a)^c = b^(ac)
        b^a * b^c = b^(a+c)
        b^a/b^c = b^(a-c)

##Summary

- constant (c)
- logaritmic (log n)
- linear (n)
- n-log-n (n log n)
- quadriatic (n^2)
- cubic (n^3)
- exponential (a^n)

When discussing logarithms, we note that the value is generally not an integer, yet the running time of an algorithm is usually expressed by means of an integer quantity such as the number of operations performed. Thus, the analysis of an algorithm may sometimes involve the use of the floor function and ceiling function.

## Asymptotic Analysis

In algorithm analysis, we focus on the growth rate of the running time as a function of the input size n, taking a 'big picture' approach.
We analyze algorithms using mathematical notation for functions that disregards constant factors. Namely, we charcterize the running times of algorithms by using functions that map the size of the input, n, to values that correspond to the main factor that determines the growth rate in terms of n. This approach redlects that each basic step in a pseudo-code description or a high-level language implementation may correspond to a small number of primitive operations. Thus we can perform an analysis of an algorithm by estimating the number of primitive operations executed up to a constant factor, rather than getting bogged down in language -specific or hardware-specific analysis of the exact number of operations that execute on the computer

## The Big-Oh Notation

Let f(n) and g(n) be functions mapping positive integers to positive real numbers. We say that f(n) is O(g(n)) if there is a real constant c>0 and an integer constant n0>\_1 such that

        f(n)<-cg(n) , for n>_n0

### Characterizing Runnint Times Using the Big-Oh Notation

The big-Oh notation is widely to characterize running times and space bounds in terms of some parameter n, which varies from problem to problem, but is always defined as a chosen measure of the size of the problem.

### Properties of the Big-Oh Notation

- The big-Oh notation allows us to ignore constant factors and lower-order terms and focus on the main components of a function that affects its growth

        If f(n) is a polynomial of degree d, that is
            f(n) = a0+a1n+...adn^d,
        and ad > 0, then f (n) is O(n^d).

Thus, the highest-degree term in a polynomial is the term that determines the asymptotic growth rate of that polynomial.

### Characterizing Functions in Simplest Terms

In general, we should use the big-Oh notation to charasterize a function as closely as possible. It is also considered poor taste to include constant factors and lower-order terms in the big-Oh notation.We should strive to describe the function in the big-OH in simplest terms

The seven functionas described are the most common functions used in conjunction with the big-Oh notation to characterize the running times and space usage of algorithms. Indeed, we typically use the names of these functions to refer to the running tmes of the algorithms they characterize.

## Big-Omega

Just as the big-Oh notation provides an asymptotic way of saying that a function is 'less than or equal to' another function, the following notations provide an asymptotic way of saying that a function grows at a rate that is 'greater than or equal to that of another.

Let f(n) and g(n) be functions mapping positive integers to positive real numbers. We say that f(n) is Omega g(n) pronounced 'f(n) is big-Omega of g(n)' if g(n) id O(f(n)), that is , there is a real constant c>0 and an integer constant n0 >\_1 such that

                f(n)>_cg(n) for n>_n0

This definition allows us to say asymptotically that one function is greater than or equal to another up to a constant factor.

## Big-Theta

In addition, there is anotation that allows us to say that two functions grow at the same rate, up to constant factors.We say that f (n) is Θ(g(n)), pronounced “ f (n) is big-Theta of g(n),” if f (n) is O(g(n)) and f (n) is Ω(g(n)) , that is, there are real constants c' > 0 and c'' > 0, and an integer constant n0 ≥ 1 such that

                c'g(n) ≤ f (n) ≤ c''g(n), for n ≥ n0.

## Comparative Analysis

We can use the big-Oh notation to order classes of functions by asymptotic growth rate. Our seven functions are ordered by increasing growth rate in the following sequence, that is, if a function f (n) precedes a function g(n) in the sequence,
then f (n) is O(g(n)):

                1, logn, n, nlog n, n2, n3, 2n.

## Some Words of Caution inAsymptotic Analysis

- The use of the big-Oh and related notations can be somewhat misleading should the contant factor they hide be very large. This observation raises the issue of what constitutes a 'fast' algorithm. Generally speaking, any algorithm running in O(nlogn) time (with a reasonable constant factor) should be considered efficient.
  Even an O(n^2)-time function may be fast enough in some contexts, that is, when n is small. But an algorithm running
  in O(2n) time should almost never be considered efficient.

If we must draw a line between efficient and inefficient algorithms, therefore, it is natural to make this distinction be that between those algorithms running in polynomial time and those running in exponential time. That is, make the distinction between algorithms with a running time that is O(nc), for some constant c > 1, and those with a running time that is O(bn), for some constant b> 1. Like so many notions we have discussed in this section, this too should be taken with a “grain of salt,” for an algorithm running in O(n100) time should probably not be considered “efficient.” Even so, the distinction between polynomial-time and exponential-time algorithms is considered a robust measure of tractability.

**Time Complexity** - Analyze runtime of an algorithm as the size of the inputs increases.
**Space Complexity** - We can also use big O notation to analyze space complexity: how much additional memory do we need to allocate in order to run the code in our algorithm. The auxiliary space complexity refers to the space required by the algorithm, not including space taken up by the inputs.
### Space Complexity in JS Rules of Thumb
- Most primitives(booleans, numbers, undefined, null) are constant space
- Strings require O(n) space (where n is the string length)
- Reference types are generally O(n), where n is the lenth(for arrays) or the number of keys(for objects)