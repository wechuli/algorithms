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

The value b is known as the base of the logarithm. The most common base for the logarithm function in computer science is 2.

88fb07a534e1d6bae782e234a0d422bdf352d934
