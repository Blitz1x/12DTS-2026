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
deck = []

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
    player_hand = []
    for i in range(2):
        player_hand.append(deck.pop())
    return player_hand

def deal_flop(deck): #This is the code for the community cards, the flop, turn, and river.
    return [deck.pop(), deck.pop(), deck.pop()]

def deal_turn(deck):
    return [deck.pop()]

def deal_river(deck):
    return [deck.pop()]

def player_action():
    print("\nChoose Action")
    print("1. Check/Call")
    print("2. Raise")
    print("3. Fold")

    action = input("> ")
    return action

def get_value(card):
    return card_values[card.split("")[0]]
def get_suit(card):
    return card.split("")[2]


# ---- Loop ----