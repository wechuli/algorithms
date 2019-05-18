

# Rather than creating a new list instance, range is a class that can effectively represent the desired range of elements withpout ever storing the explicitly in memory.
r = range(8, 140, 5)

print(r)
print(type(r))
print(len(r))


class Range:
    """A class that mimics the built-in range class"""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance

        Semanctics is similar to built-in range class
        """
        if(step == 0):
            return ValueError("Step cannot be 0")
        if stop is None:   # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0,n)

        # Calculate the effective length once
        self._length = max(0, (stop-start+step-1)//step)

        # need knowledge of start and stop (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of entries in the range"""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k"""
        if type(k) is not int:
            raise ValueError("Must be an integer")

        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step


my_range = Range(0,1000,6)

print(my_range[67])