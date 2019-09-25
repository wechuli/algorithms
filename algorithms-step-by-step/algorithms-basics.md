# Algorithm Basics

Algorithms are the recipes that make efficient programming possible. The explain how to sort records, search for items, calculate numeric values such as prime factors, find the shortest path betwwen two points in a street network, and determing the maximum flow of infromation possible through a communication network.

## Why Study Algorithms

- They provide useful tools that you can use to solve particular problems such as sorting or finding shortest paths.
- Algorithms teach you methods that you may be able to apply to other problems that have a similar structure
- Algorithms are like a workout for your brain. Studying algorithms can build your problem-solving abilities.
- Algorithms can be interesting, satisfying and sometimes surprising

## Approach

To get the most out of an algorithm, you must be able to do more than simply follow its steps. You need to understanf the following

- The algorithm's behavior
- The algorithm's speed
- The algorithm's memory requirements
- The main techniques the algorithm uses

## Algorithms and Data Structures

An algorithm is a recipe for performing a certain task. A data structure is a way of arranging data to make solving a particular problem easier. Algorithms are often closely tied to data structures.

## Algorithm Features

An good algorithm must have three featurs: correctness, maintainability and efficiency.

If an algorithm ins't maintenable, it's dangerous to use in a program. If an algorithm is simple, intuitive and elegant, you can be confident that it is producing correct results and you can fix it if id doesn't. If the alorithm is intricate, confusing and convoluted, you may have a lot of trouble implementing it, and you will have even more trouble fixing it if a bug arises. If it's hard to understand, how can you know if it is producing correct results ?

## Big O Notation

Big O notation uses a function to describe how the algorithm's worst-case performance relates to the problem size as the size grows very large. This is sometimes called the program's asymptotic performance.

There are five basic rules for calculating an algorithm's Big O notation

- If an algorithm performs a certain sequence of steps f(N) times for a mathematical function f, then it takes O(f(N)) steps.
- If an algorithm performs an operation that takes O(f(N)) steps and then performs a second operation that takes O(g(N)) steps for functions f and g, then the algorithm’s total performance is O(f(N) g(N)).
- If an algorithm takes O(f(N) g(N)) time and the function f(N) is greater than g(N) for large N, then the algorithm’s performance can be simplified to O(f(N)).
- If an algorithm performs an operation that takes O(f(N)) steps, and for every step in that operation it performs another O(g(N)) steps, then the algorithm’s total performance is O(f(N) g(N)).
- Ignore constant multiples. If C is a constant, O(C f(N)) is the same as O(f(N)), and O(f(C N)) is the same as O(f(N)).

### Practical Considerations

Although theoretical behaavior is important in understanding an algorithm's run time behavior, practical considerations also play an important role in real-world performance for several reasons.

- The analysis of an algorithm typically considers all steps as taking the same amount of time even though that may not be the case. Creating and destroying new objects for example may take much longer than mosing integer values from one part of an array to another. In that case, an algorithm that uses arrays may outperform one that uses lots of objects even though the second algorithm does better in Big O notation.
- Many programming environments also provide access to operating system functions that are more efficient than basic algorithmic techniques.

- Just because an algorithm has a certain theoretical asymptotic performance doesn’t mean that you can’t take advantage of whatever tools your programming environment offers to improve performance. Some programming environments also provide tools that can perform the same tasks as some of the algorithms described in this book. For example, many libraries include sorting routines that do a very good job of sorting arrays. Microsoft’s .NET Framework, used by C#
  and Visual Basic, includes an Array.Sort method that uses an implementation that you are unlikely to beat using your own code—at least in general. Similarly, Python lists have a sort method that sorts the items in the list.
- Special-purpose libraries may also be available that can help you with certain tasks. For example, you may be able to use a network analysis library instead of writing your own network tools. Similarly, database tools may save you a
  lot of work building trees and sorting things. You may get better performance building your own balanced trees, but using a database is a lot less work.
- If your programming tools include functions that perform the tasks of one of these algorithms, by all means use them. You may get better performance than you could achieve on your own, and you’ll certainly have less debugging to do.
- Finally, the best algorithm isn’t always the one that is fastest for very large problems.
