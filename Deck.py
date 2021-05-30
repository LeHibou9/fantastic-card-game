import random

from Card import Card


class Deck:
    number_cards = 52
    deck = [Card()] * number_cards

    def __init__(self, shuffle=True):
        self.deck = [Card(number, suit)
                     for number in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                     for suit in ["♠", "♣", "♦", "♥"]]

        if shuffle:
            random.shuffle(self.deck)

    def is_valid_deck(self):
        checked = {(number, suit): False
                   for number in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                   for suit in ["♠", "♣", "♦", "♥"]}

        for card in self.deck:
            if checked[(card.get_number(), card.get_suit())]:  # this card was already checked => duplicates
                return False

            checked[(card.get_number(), card.get_suit())] = True

        return all(checked.values())

    def __repr__(self):
        return "Deck(%d)" % self.number_cards

    def __str__(self):
        return "Deck(%d)" % self.number_cards + "\n" + ", ".join([str(card) for card in self.deck])


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(deck.is_valid_deck())
