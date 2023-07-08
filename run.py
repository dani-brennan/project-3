import random

# welcome message
print("Welcome to my Black Jack Game!")
# instructions

user_input = input("Have you ever played Black Jack before? (Y/N):\n")

if user_input.lower() == "y":
    print("Great! Let's begin.")

elif user_input.lower() == "n":
    print("Game Instructions")
else:
    print('Please type Y or N')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'A {self.rank["rank"]} of {self.suit}'

# deck of cards
class DeckofCards:
    def __init__(self):
        self.cards = []
        # suits and ranks
        suits = ["hearts", "diamonds", "spades", "clubs"]

        # assign values to various card ranks
        ranks = [
                {"rank": "2", "value": "2"},
                {"rank": "3", "value": "3"},
                {"rank": "4", "value": "4"},
                {"rank": "5", "value": "5"},
                {"rank": "6", "value": "6"},
                {"rank": "7", "value": "7"},
                {"rank": "8", "value": "8"},
                {"rank": "9", "value": "9"},
                {"rank": "10", "value": "10"},
                # If the player is dealt a Jack(J), Queen(Q) or King(K), it's value will be 10
                {"rank": "K", "value": "10"},
                {"rank": "Q", "value": "10"},
                {"rank": "J", "value": "10"},
                # If the player is dealt an Ace, it's value will be 11
                {"rank": "A", "value": "11"},
            ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    # shuffle the deck
    def shuffle(self):
        # only shuffle is there is more than one card
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # deal cards
    def dealCards(self, number):
        cards_dealt = []
        for x in range(number):
            # if the length of cards is greater than 0, add card to cards dealt
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

# 
class PlayerHand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def attach_card(self, card_list):
        self.cards.extend(card_list)

    def compute_value(self):
        self.value = 0
        holding_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] =="A":
                holding_ace = True

        # If the player is holding an ace and the total value would be over 21, 
        # Ace will equal 1 instead
        if holding_ace and self.value > 21:
            self.value -= 10

    def find_value(self):
        self.compute_value()
        return self.value
            