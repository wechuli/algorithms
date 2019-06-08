# It is also possible to nest one class definition within the scope of another class.


class A:
    class B:
        def __init__(self):
            print("I don't do much either")

    def __init__(self):
        print("I really don't do much")

# In this case, class B is the nested class. The identifier B is entered into the namespace of class A associated with the newly defined class. We note that this technique is unrelated to the concept of inheritence, as class B does not inherit from class A
# Nesting one class in the scope of another makes clear that the nested class exists for support of the outer class. Furthermore, i can help reduce potential name conflicts, because it allows for a similarly named class to exist in another context.
# Another advantage of one class beinh nested as amember of another is that it allows for a more advanced form of inheritence in which a subclass of the outer class overrides the defintion of its nested class