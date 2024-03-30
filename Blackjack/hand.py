from card import Card

class Hand:
    """
    A instance of Hand stands for a collection of cards.
    """
    def __init__(self):
        self.cards = []
    
    def reset(self):
        """
        This method clears the cards in the hand.
        """
        self.__init__()

    def add(self, card):
        """
        This method takes in a instance of card and add it to the hand.
        """
        self.cards.append(card)

    @property
    def total(self):
        """
        This property returns the sum of values for the cards in the hand.
        """
        tot = 0
        for card in self.cards:
            tot += card.value
        return tot 
    
    def __repr__(self):
        return f"{self.cards}"