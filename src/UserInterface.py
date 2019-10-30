import Deck
import Menu


class UserInterface():
    def __init__(self):
        """Constructor"""
        self.__m_currentDeck = None  # current deck being modified

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
        myMessage = message  # message to display to user
        myNumInput = 0  # what will be returned
        isNumeric = False
        inRange = False

        while not isNumeric or not inRange:
            myNumInput = input(myMessage)
            isNumeric = myNumInput.isnumeric()

            # check if myNumInput is numeric and restart the while loop if it is not
            if not isNumeric:
                print("That is not a number, try again...")
                continue

            else:
                inRange = rangeBottom <= int(myNumInput) <= rangeTop  # determines if myNumInput is within range

            # continue while loop if myNumInput is outside of the range
            if not inRange:
                print("Number must be " + str(rangeBottom) + " <= number <= " + str(rangeTop))

        return int(myNumInput)

    def __getStringInput(self, message):
        myMessage = message  # message to display to user
        myStrInput = ""  # what will be returned
        valid = False  # indicator of whether the filename is valid

        while not valid:
            valid = True
            myStrInput = input(myMessage)  # set myStrInput to be equal to the given filename

            # check if file exists; resume the loop if it does not
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
        SIZE_SQUARE = cardSize * cardSize  # only necessary for simplicity
        maxNumber = self.__getNumInput("Please enter the maximum number on each card: ", 2 * SIZE_SQUARE, 4*SIZE_SQUARE)
        numOfCards = self.__getNumInput("Please enter the number of cards to be in the deck: ", 3, 10000)

        # initialize deck and start the deck menu
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
                keepGoing = False  # return to "Main menu"


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumInput("Please enter Id of card to print: ", 1, self.__m_currentDeck.getCardCount())

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
