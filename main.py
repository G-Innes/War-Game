
import random
# represents card with suit & rank attributes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
# rperesents deck, creates 52 card deck & shuffles. 
class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
    def __str__(self):
        return str([str(card) for card in self.cards])
    
    # Include Method to deal cards to players


# represents player in game, each player has name and list of cards. Include methods to play & add cards to & from stack
class Player:

    ...

# controls main flow of the game with loops until winning conditions are met
def main():

    deck = Deck()
    print(deck)

if __name__ == "__main__":
    main()