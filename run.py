import random
import sys
import time

def print_slower(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write('\n')

# welcome message
def game_intro():
    print("~" * 6)
    print_slower("Welcome to Black Jack.")
    print("~" * 6)
    print_slower("What is your name?")
    x = input()
    print("~" * 6)
    print_slower("Nice to meet you, " + x + "! :)")

    userAnswer = None 

    while userAnswer not in ("y", "n"): 
        userAnswer = input("Would you like to see the instructions on how to play? ")

        if userAnswer == "y": 
            # Show the player how to play
            print_slower("Game Instructions")
            print("~" * 8)
            
            ready_to_play = False

            while ready_to_play == False:
                ready_to_play = input("Type 'start' when you are ready to start the game.")
                
                if ready_to_play == str("start" or "Start"):
                    ready_to_play = True
                    # Start Game
                    print_slower("Game starting...")
                else:
                    print("Type 'start' to start the game.")
                    ready_to_play = False
                        


        elif userAnswer == "n": 
            # Start Game
            print_slower("Game starting...")
        else: 
            print("Please enter yes or no.") 

game_intro()

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

    def black_jack(self):
        return self.find_value() == 21

    def view_cards(self, show_dealers_hand = False):

        print(f'''{"Dealer" if self.dealer else "Your"} hand:''')   

        for index, card in enumerate(self.cards):

            # Make dealers hand hidden
            if index == 0 and self.dealer and not show_dealers_hand and not self.black_jack():
                print("hidden")
            else: 
                print(card)

        # If the player is not the dealer
        if not self.dealer:
            print("Total value:", self.find_value())
            print()

class Game
    def play(self):
    
        while game_start == True:
            deck = DeckofCards()
            deck.shuffle()

            players_hand = PlayerHand()
            dealers_hand = PlayerHand(dealer = True)

            for i in range(2):
                players_hand.attach_card(deck.deal(1))
                dealers_hand.attach_card(deck.deal(1))
            
            print("~" * 6)

            players_hand.view_cards()
            dealers_hand.view_cards()
            




