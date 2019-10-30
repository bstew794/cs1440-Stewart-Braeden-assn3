import sys

import Card
import NumberSet

class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self.cardSize = cardSize  # dimensions of each and every card
        self.__m_cardCount = cardCount  # size of the deck
        self.numberMax = numberMax  # largest a number can be on a Bingo card
        self.__m_cards = []
        i = 1

        # creates and stores randomly generated cards
        while i <= cardCount:
            tempCard = Card.Card(i, self.cardSize, NumberSet.NumberSet(numberMax))
            self.__m_cards.append(tempCard)
            i += 1
            
    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self.__m_cardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1

        if 0 <= n < self.getCardCount():
            card = self.__m_cards[n]

        return card

    def print(self, idx=None, file=sys.stdout):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:

            for idx in range(1, self.__m_cardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)

        else:
            self.getCard(idx).print(file)

