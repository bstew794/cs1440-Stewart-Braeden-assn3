import Deck
import Menu

class UserInterface():
    def __init__(self):
        self.__m_currentDeck = None
        self.numberInput = None


    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __getNumInput(self, message, rangeBottom, rangeTop):
        """Command to get numeric input from a user"""
        myMessage = message
        myNumInput = 0
        myRangeTop = rangeTop
        isNumeric = False
        inRange = rangeBottom <= myNumInput <= myRangeTop

        while not isNumeric or not inRange:
            myNumInput = input(myMessage)
            isNumeric = myNumInput.isnumeric()

            if not isNumeric:
                print("That is not a number, try again...")
                continue
            else:
                inRange = rangeBottom <= int(myNumInput) <= myRangeTop

            if not inRange:
                print("Number must be " + str(rangeBottom) + " <= number <= " + str(rangeTop))

        return int(myNumInput)

    def __getStringInput(self, message):
        myMessage = message
        myStrInput = ""
        valid = False

        while not valid:
            valid = True
            myStrInput = input(myMessage)

            try:
                myFile = open(myStrInput)
                myFile.close()
            except FileNotFoundError:
                print("File does not exist")
                valid = False

        return myStrInput


    def __createDeck(self):
        """Command to create a new Deck"""
        cardSize = self.__getNumInput("Please enter the size of the cards to be in the deck: ", 3, 15)
        sizeSquare = cardSize * cardSize
        maxNumber = self.__getNumInput("Please enter the maximum number on each card: ", 2 * sizeSquare, 4 * sizeSquare)
        numOfCards = self.__getNumInput("Please enter the number of cards to be in the deck: ", 3, 10000)

        self.__m_currentDeck = Deck.Deck(cardSize, numOfCards, maxNumber)
        self.__deckMenu()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print("")
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumInput("Id of card to print: ", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name: ")
        if fileName != "":
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(None, outputStream)
            outputStream.close()
            print("Done!")
