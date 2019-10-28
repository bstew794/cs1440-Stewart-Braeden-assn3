import sys

import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.idNum = idnum
        self.size = size
        self.numberSet = numberSet
        pass


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.idNum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        pass
