#File Name -- The Grand Poker Tournament
#Author -- Oliver Culbert
#Date -- 10/03/2026
#Texas Holdem Tournament - No money involved!!
#Card Dealing, "Betting Rounds" - No money just special chips, Hand evaluation Royal Flush - High Card, Opponent decision making, Tournament progression.

# ---- ImportLibrary -----
import random #Shuffling cards and random decisions
import time # Typewriter effect and displays
import sys # For typewriter code
from itertools import combinations # For 5 card hand evaluation so it sees all 5 card possiblities

# ---- Constants ----
STARTING_CHIPS = 500 #Chips each player and opponent starts with
MINIMUM_BET = 50 #Minimum bet used for blinds

# ---- Variables ----
#These are the variables for the card deck, the four suits and all the values in a normal game of texas holdem.
deck_suits = ["Hearts", "Diamonds", "Clubs", "Spades"] #Suits in a deck
cards_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] #List of the cards in a standard deck of cards used in poker

player_hand = []   #Stores player hand
community_cards = []    #Stores the community cards Flop Turn River etc.
deck = []        # The current deck of cards

raise_amount     = 50   #The default raise amount

card_values = {# The values for the different cards.
    "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
    "Jack":11,"Queen":12,"King":13,"Ace":14
}

opponents = [#Opponents with different skill levels 1 = easy 3 = hard
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

def value_to_name(value):# Convert card value back to name 14 --> Ace
    names = {
        14: "Ace",
        13: "King",
        12: "Queen",
        11: "Jack",
        10: "10",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2"
    }
    return names[value]

def describe_hand(score, values): #Describe the hand, Straight flush to the 7 of diamonds etc.
    if score == 8:#Straight Flush
        if values[0] == 14:
            return "Royal Flush"
        return "Straight Flush to the " + value_to_name(values[0])
    elif score == 7:#Four of a kind
        kicker = value_to_name(values[1])
        return "Four of a Kind (" + value_to_name(values[0]) + "s, Kicker: " + kicker + ")"
    elif score == 6:#Full House
        return("Full House (" + value_to_name(values[0]) + "s over " + value_to_name(values[1]) + "s)")
    elif score == 5:#Flush
        return "Flush, " + value_to_name(values[0]) + " high"
    elif score == 4:#Straight
        return "Straight to the " + value_to_name(values[0])
    elif score == 3:#Three of a Kind
        kicker1 = value_to_name(values[1])
        kicker2 = value_to_name(values[2])
        return "Three of a Kind (" + value_to_name(values[0]) + " s, Kickers: " + kicker1 + ", " + kicker2 + ")"
    elif score == 2: # Two Pair
        kicker = value_to_name(values[2])
        return("Two Pair (" + value_to_name(values[0]) + "s and " + value_to_name(values[1]) + "s, Kicker: " + kicker + ")")
    elif score == 1: #Pair
        kicker1 = value_to_name(values[1])
        kicker2 = value_to_name(values[2])
        kicker3 = value_to_name(values[3])
        return "Pair of " + value_to_name(values[0]) + "s (Kickers: " + kicker1 + ", " + kicker2 + ", " + kicker3 + ")"
    else:
        kicker1 = value_to_name(values[1])
        kicker2 = value_to_name(values[2])
        kicker3 = value_to_name(values[3])
        kicker4 = value_to_name(values[4])
        return value_to_name(values[0]) + " High (Kicker: " + kicker1 + ", " + kicker2 + ", " + kicker3 + ", " + kicker4 + ")"


def create_deck(): #This is the code that creates the deck. It adds all the cards from each suit to create 1 deck of 52 cards.
    deck.clear() # Clears the deck before creating and creates a standard 52 card deck
    for suit in deck_suits:
        for card in cards_list:
            deck.append(card + " of " + suit)
    return deck

def shuffle_deck(): # This code shuffles the deck so that every card is random and not just in order.
    random.shuffle(deck)

def deal_player():#Deals players cards 2 cards.
    for i in range(2):
        player_hand.append(deck.pop())
    return player_hand

def deal_flop(deck): #This is the code for the community cards, the flop, turn, and river.
    return [deck.pop(), deck.pop(), deck.pop()]

def deal_turn(deck): #Deal Turn
    return [deck.pop()]

def deal_river(deck): #Deal River
    return [deck.pop()]

def player_action(): #What the player would like to do in betting round
    print("\nChoose Action 1 - 4")
    print("1. Check/Call")
    print("2. Raise")
    print("3. Fold")
    print("4. ALL-IN")

    while True:
        action = input("> ")
        if action in ["1", "2", "3", "4"]:
            return action
        else:
            print("Invalid Action please choose 1 - 4")

def get_value(card): #Get the value of the cards Ace of Hearts --> 14
    return card_values[card.split()[0]]
def get_suit(card): #Get the suit of the card Ace of Hearts --> Hearts
    return card.split()[2]

def get_values(cards):# Get the values of each card  Ace = 1 etc.
    values = []
    for card in cards:
        values.append(get_value(card))
    return values

def get_suits(cards):# The suit of the card
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

def is_flush(suits): #To see if you have a flush in 5 cards
    suit_counts = {}

    for suit in suits:
        suit_counts[suit] = suit_counts.get(suit, 0) + 1

    for count in suit_counts.values():
        if count >= 5:
            return True
    return False

def is_straight(values): # See if you have a straight Ace can be high or low
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

    bluff_chance = { #Higher the skill level less chance of bluff
        1: 0.30,
        2: 0.20,
        3: 0.10
    }

    bluff = random.random()

    #Preflop when don't have 5 cards. Make it so it judges of high card for pre flop
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

    values = sorted(get_values(cards), reverse = True) # Sort cards high to low
    suits = get_suits(cards)
    counts = count_values(values) #Count the duplicates for pairs triple etc

    pairs = [] #Identify the multiples
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

    # The points for all the different hands in order of strength.
    #Check for straight flush properly
    if flush:
        for suit in set(suits):
            suited_cards = []

            for i in range(len(cards)):
                if suits[i] == suit:
                    suited_cards.append(values[i])

            suited_cards = sorted(set(suited_cards), reverse = True)

            if is_straight(suited_cards):
                return (8, suited_cards)
    if four:#Four of a Kind
        kicker = [v for v in values if v != four]
        return (7, [four] + kicker)
    elif three and pairs: #Full House
        return (6, [three, max(pairs)])
    elif flush:#Flush
        return (5,values)
    elif straight:#Straight
        return (4, values)
    elif three:#Three of a Kind
        kicker = [v for v in values if v != three]
        return (3, [three] + kicker)
    elif len(pairs) >= 2: #2 Pair
        high_pair = max(pairs)
        low_pair = min(pairs)
        kicker = [v for v in values if v != high_pair and v != low_pair]
        return (2, [high_pair, low_pair] + kicker)
    elif len(pairs) == 1:#Pair
        pair = pairs[0]
        kickers = [v for v in values if v != pair]
        return (1, [pair] + kickers)
    else:#High Card
        return (0, values)

def evaluate_hand(player_hand,community_cards): # Evaluate your hand the best possible one with the community and player cards using combinations to find the highest ranking hand
    all_cards = player_hand + community_cards

    if len(all_cards) < 5:
        return (0, [])#Not enough cards yet

    best_rank = (-1, [])

    for combo in combinations(all_cards, 5):#Evaluate every 5 card combination out of all 7 cards
        rank = evaluate_5card_hand(list(combo))

        if rank > best_rank:
            best_rank = rank
    return best_rank

def hand_name(score): # The hand names so it gives back a actual hand
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
    #Handle betting between the player and opponent updates the chip and pot based on the actions

    global player_chips # How many chips your opponent and you have.
    global opponent_chips

    current_bet = 0
    player_bet = 0
    opponent_bet = 0

    if player_chips == 0 or opponent_chips == 0: #If anyone has 0 chips auto end betting see it as all in being called
        return pot, "all_in"

    if player_chips <= 0:# If you are out of chips ask to restart.
        type_text("\nYou are out of chips")
        restart()

    while True:

        print("\nPlace your bets")#Display current betting info
        print("Pot:", pot)
        print("Your Chips:", player_chips)
        print(opponent["name"] + " Chips:", opponent_chips)

        action = player_action() #What you decide to do.

        if action == "3":# Player folds
            type_text("\nYou Folded")
            opponent_chips += pot
            time.sleep(1)

            return pot, "player_fold"

        elif action == "1": #Player calls or checks
            call_amount = current_bet - player_bet

            if call_amount > 0:
                if call_amount > player_chips:
                    call_amount = player_chips

                player_chips -= call_amount
                pot += call_amount
                player_bet += call_amount

                type_text("\nYou call " + str(call_amount) + " chips!")
            else:
                type_text("\nYou Check")

        elif action == "4":#Player goes all in
            if player_chips > 0:
                type_text("\nYou go ALL-IN")

                pot += player_chips
                player_bet += player_chips
                current_bet = max(current_bet, player_bet)
                player_chips = 0

                #Let opponent decide
                opponent_move = opponent_decision(opponent, opponent_hand, community_cards)
                if opponent_move == "fold":
                    type_text("\nOpponent folded")
                    player_chips += pot
                    return pot, "opponent_fold"
                elif opponent_move == "call":
                    call_amount = min(current_bet - opponent_bet, opponent_chips)
                    opponent_chips -= call_amount
                    pot += call_amount
                    opponent_bet += call_amount

                    type_text("\nOpponent calls")

                    return pot, "all_in"

            else:
                type_text("\nYou Check")

            time.sleep(1)

        elif action =="2":#Player raises
            try:
                raise_amount = int(
                    input("Enter raise amount: ")
                )

                if raise_amount <= 0:
                    print("Raise amount can't be less than or equal to 0")
                    continue

                total_raise = (current_bet - player_bet + raise_amount)

                if player_chips == 0:
                    print("You have no chips left!")
                    return pot, "all_in"

                if total_raise > player_chips:
                    # Auto ALL-IN instead
                    type_text("\nNot enough chips — going ALL-IN!")

                    pot += player_chips
                    player_bet += player_chips
                    player_chips = 0

                    return pot, "all_in"

                player_chips -= total_raise
                pot += total_raise

                player_bet += total_raise
                current_bet = player_bet

                type_text(
                    "\nYou raised " +
                    str(current_bet)
                )
                time.sleep(1)

            except ValueError:
                print("Invalid number.")
                continue

        time.sleep(1)

        opponent_move = opponent_decision(opponent, opponent_hand, community_cards) #Opponents responds to the players actions

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
                MINIMUM_BET,
                MINIMUM_BET * opponent["skill"] * 2
            )

            total_raise = (current_bet - opponent_bet + raise_amount)

            if total_raise > opponent_chips:
                total_raise = opponent_chips

            opponent_chips -= total_raise
            pot += total_raise

            opponent_bet += total_raise
            current_bet = opponent_bet

            print(
                opponent["name"],
                "raises to",
                current_bet
            )
            time.sleep(1)

        if player_bet == opponent_bet: #End betting when bets are equal
            break

    return pot, "continue"

def restart():#Restart the game when you are out of chips or when you finish
    while True:
        again = input("\nWould you like to play again (y/n)? ").lower()

        if again == "y" or again == "yes":
            global player_chips, opponent_chips
            player_chips = STARTING_CHIPS
            opponent_chips = STARTING_CHIPS
            type_text("\nRestarting Tournament...")
            time.sleep(1)
            start()
            return

        elif again == "n" or again == "no":
            type_text("\nThanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter y or n.")

def show_instructions():#Display the instructions for standard texas hold'em
    print("\n--- HOW TO PLAY ---")
    print("You are playing Texas Hold'em Poker.")
    print("You receive 2 cards.")
    print("Your opponent recieves 2 cards.")
    print("5 community cards are dealt. The Flop, Turn and River, Flop = 3 cards, Turn = 1, River = 1")
    print("Choose actions in between Flop, Turn, River:")
    print("1 = Check/Call")
    print("2 = Raise")
    print("3 = Fold")
    print("4 = All-In")
    print("Win chips by beating your opponent Who ever has the highest hand.")
    print("Order of Hands:\n"
          "Straight Flush = 5 cards in order of same suit\n"
          "Four of a Kind = 4 cards of the same number 4 aces etc\n"
          "Full House = 3 cards of 1 number and another 2 of a different number, 3 Aces and 2 Kings\n"
          "Straight = 5 cards in order of value\n"
          "Three of a Kind = 3 cards of same value, 3 Aces\n"
          "Two Pair = 2 Pairs of different cards, 2 Aces and 2 Kings\n"
          "Pair = one pair, 2 Aces\n"
          "High Card = Highest card in your hand, One King etc")
    print("Order of Cards = 2,3,4,5,6,7,8,9,10,Jack,Queen,King and Ace can be either below the 2 or above the King so Ace, 2 or King, Ace")
    print("--------------------\n")

def start():#Main function controls the whole tournament, betting rounds, card dealing, betting rounds, determining winners etc.
    type_text("\nThe tournament begins...\n")

    global player_chips
    global opponent_chips

    # Loop through opponents (levels)
    for i, opponent in enumerate(opponents):
        player_chips = STARTING_CHIPS
        opponent_chips = STARTING_CHIPS
        type_text("\nYour next opponent is " + opponent["name"])

        while player_chips > 0 and opponent_chips > 0:

            if player_chips <= 0:
                type_text("\nYou have been eliminated from the tournament!")
                result = restart()
                if result == "restart":
                    return
                break

            time.sleep(1)

            # Reset Hands
            player_hand.clear()
            community_cards.clear()
            opponent_hand = []

            # Create and shuffle deck
            create_deck()
            shuffle_deck()

            pot = MINIMUM_BET * 2

            player_chips -= MINIMUM_BET
            opponent_chips -= MINIMUM_BET
            type_text("\nBlinds posted (" + str(MINIMUM_BET) + " each)")
            time.sleep(1)

            # Deal Player Cards
            deal_player()
            opponent_hand = [deck.pop(), deck.pop()]
            time.sleep(1)

            print("\nYour Cards:")
            for card in player_hand:
                print(card)
            time.sleep(2)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)#Pre flop betting

            if result == "player_fold" or result == "opponent_fold":
                continue

            input("\nPress ENTER to deal the flop")

            community_cards.extend(deal_flop(deck))#Deal the flop

            print("\nFlop")
            for card in community_cards:
                print(card)

            score, values = evaluate_hand(player_hand, community_cards)#Show current hand
            print("Current hand:", describe_hand(score, values))

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)#Flop betting

            if result == "player_fold" or result == "opponent_fold":
                continue

            input("\nPress ENTER to deal the turn")

            community_cards.extend(deal_turn(deck))

            print("\nTurn:")
            for card in community_cards:
                print(card)

            score, values = evaluate_hand(player_hand, community_cards)
            print("Current hand:", describe_hand(score, values))

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)

            if result == "player_fold" or result == "opponent_fold":
                continue

            input("\nPress ENTER to deal the river")

            community_cards.extend(deal_river(deck))

            print("\nRiver:")
            for card in community_cards:
                print(card)

            pot, result = betting_round(opponent, opponent_hand, community_cards, pot)

            if result == "player_fold" or result == "opponent_fold":
                continue

            # Ensure 5 cards if ALL-IN happened
            while len(community_cards) < 5:

                if len(community_cards) == 0:
                    community_cards.extend(deal_flop(deck))

                elif len(community_cards) == 3:
                    community_cards.extend(deal_turn(deck))

                elif len(community_cards) == 4:
                    community_cards.extend(deal_river(deck))

            # Evaluate Hands
            player_rank = evaluate_hand(player_hand, community_cards)
            opponent_rank = evaluate_hand(opponent_hand, community_cards)
            time.sleep(2)

            print("\nOpponent Cards")
            for card in opponent_hand:
                print(card)
            time.sleep(2)

            player_score, player_values = player_rank
            opponent_score, opponent_values = opponent_rank

            player_describe = describe_hand(player_score, player_values)
            opponent_describe = describe_hand(opponent_score, opponent_values)

            print("\nYou got", player_describe)
            print(opponent["name"], "got", opponent_describe)

            if player_rank > opponent_rank:#Determnine the winner
                type_text("\nPlayer wins with " + player_describe)

                player_chips += pot
                time.sleep(3)

            elif player_rank < opponent_rank:
                type_text("\nOpponent wins with " + opponent_describe)
                opponent_chips += pot
                time.sleep(1)

            else:
                type_text("\nIt's a draw! You both have " + player_describe)

                split_pot = pot // 2
                player_chips += split_pot
                opponent_chips += split_pot

                if pot % 2 != 0:
                    player_chips += 1


            if player_chips > 0 and opponent_chips == 0:
                if i == len(opponents) - 1:
                    type_text("\nYou are the GRAND POKER CHAMPION!")#You are the winner if you beat all opponents
                    exit()
            elif player_chips == 0:
                type_text("\nYou have been eliminated from the tournament!")
                result = restart()
                if result == "restart":
                    return
# ---- Loop ----
name = input("What is your name?")


type_text("Welcome to the Grand Poker Championship, " + name + "!")
time.sleep(1)

type_text("\n---You sit at the table, your stunning Championship chips stacked neatly in front of you.---\n"
          "---The room is still, the silence only broken by the murmur of spectators and the clinking of chips.---\n"
          "---Players from all over the world have been invited, you studied them, some are cautious they wait for the perfect hand---\n"
          "---others bluff hiding their hand behind a poker face developed over years.---\n"
          "---You are the newest challenger no one knows what to expect.---\n"
          "---You are playing for no money, Win you are remembered, Lose you walk away.---\n"
          "---This is the Grand Poker Championship it is down to you to choose what to play!---\n")
time.sleep(1)

show_instructions()

while True:
    play = input("Would you like to play (y/n)? ").lower()
    if play == "y" or play == "yes":
        start()

    elif play == "n" or play == "no":
        type_text("\nMaybe next time.")
        exit()

    else:
        print("Invalid input. Please enter y or n.")

