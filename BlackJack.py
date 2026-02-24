#File Name: BlackJack
#Date: Monday 3rd of March 2025
#Author: Oliver Culbert

import random
import time

# ------------------- Variables ------------------------

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

#---------------- Functions ----------------
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == 'Ace')

    # Adjust Ace from 11 to 1 if bust
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

# ------------------- Start ------------------------

while True:
    # Create and shuffle deck
    deck = [(card, suit) for suit in suits for card in cards_list]
    random.shuffle(deck)

    # Deal cards
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]

    # ---------------- Player Turn ----------------
    while True:
        player_score = calculate_score(player_card)
        dealer_score = calculate_score(dealer_card)

        print("\nYour Cards:", player_card)
        print("Your Score:", player_score)
        print("Dealer Shows:", dealer_card[0])
        time.sleep(1)

        if player_score > 21:
            print("Player Bust! Dealer Wins.")
            time.sleep(1)
            break

        if player_score == 21:
            print("YOU HAVE BLACKJACK!")
            time.sleep(1)
            break

        choice = input("Hit or Stand? ").lower()

        if choice == "hit":
            player_card.append(deck.pop())
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please type 'hit' or 'stand'.")

    # ---------------- Dealer Turn ----------------
    player_score = calculate_score(player_card)
    dealer_score = calculate_score(dealer_card)

    if player_score <= 21:
        print("\nDealer's Turn...")
        time.sleep(1)

        while dealer_score < 17:
            dealer_card.append(deck.pop())
            dealer_score = calculate_score(dealer_card)

    # ---------------- Final Results ----------------
    print("\nFinal Hands:")
    print("Player:", player_card, "Score:", player_score)
    print("Dealer:", dealer_card, "Score:", dealer_score)
    time.sleep(2)

    if player_score > 21:
        print("Dealer Wins.")
        time.sleep(2)
    elif dealer_score > 21:
        print("Dealer Bust! Player Wins.")
        time.sleep(2)
    elif dealer_score > player_score:
        print("Dealer Wins.")
        time.sleep(2)
    elif dealer_score < player_score:
        print("Player Wins!")
        time.sleep(2)
    else:
        print("Dealer Wins.")
        time.sleep(2)

    # ---------------- Replay ----------------
    replay = input("\nPlay again? (yes/no): ").lower()
    if replay == "no":
        print("Thanks for playing!")
        break

