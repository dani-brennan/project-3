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
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

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
cards_dealt = dealCards(2)
card = cards_dealt[0]
rank = card[1]
print(cards_dealt)

