import unittest
from main import Card, Deck, Player


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card("Hearts", "King")

        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "King")
        self.assertEqual(card.value, 13)

    def test_card_string(self):
        card = Card("Spades", "Ace")

        self.assertEqual(str(card), "Ace of Spades")


class TestDeck(unittest.TestCase):

    def test_deck_has_52_cards(self):
        deck = Deck()

        self.assertEqual(len(deck.all_cards), 52)

    def test_deck_contains_all_cards(self):
        deck = Deck()

        self.assertEqual(len(set(
            (card.suit, card.rank) for card in deck.all_cards
        )), 52)

    def test_shuffle(self):
        deck = Deck()

        original_order = [
            (card.suit, card.rank)
            for card in deck.all_cards
        ]

        deck.shuffle()

        shuffled_order = [
            (card.suit, card.rank)
            for card in deck.all_cards
        ]

        self.assertNotEqual(original_order, shuffled_order)

    def test_grab_one(self):
        deck = Deck()

        card = deck.grab_one()

        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.all_cards), 51)


class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("Andrew")

        self.assertEqual(player.name, "Andrew")
        self.assertEqual(len(player.all_cards), 0)

    def test_add_one_card(self):
        player = Player("Andrew")
        card = Card("Hearts", "Ace")

        player.add_cards(card)

        self.assertEqual(len(player.all_cards), 1)
        self.assertIs(player.all_cards[0], card)

    def test_add_multiple_cards(self):
        player = Player("Andrew")

        cards = [
            Card("Hearts", "Ace"),
            Card("Spades", "King"),
            Card("Clubs", "Queen")
        ]

        player.add_cards(cards)

        self.assertEqual(len(player.all_cards), 3)
        self.assertEqual(player.all_cards, cards)

    def test_remove_one(self):
        player = Player("Andrew")

        card1 = Card("Hearts", "Ace")
        card2 = Card("Spades", "King")

        player.add_cards([card1, card2])

        removed_card = player.remove_one()

        self.assertIs(removed_card, card1)
        self.assertEqual(len(player.all_cards), 1)

    def test_remove_one_from_empty_player(self):
        player = Player("Andrew")

        removed_card = player.remove_one()

        self.assertIsNone(removed_card)

    def test_player_string(self):
        player = Player("Andrew")

        player.add_cards(Card("Hearts", "Ace"))

        self.assertEqual(str(player), "Andrew has 1 cards.")


if __name__ == "__main__":
    unittest.main()