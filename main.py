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

two_hearts = Card(suits[0],ranks[0])

# Deck class
class Deck:

    def __init__(self):
        self.all_cards = []

        # Create a Card object for every suit and rank combination
        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)
                self.all_cards.append(created_card)


    # shuffle all the cards using random.shuffle()
    def shuffle(self):

        random.shuffle(self.all_cards)

    # Remove and return one card from the deck
    def grab_one(self):
        return self.all_cards.pop()

my_deck = Deck()
my_deck.shuffle()

# grab one card...
my_card = my_deck.grab_one()


# Creating a Player class with game logic
class Player:

    def __init__(self,name):
        # takes name from the user
        self.name = name

        # at first, user will have 0 cards
        self.all_cards = []

    def add_cards(self,mycards):
        # add cards to the Player.
        if isinstance(mycards,list):
            self.all_cards.extend(mycards)
        else:
            self.all_cards.append(mycards)

    def remove_one(self):
        # it will remove the card from the top. so pop(0)
        try:
            return self.all_cards.pop(0)
        except IndexError:
            print("No cards left!")
        
    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."

name = Player("Alex")
name.add_cards(my_card)
name.add_cards([my_card,my_card,my_card])
print(name)
print("removing one card")
name.remove_one()
print(name)
