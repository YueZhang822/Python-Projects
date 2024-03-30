from hand import *
import random 

class Deck:
    """
    A instance of Deck stands for a collection of cards that used as deck in the game.
    """
    def __init__(self):
        """
        This method initialize the deck with all 52 cards.
        """
        self.cards = []
        self.dealt = []
        for i in [Card.CLUBS, Card.DIAMONDS, Card.HEARTS, Card.SPADES]:
            for j in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)
                
    @property
    def size(self):
        """
        This property returns the number of cards left in the deck.
        """
        return len(self.cards)

    def deal(self):
        """
        This method removes the top card form the deck and returns it.
        """
        dealt = self.cards.pop(0)
        self.dealt.append(dealt)
        return dealt

    def shuffle(self):
        """
        This method shuffles the already dealt cards and places them at the bottom of the deck.
        """
        random.shuffle(self.dealt)
        self.cards += self.dealt 
        self.dealt = []

    def __repr__(self):
        return f"{self.cards}"