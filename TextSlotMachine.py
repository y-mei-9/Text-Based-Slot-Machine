# Yingyi M
# Period 4
# Jan 23, 2024
# Text-Based Slot Machine

# Init
import random
current_slot, weight = [], []  # Empty list variables for use in functions
cost_for_spin, prize_earned, credits_won, current_credits = 0, 0, 0, 0  # Empty integer variables for use in function
slot_symbols = ['♥', '♦', '♠', '♣', '7']  # Possible slot symbols

# Functions
# To define empty variables based on bet level chosen by user
def choose_bet_difficulty():
    global slot_symbols, cost_for_spin, prize_earned, weight, current_slot
    print("\nHere is the catch...you can modify how large of a bet you want to make!!!\n    1) Small (10 credits for a play. Get $10 for a Jackpot, $1 for a match!)\n    2) Medium (20 credits for a play. Get $100 for a Jackpot, $10 for a match!)\n    3) Large (30 credits for a play. Get $1000 for a Jackpot, $100 for a match!)\n    4) EXTREME (500 credits for a play. Get $100,000 for a Jackpot, $10000 for a match!)")
    while True:
        user_difficulty = input("\nDo you want a small, medium, large, or extreme bet (Enter an integer from 1 to 4)? \nRemember: Larger the bet, smaller the odds!!!: ")
        if user_difficulty == "1":
            cost_for_spin, prize_earned, weight = 10, 100, [.1125, .1125, .1125, .1125, .45]
            break
        elif user_difficulty == "2":
            cost_for_spin, prize_earned, weight = 20, 1000, [.15, .15, .15, .15, .4]
            break
        elif user_difficulty == "3":
            cost_for_spin, prize_earned, weight = 30, 10000, [.2, .2, .2, .2, .2]
            break
        elif user_difficulty == "4":
            cost_for_spin, prize_earned, weight = 500, 1000000, [.24, .24, .24, .24, .05]
            break
        else:
            print("That is not a valid option. Try again!")

# Generates a sequence of 3 symbols using random.choice
# Parameter (weight) is a list
def random_slot_symbol(weight):
    global current_credits, current_slot
    current_credits -= cost_for_spin
    current_slot = random.choices(slot_symbols, weights=weight, k=3)
    print(current_slot)

# Check win by seeing if all indices of the current symbol list are equal or is the jackpot symbol and allocates credits accordingly
# Parameter (symbol_list) is a list
# Parameter (prize) is an integer
def check_win(symbol_list, prize):
    global credits_won
    # Check for match and jackpots
    if symbol_list[0] == symbol_list[1] == symbol_list[2]:
        if symbol_list[0] == '7':  # If all symbols are the same, then any one of the three is a '7' for a jackpot
            credits_won += prize
            print("JACKPOT!!!")
            print(f"You now have {current_credits + credits_won} credits.")
            print(f"You earned a total of ${credits_won/10}.")
        else:  # If all symbols are the same and are not 7, then it is a match
            credits_won += (prize/10)
            print("\nMatch!")
            print(f"You now have {current_credits + credits_won} credits.")
            print(f"You earned a total of ${credits_won/10}.")
    else:
        print("\nYou lost!")
        print(f"You now have {current_credits + credits_won} credits.")
        print(f"You earned a total of ${credits_won/10}.")

# Introduce the rules of the slot game and collects the amount of credits user want to buy
# Returns an integer stored in variable credit_pts
def introduce_game():
    print("Welcome to Slot Machine Simulator! Get three 7's in a row for a jackpot. Get three of all other symbols for a match. ")
    print("10 prize credits redeems to $1!!!")
    while True:
        try:
            choose_bet_difficulty()
            credit_pts = int(input(f"\nHow many credits would you like to purchase ({cost_for_spin} credits per spin, 10 credits per dollar). \n(NO REFUNDS FOR LEFTOVER CREDITS; YOU CAN ONLY REDEEM PRIZE MONEY): "))
            break
        except ValueError:
            print("\nThat is not a number. Try again.")
    return credit_pts

# Check if the user has enough credits to spin the slot
# Returns a boolean
def check_credits():
    if (current_credits + credits_won) < cost_for_spin:
        print("\nYou ran out of credits.")
        print(f"Please pay ${starting_credits/10} for the credits you bought.")
        if credits_won > starting_credits:
            print(f"You earned a total prize of ${(current_credits + credits_won) / 10}.")
            print(f"After subtracting your starting cost from your prize money, you get ${(credits_won - starting_credits)/10}.")
            return False
        else:
            print(f"After subtracting your prize money from your starting cost, you still have to pay ${(starting_credits-credits_won)/10}.")
    else:
        return True

# Calculate how much the user earned if they do not wish to spin again
def calculate_earning():
    print(f"\nYou earned a total prize of ${credits_won / 10}.")
    print(f"Please pay ${starting_credits/10} for the credits you bought.")
    if credits_won > current_credits:
        print(f"After subtracting your starting cost from your prize money, you get ${(credits_won - starting_credits)/10}.")
    else:
        print(f"You owe ${(starting_credits-credits_won) /10} after subtracting your prize money from starting cost.")

# Main
current_credits = starting_credits = introduce_game()  # Introduce the game and define current and starting credit vars
# While loop to let user play until they input otherwise
while True:
    start_prompt = input("\nWill you like to spin the slots (Input yes or no (y or n works as well))?:  ")
    if start_prompt == "yes" or start_prompt == "y":  # Spin slot and check for wins
        random_slot_symbol(weight)
        check_win(current_slot, prize_earned)
        if not check_credits():  # Break while loop if user is out of credits
            break
    elif start_prompt == "no" or start_prompt == "n":  # Break the loop when user prompts
        calculate_earning()
        break
    else:
        print("Invalid input. Try again!")  # Handles error
