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
def type_text(text, speed=0.07): #Typewriter effect
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

def opponent_decision(opponent, community_cards):

    opponent_hand = [deck.pop(), deck.pop()]

    score, best_hand = evaluate_hand(opponent_hand, community_cards)
    skill = opponent["skill"]
    bluff_chance = {
        1: 0.30,
        2: 0.20,
        3: 0.10
    }

    bluff = random.random()

    if score >= 5:
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
    return opponent_hand, action

def evaluate_5card_hand(cards):

    values = get_values(cards)
    suits = get_suits(cards)
    counts = count_values(values)

    pairs = 0
    three = False
    four = False

    for c in counts.values():
        if c == 2:
            pairs += 1
        elif c == 3:
            three = True
        elif c == 4:
            four = True

    flush = is_flush(suits)
    straight = is_straight(values)

    if straight and flush:
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

def evaluate_hand(player_hand,community_cards):
    all_cards = player_hand + community_cards

    best_score = - 1
    best_hand = None

    #Check all 5 card combinations
    for combo in combinations(all_cards, 5):
        score = evaluate_5card_hand(list(combo))

        if score > best_score:
            best_score = score
            best_hand = combo

    return best_score, best_hand

def hand_name(score):
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
          "As the dealer shuffles you study your opponent carefully, a twitch in the eye, a tap on the table,"
          "everything is a clue, it could tell you what you want to know or lead you into a trap.\n"
          "This is the Grand Poker Championship it is down to you to choose what to play!\n")
time.sleep(1)

play = input("Would you like to play (y/n)?")

if play.lower() == "y" or play.lower() == "yes":
    while True:
        type_text("First opponent:)
