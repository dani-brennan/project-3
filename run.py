import random

# welcome message
print("Welcome to my Black Jack Game!")
# instructions

user_input = input("Have you ever played Black Jack before? (Y/N):")

if user_input.lower() == "y":
    print("Great! Let's begin.")

elif user_input.lower() == "n":
    print("Game Instructions")
else:
    print('Please type Y or N')

# deck of cards

cards = []
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
        cards.append([suit, rank])

# shuffle the deck
def shuffle():
    random.shuffle(cards)

# deal cards
def dealCards(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
card = dealCards(1)[0]

print(card)

