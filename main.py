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
        
    # str overide to view deck is constructed as expected 
    def __str__(self):
        return str([str(card) for card in self.cards])
    
    # Include Method to deal cards to players
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

# represents player in game, each player has name and list of cards. Include methods to play & add cards to & from stack
class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def deal_card(self):

        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            None

    def add_card(self, new_cards):

        self.cards.extend(new_cards)


        

# controls main flow of the game with loops until winning conditions are met
def main():

    deck = Deck()
    print(deck)

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while len(deck.cards) > 0:
        player1.cards.append(deck.deal())
        player2.cards.append(deck.deal())
    print(len(player1.cards))
    print(len(player2.cards))

    round_count = 1
    while True:
        print(f"Round {round_count}")
        print(f"{player1.name}: {len(player1.cards)}")
        print(f"{player2.name}: {len(player2.cards)}")
        card1 = player1.deal_card()
        card2 = player2.deal_card()
        print(f"{player1.name} plays {card1}")
        print(f"{player2.name} plays {card2}")

        if card1 is None or card2 is None:
            break

        elif card1.rank > card2.rank:
            # introduced War boolean
            war = False
            player1.add_card([card1, card2])

        elif card1.rank < card2.rank:
            war = False
            player2.add_card([card1, card2])
        
        # war case    
        elif card1.rank == card2.rank:    
            elif len(player1.cards) > 4 and len(player2.cards) > 4:
                war = True
                while war = True: 
                    player1_list = []
                    player2_list = []
                    card_list = []

                    for i in range(5):
                        player1_list.append(player1_list.deal_card())
                        player2_list.append(player2_list.deal_card())
                    card_list.extend(player1_list)
                    card_list.extend(player2_list) 

                    if player1_list[0].value > player2[0].value:
                        player1.add_cards(card_list)
                        war = False
                        break
                        
                    elif player1_list[0].value < player2[0].value:
                        player2.add_cards(card_list)
                        war = False
                        break
                    
                    #war keeps going
                    else:
                        war = True

            # if players don't have enough cards, the game ends:
            else: 
                war = False
                return False
                break
            
        round_count += 1



if __name__ == "__main__":
    main()
