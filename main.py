import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Deck class
class Deck:

    def __init__(self):
        self.all_cards = []

        # create a card object
        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

new_deck = Deck()

# To get all cards
# for all_card in new_deck.all_cards:
#     print(all_card)

