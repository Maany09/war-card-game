import random
import pdb


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



# GAME LOGIC
# Two PLayers
player_one = Player("Andrew")
player_two = Player("Sam")

# Setting up the new game
new_deck = Deck()
new_deck.shuffle()


# Splitting the deck b/t two players
len(new_deck.all_cards)/2

for x in range(26):
    player_one.add_cards(new_deck.grab_one())
    player_two.add_cards(new_deck.grab_one())


print(len(player_one.all_cards))

game_on = True

round_num = 0
while game_on:
    
    round_num = round_num + 1
    print(f"Round {round_num}")
    # Check if any player is out of their cards.

    if len(player_one.all_cards) == 0:
        print("Player one is out of cards")
        print("PLayer two has WON the War!!!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two is out of cards")
        print("Player one has WON the War!!!")
        game_on = False
        break

    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        # Player One has higher card
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets all the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        # Player Two has higher card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets all the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        # For Cards that have the same value
        else:

            print("WAR!")

            # Check if Player One has enough cards to continue
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war!")
                print("Player Two Wins!")
                game_on = False
                break

            # Check if Player Two has enough cards to continue
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war!")
                print("Player One Wins!")
                game_on = False
                break

            # Both players have enough cards
            else:

                # Each player puts 5 more cards on the table
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

