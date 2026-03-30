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
def type_text(text, speed=0.01): #Typewriter effect
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
        print("\n", opponent["name"], "chooses to", action)
        return action

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

    values = sorted(get_values(cards), reverse = True)
    suits = get_suits(cards)
    counts = count_values(values)

    pairs = []
    three = None
    four = None

    for value, count in counts.items(): #What type of pairs pair, three of a kind, 4 of a kind.
        if count == 4:
            four = value
        elif count == 3:
            three = value
        elif count == 2:
            pairs.append(value)

    flush = is_flush(suits)
    straight = is_straight(values)

    if straight and flush: # The points for all the different hands in order of strength.
        return (8, values)
    elif four:
        kicker = [v for v in values if v != four]
        return (7, [four] + kicker)
    elif three and pairs:
        return (6, [three, max(pairs)])
    elif flush:
        return (5,values)
    elif straight:
        return (4, values)
    elif three:
        kicker = [v for v in values if v != three]
        return (3, [three] + kicker)
    elif len(pairs) >= 2:
        high_pair = max(pairs)
        low_pair = min(pairs)
        kicker = [v for v in values if v != high_pair and v != low_pair]
        return (2, [high_pair, low_pair] + kicker)
    elif len(pairs) == 1:
        pair = pairs[0]
        kickers = [v for v in values if v != pair]
        return (1, [pair] + kickers)
    else:
        return (0, values)

def evaluate_hand(player_hand,community_cards): # Evaluate your hand
    all_cards = player_hand + community_cards

    if len(all_cards) < 5:
        return (0, [])

    best_rank = (-1, [])

    for combo in combinations(all_cards, 5):
        rank = evaluate_5card_hand(list(combo))

        if rank > best_rank:
            best_rank = rank
    return best_rank

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

    current_bet = 0
    player_bet = 0
    opponent_bet = 0

    print("\nPlace your bets")
    print("Pot:", pot)
    print("Your Chips:", player_chips)
    print(opponent["name"] + " Chips:", opponent_chips)

    action = player_action() #WHat you decide to do.

    if action == "3":
        type_text("\nYou Folded")
        opponent_chips += pot
        time.sleep(1)

        return pot, "player_fold"

    elif action == "1":
        call_amount = current_bet - player_bet

        if call_amount > 0:
            if call_amount > player_chips:
                call_amount = player_chips

            player_chips -= call_amount
            pot += call_amount
            player_bet += call_amount

            type_text("\nYou call" + str(call_amount) + " chips!")

        else:
            type_text("\nYou Check")

        time.sleep(1)

    elif action =="2":
        try:
            raise_amount = int(
                input("Enter raise amount: ")
            )

            total_raise = (current_bet - player_bet + raise_amount)

            if total_raise > player_chips:
                print("Not enough chips!")
                continue

            player_chips -= total_raise
            pot += total_raise

            player_bet += total_raise
            current_bet = player_bet

            type_text(
                "\nYou raised " +
                str(current_bet)
            )
            time.sleep(1)

        except:
            print("Invalid number.")
            continue

    time.sleep(1)

    opponent_move = opponent_decision(opponent, opponent_hand, community_cards) #Opponents choice.

    if opponent_move == "fold":
        type_text("\nOpponent Folded")
        player_chips += pot

        return pot, "opponent_fold"

    elif opponent_move == "call":
        call_amount = current_bet - opponent_bet

        if call_amount > opponent_chips:
            call_amount = opponent_chips

        opponent_chips -= call_amount
        pot += call_amount
        opponent_bet += call_amount

        print(
            opponent["name"],
            "calls",
            call_amount
        )

        time.sleep(1)

    elif opponent_move == "raise":

        raise_amount = random.randint(
            minimum_bet,
            minimum_bet * opponent["skill"] * 2
        )

        total_raise = (current_bet - opponent_bet + raise_amount)

        if total_raise > opponent_chips:
            total_raise = opponent_chips

        opponent_chips -= total_raise
        pot += total_raise

        print(
            opponent["name"],
            "raises",
            opponent_raise,
            "chips!"
        )
    return pot, "continue"
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
        player_chips = 500
        opponent_chips = 500

        type_text("\nYour next opponent is " + opponent["name"] + "!")

        while player_chips > 0 and opponent_chips > 0:

            time.sleep(1)

            # Reset hands
            player_hand.clear()
            community_cards.clear()
            opponent_hand = []

            # Create and shuffle deck
            create_deck()
            shuffle_deck()

            pot = minimum_bet * 2

            player_chips -= minimum_bet
            opponent_chips -= minimum_bet

            # Deal player cards
            deal_player()
            opponent_hand = [deck.pop(), deck.pop()]
            time.sleep(1)

            print("\nYour Cards:") #Print players cards.
            for card in player_hand:
                print(card)
            time.sleep(2)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot) #Print the blind betting
            if result != "continue":
                continue
            time.sleep(1)

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
            player_rank  = evaluate_hand(player_hand, community_cards)
            opponent_rank = evaluate_hand(opponent_hand, community_cards)

            # Show opponent cards
            print("\nOpponent Cards:")
            for card in opponent_hand:
                print(card)

            # Show results
            print("\nYour Hand:", hand_name(player_rank[0]))
            print("Opponent Hand:", hand_name(opponent_rank[0]))

            # Decide winner
            if player_rank > opponent_rank:

                type_text("\nYou defeated " + opponent["name"] + "!")
                player_chips += pot
                time.sleep(1)

            elif player_rank < opponent_rank:

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