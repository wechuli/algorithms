# Objects in Python

- Python is a dynamically typed language, as there is no advance declaration associatin an identifier with a particular data type
- When using a method of a class, it is important to understand its behaviour. Some methods return information about the state of an object, but do not change that state. These are known as accessors. Other methods, such as the sort method of the list class, do change the state of an object. These methods are known as mutators or update methods.

- A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed. Once as an instance has been created, its value cannot be changed although an identifier referencing that object can be reassigned to a different value

# Exception Handling

- If uncaught, an exception causes the interpreter to stop executing the program and to report an approprate message to the console

# Object Oriented Principles

- Each object is an instance of a class. The class definition typically specifies instance variables also known as data members that the object contains, as well as the methods, also known as member functions that the object can execute.
- Software implementations should achieve robustness, adaptability and reusability

## Object-Oriented Design Principles

- ** Modularity ** - Modularity refers to an organization principle in which different components of a software system are divided into separate functional units.Using modularity in a software system can also provide a powerful organizing framework that brings clarity to an implementation. Robustness is greatly increased because it is easier to test and debug separate components before they are integrated into a larger software system.The stucture imposed by modularity also helps enable software resusability

- ** Abstraction ** - The notion of abstraction is to distill a complicated system down to its most fundamental parts.Typically, describing the parts of a system involves naming them and explaining their functionality. Applying the abstraction paradigm to the design od data structures gives rise to abstract data types(ADT). An ADT is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the types of parameters of the operations.An ADT specifies what each operation does, but not how it does it.We will typically refer to the collective set of behaviors supported bu an ADT as its public interface.

- ** Encapsulation ** - Another important principle of object-oriented design is encapsulation.Different components of a software system should not reveal the internal details of their respective implementations.The only constraint on the programmer of a component is to maintain the public interface for the component as other programmers will be writing code that depends on that interface.

# Software Development

- Design
- Implementation
- Testing and Debugging

## Design

- In this stage we decide how to divide the workings of our program into classes, we decide how these classes will interact, what data each will store, and what actions each will perform.
- Guidelines Include
  - Responsibilities- Divide the work into different actors, each with a different responsibility.
  - Independence - Define the work for each class to be as independent from other classes as possible.
  - Behaviours - define the behavios for each class carefully and precisely so that the consequences of each action performed by a class will be well understood by other classes that interact with it

## Operator Overloading and Python's Special Methods

- By default, the + operator is undefined for a new class. however, the author of a class may provide a definition using a technique known as operatorr overloading. This is done by implementing a pecially named method. In particular, the + operator is overloaded by implementing a method named **add**, which takes the right-hand operand as a parameter and which returns the result of the expression. a+b is converted to a method call on object a of the form a.**add**(b). Similar specially named methods exist for other operators
- When a binary operator is applied to two instances of different types, as in 3\*'love me', Python gives deference to the class of the left operand.In this example, it would effectively check if the int class provides a sufficient definition for how to multiply an instance by a string, via the mul method. However, if that class does not implement such a behavior, Python checks the class definition
  for the right-hand operand, in the form of a special method named rmul
  (i.e., “right multiply”). This provides a way for a new user-defined class to support
  mixed operations that involve an instance of an existing class (given that the existing
  class would presumably not have defined a behavior involving this new class).
  The distinction between mul and rmul also allows a class to define different
  semantics in cases, such as matrix multiplication, in which an operation is
  noncommutative (that is, A x may differ from x A).

## Non-operator Overloads
- In addition to traditional operator overloading, Python relies on specially named methods to control the behavior of various other functionality, when applied to user-defined classes.

- Several other top-level functions rely on calling specially named methods.For
example, the standard way to determine the size of a container type is by calling
the top-level len function. Note well that the calling syntax, len(foo), is not the
traditional method-calling syntax with the dot operator. However, in the case of a
user-defined class, the top-level len function relies on a call to a specially named
len method of that class. That is, the call len(foo) is evaluated through a
method call, foo. len (). When developing data structures, we will routinely
define the len method to return a measure of the size of the structure.

##Implied Methods

- As a general rule, if a particular special method is not implemented in a user-defined class, the standard syntax that relies upon that method will raise an exception. For example, evaluating the expression, a+b, for instances of a user-defined class without __add__ or __radd__ will raise an error. However, there are some operators that have default defintions provided by Python, in the absence of special methods, and there are sopme operators whose definitiots are derived from others