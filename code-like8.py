# Section 1 - Add to the function to print a hand, card by card 
def print_hand(hand, last="\n"):  
    print("Cards: ", end="")
    for card in hand:
        print(card, end=" ")
    print("", end=last)

# Section 2 - Write a function that computes a score based on ranks
def score_ranks(hand): 
    score = 0
    ranks = {"J": 1, "Q": 2, "K": 3, "A": 4}
    for card in hand:
        if card[0] in ranks.keys():
            score += ranks[card[0]]
    return score

# Section 3 - Write a function that computes a score based on ranks
def score_suits(hand): 
    score = 0
    suits = {"♣": 0, "♦": 0, "♥": 0, "♠": 0}
    for card in hand:    
        suits[card[1]] += 1
    for suit in suits.keys():
        if suits[suit] == 0:
            score += 1
    return score

# Section 4 - Compute each hand’s score and the winning hand
def print_winner(all_hands): 
    winner = [[], 0]
    for hand in all_hands:
        score = score_suits(hand) + score_ranks(hand)
        if score > winner[1]:
            winner[0] = hand
            winner[1] = score  
    print(f"Winning Hand: {winner[0]}")
    
# This is  your main section code.
# Update this as you go!
if __name__ == "__main__":
    player_hands = [['J♣', '9♠', 'A♥', '2♥', '4♦'],
                    ['5♠', '6♣', '6♥', 'K♥', '8♦'],
                    ['A♠', '8♠', '3♠', 'Q♦', 'Q♣'],
                    ['5♦', '8♣', 'A♥', '3♣', 'K♦'],
                    ['J♦', '9♣', 'Q♥', '3♥', 'A♦'],
                    ['4♠', '4♥', '7♣', '9♣', '2♣']]
    
    print("All Hands:")
    for hand in player_hands:
        print(hand)
    print()
    for hand in player_hands:
        print_hand(hand)
    print()    
    for hand in player_hands:
        print(hand)
        print(f"Score by Rank: {score_ranks(hand)}")
    print()    
    for hand in player_hands:
        print(hand)
        print(f"Score by Suit: {score_suits(hand)}")
    print()
    for hand in player_hands:
        print_hand(hand, "\t")
        print(f"Hand Score: {score_ranks(hand) + score_suits(hand)}")
    print()
    print_winner(player_hands)

