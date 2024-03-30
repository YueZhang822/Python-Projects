# Simplified Blackjack #

This application is a simple version of the card game, Blackjack with a tkinter GUI.

## Rules ##

There will be two players in the game, the player, and the dealer.
Cards 2-10 are worth the value on the card.
Face cards, Jack, Queen, King, are worth 10.
An Ace is always worth 11 points.
A round will go through the following process:

1. The deck is shuffled.

2. The player and dealer each recieve two cards from the deck.

3. The player's turn comes first:

* The player is shown the value of their hand (the sum of card values) and can choose to take another card from the deck (hit) or stop at the current value (stand).

* If the player chooses to hit, they are given a new card and the total is recalculated.

* If the player's score is above 21, the player loses (bust).

* The player may repeat this process until they choose to stand, or bust.

4. If the player did not bust, the dealer plays.
The dealer plays automatically, choosing to hit while their hand's value is less than 17. (i.e. The dealer automatically stands on 17 and above.)

5. If the player and dealer both avoided a bust, then the hand with the highest value wins the game. If they have the same hand value, the hand is a tie (push).