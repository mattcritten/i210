import random as r


def make_deck(ranks, suits):
    card_deck = []
    for i in range(0, len(suits)):
        for j in range(0, len(ranks)):
            card_deck.append(ranks[j] + suits[i])
    r.shuffle(card_deck)
    return card_deck

def deal(hand, deck, cards):
    for j in range(0, int(cards)):
        hand.append(deck.pop())
        j += 1

def main():
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♠", "♥", "♦", "♣"]
    deck = make_deck(ranks, suits)
    players = input("How many players? ")
    cards = input("How many cards per player? ")
    for i in range(int(players)):
        hand = []
        deal(hand, deck, cards)
        print(f"Player {i + 1}'s hand: {hand}")
        
        
if __name__ == "__main__":
    main()