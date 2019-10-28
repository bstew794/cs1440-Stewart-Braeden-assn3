import random


class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.size = size
        self.numberSet = []
        self.currIndex = 0
        i = 1

        while i <= self.size:
            self.numberSet.append(i)
            i += 1

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if self.size <= 0:
            return None

        return self.numberSet[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.numberSet)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.size <= 0:
            return None

        if self.currIndex >= self.size:
            self.currIndex = 0

        oldIndex = self.currIndex
        self.currIndex += 1
        return self.numberSet[oldIndex]
