# To demonstrate the use of operator overloading via special methods, we providean implementation of a Vector class, representing the coordinates of a vector in a multidimensional space. For example, in a three-dimensional space, we might wishto represent a vector with coordinates 5,−2, 3. Although it might be tempting todirectly use a Python list to represent those coordinates, a list does not provide an appropriate abstraction for a geometric vector. In particular, if using lists, the expression [5, −2, 3] + [1, 4, 2] results in the list [5, −2,3, 1, 4, 2]. When working with vectors, if u = 5,−2, 3 and v = 1, 4, 2, one would expect the expression,u + v, to return a three-dimensional vector with coordinates 6, 2, 5.

# class Vector:
#     """ Represent a vector in a multidimensional space """

#     def __init__(self, d):
#         """Create a d-dimensional vector of zeros"""
#         self._coords = [0] * d

mult = [0] + [0]
print(mult)
