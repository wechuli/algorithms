
# Python provides a more direct mechanism for representing instance namespaces
# that avoids the use of an auxiliary dictionary. To use the streamlined representation
# for all instances of a class, that class definition must provide a class-level member
# named slots that is assigned to a fixed sequence of strings that serve as names
# for instance variables


class Wedding:
    __slots__ = '_man', '_woman', '_venue', '_date'

    def __init__(self, man, woman, venue, date):
        self._man = man
        self._wife = wife
        self._venue = venue
        self._date = date

    def get_man(self):
        return self._man

    def get_woman(self):
        return self._wife
