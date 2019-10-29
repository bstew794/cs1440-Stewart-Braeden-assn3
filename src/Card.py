import sys

import NumberSet

class Card():
    def __init__(self, idnum, size, myNumSet):
        """Card constructor"""
        self.idNum = idnum
        self.size = size
        myNumSet.randomize()
        myNumSet.numberSet[0: self.size * self.size]
        self.myNumSet = myNumSet

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
        self.myNumSet.currIndex = 0
        NUM_SPACE = 5
        isEven = self.size % 2 == 0
        indexOfFree = self.size // 2

        printLine = "Card #" + str(self.idNum)
        printLine += "\n"
        k = 1

        while k <= self.size:
            i = 1
            firstLine = ""

            while i <= self.size:
                firstLine += "+"
                j = 1

                while j <= NUM_SPACE:
                    firstLine += "-"
                    j += 1

                i += 1

            firstLine += "+"
            firstLine += "\n"
            numLine = ""

            i = 0

            while i < self.size:
                numLine += "|"
                numStr = str(self.myNumSet.getNext())

                if i == indexOfFree and k == indexOfFree + 1 and not isEven :
                    numStr = "FREE!"

                numLine += numStr.center(NUM_SPACE)
                i += 1

            numLine += "|"
            numLine += "\n"
            printLine += firstLine + numLine
            k += 1

        i = 1
        endLine = ""

        while i <= self.size:
            endLine += "+"
            j = 1

            while j <= NUM_SPACE:
                endLine += "-"
                j += 1

            i += 1

        endLine += "+"
        endLine += "\n"
        printLine += endLine
        printLine += "\n"

        if file is None:
            print(printLine)

        else:
            file.write(printLine)
