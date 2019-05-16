class SequenceIterator:
    """An iterator for any Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1  # will increment to 0 on the first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        self._k += 1   # advacne to the neext index

        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration

    def __iter__(self):
        """By convetion, an iterator must return itself as an iterator"""
        return self


my_goals = ['Software Engineer', 'Cloud Engineer',
            'Machine Learning', 'Psychology', 'Philosophy']


my_goals_iterator = SequenceIterator(my_goals)

print(next(my_goals_iterator))
print(next(my_goals_iterator))
print(next(my_goals_iterator))

