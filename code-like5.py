import random as rnd

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♦", "♣"]
card_deck = []

for i in range(0, len(suits)):
    for j in range(0, len(ranks)):
        card_deck.append(ranks[j] + suits[i])

print(card_deck)

rnd.shuffle(card_deck)
print(card_deck)

players = 0
while not(1 <= players <= 5):
    players = int(input("How many players are there (1 - 5)? "))
    if not(1 <= players <= 5):
        print("You may only choose numbers between 1 and 5.")

player_hands = {}
for i in range(0, players):
    index = str(i + 1)
    hand = []
    for j in range(0, 5):
        hand.append(card_deck.pop())
        j += 1
    player_hands[index] = hand
    print(f"Player {index}'s hand: {hand}")
    i += 1