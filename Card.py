import random


class Card:
    suit_value = "♥"
    number_value = "A"

    def __init__(self, number="A", suit="♥"):
        """
        Create a card instance.
        :param suit: can be "spade"/"pike", "club"/"clover", "diamond"/"tile" or "heart".
        :param number: can be an integer between 1 to 13, or a string "one" to "thirteen". "King", "Queen" and "Jack"
        are also accepted.
        """

        if suit == "spade" or suit == "pike" or suit == "♠":
            self.suit_value = "♠"
        elif suit == "club" or suit == "clover" or suit == "♣":
            self.suit_value = "♣"
        elif suit == "diamond" or suit == "tile" or suit == "♦":
            self.suit_value = "♦"
        elif suit == "heart" or suit == "♥":
            self.suit_value = "♥"
        else:
            raise ValueError("Suit value has to be either spade, club, diamond or heart.")

        if isinstance(number, int):
            if 2 <= number <= 10:
                self.number_value = str(number)
            elif number == 1:
                self.number_value = "A"
            elif number == 11:
                self.number_value = "J"
            elif number == 12:
                self.number_value = "Q"
            elif number == 13:
                self.number_value = "K"
            else:
                raise ValueError("Number value has to be comprised between 1 and 13.")
        elif isinstance(number, str):
            if number == "1" or number == "one" or number == "A":
                self.number_value = "A"
            elif number == "2" or number == "two":
                self.number_value = "2"
            elif number == "3" or number == "three":
                self.number_value = "3"
            elif number == "4" or number == "four":
                self.number_value = "4"
            elif number == "5" or number == "five":
                self.number_value = "5"
            elif number == "6" or number == "six":
                self.number_value = "6"
            elif number == "7" or number == "seven":
                self.number_value = "7"
            elif number == "8" or number == "eight":
                self.number_value = "8"
            elif number == "9" or number == "nine":
                self.number_value = "9"
            elif number == "10" or number == "ten":
                self.number_value = "10"
            elif number == "11" or number == "eleven" or number == "J":
                self.number_value = "J"
            elif number == "12" or number == "twelve" or number == "Q":
                self.number_value = "Q"
            elif number == "13" or number == "thirteen" or number == "K":
                self.number_value = "K"
            else:
                raise ValueError("Number value has to be comprised between 1 and 13.")
        else:
            raise ValueError("Number value has to be a string or an integer.")

    def get_suit(self):
        return self.suit_value

    def get_number(self):
        return self.number_value

    def shuffle(self):
        self.suit_value = random.choice(["♠", "♣", "♦", "♥"])
        self.number_value = random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

    def __repr__(self):
        return "Card(%s,%s)" % (self.number_value, self.suit_value)

    def __str__(self):
        return self.number_value + self.suit_value


if __name__ == "__main__":
    card = Card("A", "♠")
    print(card)
