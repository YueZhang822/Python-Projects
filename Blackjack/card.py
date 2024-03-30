class Card:
    """
    A instance of Card stands for a single card in the game.
    """
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"
    SUIT_SYMBOLS = {
        CLUBS: "♣",
        SPADES: "♠",
        HEARTS: "♥",
        DIAMONDS: "♦",
    }
    CARD_VALUES = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
        "J": 10, "Q": 10, "K": 10, "A": 11
    }

    def __init__(self, suit, value):
        self.suit = suit 
        self.original = value    # the original string that stands for its value
        self.value = value    # the numercic value according to rules
    
    @property
    def value(self):
        """
        This method returns the numeric value of the card as defined in the rules above.
        """
        return self.__value

    @value.setter
    def value(self, value):
        """
        The setter of the value attribute.
        """
        if value not in Card.CARD_VALUES:
            raise ValueError("Not eligible value")
        self.__value = Card.CARD_VALUES[value]

    @property
    def color(self):
        """
        This property returns red if the suit is HEARTS or DIAMONDS, and black otherwise.
        """
        if self.suit == Card.HEARTS or self.suit == Card.DIAMONDS:
            return "red"
        elif self.suit == Card.CLUBS or self.suit == Card.SPADES:
            return "black"
        else:
            raise ValueError("Not eligible suit")
    
    @property
    def display(self):
        return f"{self.original}{Card.SUIT_SYMBOLS[self.suit]}"

    def __repr__(self):
        return f"{self.original}{Card.SUIT_SYMBOLS[self.suit]}"