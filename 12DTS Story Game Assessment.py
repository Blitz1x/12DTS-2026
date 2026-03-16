#File Name -- The Grand Poker Tournament
#Author -- Oliver Culbert
#Date -- 10/03/2026

# ---- ImportLibrary -----
import random
import time

# ---- Variables ----
#These are the variables for the card deck, the four suits and all the values in a normal game of texas holdem.
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
community_cards
player_hand = []
deck = []
values = []
suits = []
counts = {}
cards = player_hand + community_cards

card_values = {
    "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
    "Jack":11,"Queen":12,"King":13,"Ace":14
}

# ---- Functions ----
def create_deck(): #This is the code that creates the deck. It adds all the cards from each suit to create 1 deck of 52 cards.
    for suit in suits:
        for card in cards_list:
            deck.append(card + "of" + suit)
    return deck

def shuffle_deck(deck): # This code shuffles the deck so that every card is random and not just in order.
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
    return card_values[card.split("")[0]]
def get_suit(card): #Get the suit of the card
    return card.split("")[2]

def get_values(cards):
    for card in cards:
        values.append(get_value(card))
    return values

def get_suits(cards):
    for card in cards:
        suits.append(get_suit(card))
    return suits

def count_values(values): #To see doubles triples etc.
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts = 1
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
    for i in range (len(values)-4) #Normal Straight 2,3,4,5,6 etc
        if values[i+4] - values[i] == 4:
            return True
    if set([14,2,3,4,5]): #For low straight Ace,2,3,4,5
        return True
    return False

def evaluate_hand(hand, community):
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


# ---- Loop ----