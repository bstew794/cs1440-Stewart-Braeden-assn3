import random


class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.size = size  # length of list
        self.numSet = []  # stores the range of numbers
        self.currIndex = 0  # used to iterate in getNext() function
        i = 1

        # generate and add numbers from 1 to self.size
        while i <= self.size:
            self.numSet.append(i)
            i += 1

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if self.size <= 0 or index >= self.size:
            return None

        return self.numSet[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.numSet)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""

        # do not attempt to return a index at the end of the list or from an empty list
        if self.size <= 0 or self.currIndex == self.size:
            return None

        # save and return current index and then iterate currIndex
        oldIndex = self.currIndex
        self.currIndex += 1
        return self.numSet[oldIndex]
