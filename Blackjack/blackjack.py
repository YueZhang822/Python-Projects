from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.padding import Padding
from rich import print

from card import Card
from deck import Deck
from hand import Hand

import time 


def _card_to_display(card: Card):
    """
    Helper method to draw a single card.
    """
    return Panel(
        Text(f"{card.display}\n\n{card.display:>3}", style=card.color),
        width=7,
        height=5,
        style="black on white",
    )


def _hand_to_display(hand: Hand, which: str, wins: int):
    """
    Helper method to draw a hand.
    """
    g = Table.grid("Player")
    for card in hand.cards:
        g.add_column()
    g.add_row(*[_card_to_display(card) for card in hand.cards])
    g.add_row(
        Text(f"Total: {hand.total}", style="black" if hand.total <= 21 else "red"),
        Text(f"  Wins: {wins}"),
    )
    return Panel(g, title=which, style="magenta on white")


def draw_card_table(
    deck: Deck,
    dealer: Hand,
    player: Hand,
    num_dealer_wins: int,
    num_player_wins: int,
    *,
    winner: str = None,
):
    """
    Method to draw the current state of the game.

    Parameters:
        deck (Deck):            Deck of cards.
        dealer (Hand):          Dealer's Hand.
        player (Hand):          Player's Hand.
        num_dealer_wins (int):  Number of times dealer has won this game.
        num_player_wins (int):  Number of times player has won this game.
        winner (str):           Either "player" or "dealer" if a player has won the game.
    """
    # clear screen
    print("\n" * 100)
    layout = Table.grid(expand=True)
    layout.add_column(ratio=2)
    layout.add_column(ratio=1)
    layout.add_row(
        _hand_to_display(dealer, "Dealer", num_dealer_wins),
        Panel(f"Cards Left: {deck.size}", title="Deck", style="green on white"),
    )
    layout.add_row(_hand_to_display(player, "Player", num_player_wins))
    if winner == "player":
        layout.add_row(Padding("[white on green]Player Wins!", 1, expand=True))
    elif winner == "dealer":
        layout.add_row(Padding("[white on red]Dealer Wins!", 1, expand=True))
    print(layout)


def does_player_hit():
    """
    Prompts player for [h]it or [s]tand decision.

    Returns: True if player selects "hit", False if they stand.
    """
    return Prompt.ask("\[h]it or \[s]tand?", choices="hs") == "h"


def main():
    """
    Implement this function according to the rules set out in README.md

    Use draw_card_table and does_player_hit as needed.
    """
    # Initialize Game
    deck = Deck()
    player = Hand()
    dealer = Hand()
    dealer_wins = 0
    player_wins = 0
    
    def play(people, is_dealer=False):
        """
        This function takes in a player as argument and keeps track of the his/her score until total value 
        exceed 21 or dealer's total value reaches 17 or the player decide to stand.

        Input: a instance of Hand, which stands for player's or dealer's handcards.

        Output: return the total value of the player's or dealer's handcards after his/her turn is over.
        """
        draw_card_table(deck, dealer, player, dealer_wins, player_wins)
        while is_dealer and people.total < 17:
            print("【 Dealer is drawing new card... 】")
            time.sleep(1.5)
            people.add(deck.deal())
            draw_card_table(deck, dealer, player, dealer_wins, player_wins)
        while not is_dealer and people.total <= 21 and does_player_hit():
            people.add(deck.deal())
            draw_card_table(deck, dealer, player, dealer_wins, player_wins)
        return people.total 

    while True:
        # Play Round of Blackjack
        if deck.size < 16:    # shuffle the deck when deck is short of cards
            print("【 suffling deck... 】")
            time.sleep(2)
            deck.shuffle()
        player.reset()    # reset two player's handcards before each round
        dealer.reset()
        for i in range(2):    # give two cards to each player to start with
            player.add(deck.deal())
            dealer.add(deck.deal())
        player_score = play(player)    # first comes the palyer's turn
        if player_score > 21:
            dealer_wins += 1
            draw_card_table(deck, dealer, player, dealer_wins, player_wins, winner="dealer")
            print("【 Player Bust! 】\n")
        else:
            dealer_score = play(dealer, True)    # then comes dealer's turn if player didn't bust
            if dealer_score > 21 or player_score > dealer_score:
                player_wins += 1
                draw_card_table(deck, dealer, player, dealer_wins, player_wins, winner="player")
                if dealer_score > 21:
                    print("【 Dealer Bust! 】\n")
            elif player_score < dealer_score:
                dealer_wins += 1
                draw_card_table(deck, dealer, player, dealer_wins, player_wins, winner="dealer")
            else:
                print("【 Tie! 】\n")
        # end of round
        if not Confirm.ask("Play again?"):
            break


if __name__ == "__main__":
    main()