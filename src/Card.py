import sys
import NumberSet


class Card():
    def __init__(self, idnum, size, myNumSet):
        """Card constructor"""
        self.idNum = idnum  # identifier of this card
        self.size = size  # dimension of one side of a square bingo card

        # shuffle given NumberSet and then shorten it down to how many spaces are available and reassign self.myNumSet
        myNumSet.randomize()
        myNumSet.numSet[0: self.size * self.size]
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
        self.myNumSet.currIndex = 0  # resets the current index of our numberSet (just in cause)
        NUM_SPACE = 5  # format spacing for Bingo card slots
        isEven = self.size % 2 == 0
        indexOfFree = self.size // 2

        # adds which card it is to the string
        printLine = "Card #" + str(self.idNum)
        printLine += "\n"
        k = 1

        # builds the card in a string format so it may be printed to the console or saved to a text file
        while k <= self.size:
            i = 1
            firstLine = ""

            # adds the "+-----+-----+" border before the entries of the Bingo card
            while i <= self.size:
                firstLine += "+"
                j = 1

                while j <= NUM_SPACE:
                    firstLine += "-"
                    j += 1

                i += 1

            firstLine += "+"
            firstLine += "\n"

            # numLine will temporarily store a row of the entries on the Bingo card
            numLine = ""

            i = 0

            # add entries of the Bingo card to numLine
            while i < self.size:
                numLine += "|"
                numStr = str(self.myNumSet.getNext())

                # determines whether to place the "FREE!" space and where to do so
                if i == indexOfFree and k == indexOfFree + 1 and not isEven:
                    numStr = "FREE!"

                numLine += numStr.center(NUM_SPACE)  # centers the entries
                i += 1

            numLine += "|"
            numLine += "\n"

            printLine += firstLine + numLine
            k += 1

        # add +-----+-----+ border to end of printLine
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

        # print to console if no file is given, otherwise write the string to the given file
        if file is None:
            print(printLine)

        else:
            file.write(printLine)
