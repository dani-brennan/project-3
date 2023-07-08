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
ranks = ["A", "2", "3", "4", "5", "6","7", "8", "9", "10", "J", "Q", "K"]

