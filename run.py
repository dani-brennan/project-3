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
    print("♥♦♠♣" * 7)
    print_slower("♠♣  WELCOME TO BLACKJACK! ♥♦")
    print("♥♦♠♣" * 7)
    print()
    print_slower("Dealer: I don't think I've seen you around here before.. ")
    name = input("What's your name?: ")
    if name == (""):
        print_slower("Dealer: Well aren't you mysterious?")
    else:
        print_slower("Dealer: Welcome to my table " + name + " :)")

    print()
    userAnswer = None

    while userAnswer not in ("y", "yes", "n", "no"):
        userAnswer = input("Dealer: Need me to teach you " +
                           "how to play? (Y/N): ").lower()

        if userAnswer == "y":
            # Show the player how to play
            print_slower("Okay, the rules of Blackjack are..")
            print("--" * 12)
            print_slower("Each player gets dealt 2 cards.")
            print_slower("You can then decide whether to Hit or Stand.")
            print_slower("To win you must have a higher hand value, " +
                         "than me which must not exceed 21.")
            print_slower("If the hand value is worth 21 you" +
                         " got a Blackjack")
            print_slower("This instantly wins the game.")
            print_slower("If the hand value is over 21, player busts.")
            print("--" * 12)
            ready_to_play = False

            while ready_to_play := False:
                ready_to_play = input("Type 'start' to begin: ").lower()

                if ready_to_play == str("start" or "Start"):
                    ready_to_play = True
                    # Start Game
                    print_slower("The dealer is shuffling the deck...")
                else:
                    print("" * 12)
                    ready_to_play = False

        elif userAnswer == ("n", "N"):
            print_slower("The dealer is shuffling the deck...")
        else:
            print("Please type Y or N: ")


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'> {self.rank["rank"] } {self.suit}'


# deck of cards
class DeckofCards:
    def __init__(self):
        self.cards = []
        # suits and ranks
        suits = ["♥", "♦", "♠", "♣"]

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
                # If the player is dealt a Jack(J), Queen(Q)
                # or King(K), it's value will be 10
                {"rank": "K", "value": "10"},
                {"rank": "Q", "value": "10"},
                {"rank": "J", "value": "10"},
                # If the player is dealt an Ace, it's value will be 11
                {"rank": "A", "value": "11"},
            ]
        # Credit: https://replit.com/@BeauCarnes/blackjack-python
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    # Credit: https://replit.com/@BeauCarnes/blackjack-python
    # shuffle the deck
    def shuffle(self):
        # only shuffle is there is more than one card
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # Credit: https://replit.com/@BeauCarnes/blackjack-python
    # deal cards
    def dealCards(self, number):
        cards_dealt = []
        for x in range(number):
            # if the length of cards is greater than 0, add card to cards dealt
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


# Credit: https://replit.com/@BeauCarnes/blackjack-python
class PlayerHand:
    def __init__(self, dealer=False):
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
            if card.rank["rank"] == "A":
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

    def view_cards(self, show_dealers_hand=False):

        print(f'''{"Dealer" if self.dealer else "Your"} hand:''')

        for index, card in enumerate(self.cards):

            # Make dealers hand hidden
            if index == 0 and self.dealer and not show_dealers_hand \
                    and not self.black_jack():
                print("> [hidden]")
            else:
                print(card)

        # If the player is not the dealer
        if not self.dealer:
            print("Total value:", self.find_value())
            print()


class Game:

    def play(self):
        game_number = 3
        play_again = True
        total_games_played = 0
        print("Playing 3 rounds of Blackjack")

        while game_number > 0:
            game_number -= 1
            total_games_played += 1
            print("--" * 12)
            print(f"Game {total_games_played} of 3")
            print("--" * 12)
            deck = DeckofCards()
            deck.shuffle()

            players_hand = PlayerHand()
            dealers_hand = PlayerHand(dealer=True)

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            for i in range(2):
                players_hand.attach_card(deck.dealCards(1))
                dealers_hand.attach_card(deck.dealCards(1))

            print()

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            players_hand.view_cards()
            dealers_hand.view_cards()

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            if self.check_for_win(players_hand, dealers_hand):
                continue

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            hit_or_stand = ""

            # While the players hand is less than 21, give the
            # player the choice to hit or stand
            while players_hand.find_value() < 21 and hit_or_stand \
                    not in ["Stand", "stand"]:
                print()
                hit_or_stand = input("Would you like to 'Hit' or " +
                                     "'Stand'?: ").lower()
                print()
                while hit_or_stand not in ["Hit", "hit", "Stand", "stand"]:
                    hit_or_stand = input("Please type 'Hit' or 'Stand': ")

                if hit_or_stand in ["Hit", "hit"]:
                    players_hand.attach_card(deck.dealCards(1))
                    players_hand.view_cards()

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            if self.check_for_win(players_hand, dealers_hand):
                continue

            players_hand_total = players_hand.find_value()
            dealers_hand_total = dealers_hand.find_value()

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            while dealers_hand_total < 17:
                dealers_hand.attach_card(deck.dealCards(1))
                dealers_hand_total = dealers_hand.find_value()

            # Credit: https://replit.com/@BeauCarnes/blackjack-python
            dealers_hand.view_cards(show_dealers_hand=True)
            if self.check_for_win(players_hand, dealers_hand):
                continue

            print()
            print("." * 12)
            print_slower(":Game Results: ")
            print("'" * 12)
            print_slower("Your Hand: ")
            print(players_hand_total)
            print()
            print_slower("Dealer's Hand: ")
            print(dealers_hand_total)

            self.check_for_win(players_hand, dealers_hand, True)

        print(f"You played {total_games_played} rounds.")

        while game_number == 0:
            play_again = input("Dealer: Would you like to play again? " +
                               "(Y/N): ").lower()

            if play_again not in ["Y", "y", "N", "n"]:
                play_again = input("Please type Y/N: ")

            elif play_again in ["y", "Y"]:
                game.play()
            elif play_again in ["n", "N"]:
                print("♥♦♠♣" * 7)
                print_slower("♠♣   THANKS FOR PLAYING!  ♥♦")
                print("♥♦♠♣" * 7)
                print()
                exit()

    # Credit: https://replit.com/@BeauCarnes/blackjack-python
    def check_for_win(self, players_hand, dealers_hand, game_over=False,
                      player_win=False):

        if not game_over:
            # If the total value of the players cards is over 21, player loses
            if players_hand.find_value() > 21:
                print("*" * 12)
                print_slower("Bust! Dealer wins.")
                print("*" * 12)
                return True
            # If the total value of the dealers cards is over 21, dealer loses
            elif dealers_hand.find_value() > 21:
                print("*" * 12)
                print_slower("You win! Dealer has bust.")
                print("*" * 12)
                return True

            # If player has a total card value of 21, player wins
            elif players_hand.black_jack():
                print_slower("*" * 12)
                print_slower("Black Jack! You win!")
                print_slower("*" * 12)
                return True

            # If dealer has a total card value of 21, dealer wins
            elif dealers_hand.black_jack():
                print_slower("*" * 12)
                print_slower("You lose! Dealer has Black Jack.")
                print_slower("*" * 12)
                return True
            # If both players have a total card value of 21, it's a tie
            elif dealers_hand.black_jack() and players_hand.black_jack():
                print_slower("It's a tie! You both have Black Jack.")
                return True
        else:
            # If the players card value is more that the dealers card value
            if players_hand.find_value() > dealers_hand.find_value():
                print_slower("*" * 12)
                print_slower("You win!")
                print_slower("*" * 12)
            # If the dealers card value is more that the players card value
            elif players_hand.find_value() < dealers_hand.find_value():
                print_slower("*" * 12)
                print_slower("You lose!")
                print_slower("*" * 12)
            # If the players card value is the same as the dealers card value
            elif players_hand.find_value() == dealers_hand.find_value():
                print("*" * 12)
                print_slower("It's a tie!")
                print("*" * 12)
            return True
        return False


game_intro()
game = Game()
game.play()
