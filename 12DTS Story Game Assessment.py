#File Name -- The Grand Poker Tournament
#Author -- Oliver Culbert
#Date -- 10/03/2026

# ---- ImportLibrary -----
import random
import time
import sys
from itertools import combinations

# ---- Variables ----
#These are the variables for the card deck, the four suits and all the values in a normal game of texas holdem.
deck_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

player_hand = []
community_cards = []
deck = []

raise_amount = 50
minimum_bet = 50

card_values = {
    "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
    "Jack":11,"Queen":12,"King":13,"Ace":14
}

opponents = [
    {"name": "Mikki Mase", "skill": 1},
    {"name": "Brandon Wilson", "skill": 2},
    {"name": "Tony Lin", "skill": 3},
]
# ---- Functions ----
def type_text(text, speed=0.001): #Typewriter effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def create_deck(): #This is the code that creates the deck. It adds all the cards from each suit to create 1 deck of 52 cards.
    deck.clear() # Clears the deck before creating
    for suit in deck_suits:
        for card in cards_list:
            deck.append(card + " of " + suit)
    return deck

def shuffle_deck(): # This code shuffles the deck so that every card is random and not just in order.
    random.shuffle(deck)

def deal_player():#Deals players cards.
    for i in range(2):
        player_hand.append(deck.pop())
    return player_hand

def deal_flop(deck): #This is the code for the community cards, the flop, turn, and river.
    return [deck.pop(), deck.pop(), deck.pop()]

def deal_turn(deck): #Deal Turn
    return [deck.pop()]

def deal_river(deck): #Deal River
    return [deck.pop()]

def player_action(): #What the player would like to do
    print("\nChoose Action")
    print("1. Check/Call")
    print("2. Raise")
    print("3. Fold")

    action = input("> ")
    return action

def get_value(card): #Get the value of the cards
    return card_values[card.split()[0]]
def get_suit(card): #Get the suit of the card
    return card.split()[2]

def get_values(cards):
    values = []
    for card in cards:
        values.append(get_value(card))
    return values

def get_suits(cards):
    suits = []
    for card in cards:
        suits.append(get_suit(card))
    return suits

def count_values(values):#To see doubles triples etc.
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts

def is_flush(suits): #To see if you have a flush
    for suit in suits:
        if suits.count(suit) >= 5:
            return True
    return False

def is_straight(values): # See if you have a straight
    sorted_values = sorted(set(values))

    if len(sorted_values) < 5:
        return False

    for i in range (len(sorted_values)-4): #Normal Straight 2,3,4,5,6 etc
        if sorted_values[i+4] - sorted_values[i] == 4:
            return True

    if set([14,2,3,4,5]).issubset(sorted_values): #For low straight Ace,2,3,4,5
        return True
    return False

def opponent_decision(opponent, opponent_hand, community_cards): #Opponents decision based on skill level


    skill = opponent["skill"]
    stage = len(community_cards)

    bluff_chance = {
        1: 0.30,
        2: 0.20,
        3: 0.10
    }

    bluff = random.random()

    #Preflop when don't have 5 cards.
    if stage < 3:
        high_cards = get_values(opponent_hand)
        if max(high_cards) >= 11:
            action = "call"
        elif bluff < bluff_chance[skill]:
            action = "raise"
        else:
            action = "call"

    else:
        score, best_hand = evaluate_hand(opponent_hand, community_cards)#The percentage chance the opponent will bluff based on skill level
        if score >= 5:  # What will happen for each different hand based on skill level
            if skill == 3:
                action = "raise"
            else:
                action = "call"

        elif score >= 2:
            if bluff < bluff_chance[skill]:
                action = "raise"
            else:
                action = "call"

        else:
            if bluff < bluff_chance[skill]:
                action = "raise"
            else:
                action = "fold"

        print ("\n", opponent["name"], "chooses to", action)
        return action

def evaluate_5card_hand(cards): #Evaluate your best 5 cards in your hand + the community cards.

    values = get_values(cards)
    suits = get_suits(cards)
    counts = count_values(values)

    pairs = 0
    three = False
    four = False

    for c in counts.values(): #What type of pairs pair, three of a kind, 4 of a kind.
        if c == 2:
            pairs += 1
        elif c == 3:
            three = True
        elif c == 4:
            four = True

    flush = is_flush(suits)
    straight = is_straight(values)

    if straight and flush: # The points for all the different hands in order of strength.
        return 8
    elif four:
        return 7
    elif three and pairs:
        return 6
    elif flush:
        return 5
    elif straight:
        return 4
    elif three:
        return 3
    elif pairs >= 2:
        return 2
    elif pairs == 1:
        return 1
    else:
        return 0

def evaluate_hand(player_hand,community_cards): # Evaluate your hand
    all_cards = player_hand + community_cards

    if len(all_cards) < 5:
        return 0, None

    best_score = - 1
    best_hand = None

    #Check all 5 card combinations
    for combo in combinations(all_cards, 5):
        score = evaluate_5card_hand(list(combo))

        if score > best_score:
            best_score = score
            best_hand = combo

    return best_score, best_hand

def hand_name(score): # The hand names
    names = [
        "High Card",
        "Pair",
        "Two Pair",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush"
    ]

    return names[score]

def betting_round(opponent, opponent_hand, community_cards, pot): #The betting for chips in rounds.
    global player_chips # How many chips your opponent and you have.
    global opponent_chips

    print("\nPlace your bets")
    print("Pot:", pot)
    print("Your Chips:", player_chips)
    print(opponent["name"] + " Chips:", opponent_chips)

    action = player_action() #WHat you decide to do.

    if action == "3":
        type_text("\nYou Folded")
        opponent_chips += pot

        return pot, "player_fold"

    elif action =="2":
        try:
            raise_amount = int(
                input("Enter raise amount: ")
            )

            if raise_amount > player_chips:
                print("Not enough chips!")
                return pot, "continue"

            player_chips -= raise_amount
            pot += raise_amount

            type_text(
                "\nYou raised " +
                str(raise_amount) +
                " chips!"
            )
        except:
            print("Invalid number.")
            return pot, "continue"

    opponent_move = opponent_decision(opponent, opponent_hand, community_cards) #Opponents choice.

    if opponent_move == "fold":
        type_text("\nOpponent Folded")
        player_chips += pot

        return pot, "opponent_fold"

    elif opponent_move == "raise":
        opponent_raise = random.randint(
            minimum_bet,
            minimum_bet * opponent["skill"] * 2
        )

        if opponent_raise > opponent_chips:
            opponent_raise = opponent_chips

        opponent_chips -= opponent_raise
        pot += opponent_raise

        print(
            opponent["name"],
            "raises",
            opponent_raise,
            "chips!"
        )
# ---- Loop ----
name = input("What is your name?")
type_text("Welcome to the Grand Poker Championship, " + name + "!")
time.sleep(1)

type_text("You sit at the table, your stunning Championship chips stacked neatly in front of you.\n"
          "The room is still, the silence only broken by the murmur of spectators and the clinking of chips.\n"
          "Players from all over the world have been invited, you studied them, some are cautious they wait for the perfect hand\n"
          "others bluff hiding their hand behind a poker face developed over years.\n"
          "You are the newest challenger no one knows what to expect.\n "
          "You are playing for no money, Win you are remembered, Lose you walk away.\n"
          "This is the Grand Poker Championship it is down to you to choose what to play!\n")
time.sleep(1)

play = input("Would you like to play (y/n)?")

if play.lower() == "y" or play.lower() == "yes":

    type_text("\nThe tournament begins...\n")

    # Loop through opponents (levels)
    for opponent in opponents:

        # Reset chips for new opponent
        player_chips = 1000
        opponent_chips = 1000

        type_text("\nYour next opponent is " + opponent["name"] + "!")

        while player_chips > 0 and opponent_chips > 0:

            type_text("\nYour next opponent is " + opponent["name"] + "!")
            time.sleep(1)

            # Reset hands
            player_hand.clear()
            community_cards.clear()

            # Create and shuffle deck
            create_deck()
            shuffle_deck()

            pot = minimum_bet * 2

            player_chips -= minimum_bet
            opponent_chips -= minimum_bet

            # Deal player cards
            deal_player()
            opponent_hand = [deck.pop(), deck.pop()]

            print("\nYour Cards:")
            for card in player_hand:
                print(card)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)
            if result != "continue":
                continue

            input("\nPress ENTER to deal the Flop...")

            # Flop
            community_cards.extend(deal_flop(deck))

            print("\nFlop:")
            for card in community_cards:
                print(card)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)

            if result != "continue":
                continue

            input("\nPress ENTER to deal the Turn...")

            # Turn
            community_cards.extend(deal_turn(deck))

            print("\nTurn:")
            for card in community_cards:
                print(card)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)

            if result != "continue":
                continue

            input("\nPress ENTER to deal the River...")

            # River
            community_cards.extend(deal_river(deck))

            print("\nRiver:")
            for card in community_cards:
                print(card)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)

            if result != "continue":
                continue

            # Evaluate hands
            player_score, player_best = evaluate_hand(
                player_hand,
                community_cards
            )

            opponent_score, opponent_best = evaluate_hand(
                opponent_hand,
                community_cards
            )

            # Show opponent cards
            print("\nOpponent Cards:")
            for card in opponent_hand:
                print(card)

            # Show results
            print("\nYour Hand:", hand_name(player_score))
            print("Opponent Hand:", hand_name(opponent_score))

            # Decide winner
            if player_score > opponent_score:

                type_text("\nYou defeated " + opponent["name"] + "!")
                player_chips += pot
                time.sleep(1)

            elif player_score < opponent_score:

                type_text("\nYou lost to " + opponent["name"] + ".")
                opponent_chips += pot
                type_text("You have been eliminated from the tournament.")
                break

            else:

                type_text("\nIt's a tie! Rematch!")

                # replay same opponent
                continue

        else:

            type_text("\nYOU ARE THE GRAND POKER CHAMPION!")

    else:

        type_text("\nMaybe next time.")