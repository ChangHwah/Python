"""
    This is the file you edit.

    You *do not need to create a new file*. Just edit this file to achieve what is needed.

    Fill in the functions provided to solve the puzzle.

    DO NOT EDIT THE FUNCTION DEFINITION LINES. Just update the bodies of the functions.
"""

# Shuffling - See: https://note.nkmk.me/en/python-random-shuffle/
import random

'''
Log of cards played each round. Each card set must be a tuple, and tie breakers must be a tuple-of-tuples. Each tie-breaker round must show as separate tuples in the log, even if they chain off the previous one. All log entries (including within tie-breaker rounds) must be in the order the cards are played.
'''
round_log = []

def deal() -> dict:

    # A deck is generated
    deck = []

    for i in range(2, 15):
        deck.extend([i]*4)

    random.shuffle(deck)
    lenDeck = len(deck)

    # Deck is split in half
    halfDeck = lenDeck // 2

    # Player 1 takes the last half of deck
    # Player 2 takes the first half of deck
    player_1 = deck[:halfDeck] 
    player_2 = deck[halfDeck:]

    # Players 1 and 2 are object lists in this dictionary
    players = {
        'player_1' : player_1,
        'player_2' : player_2
    }
    return players

def play_round(players: dict) -> str:
    # First card in each object list
    p1_card = players['player_1'][0]
    p2_card = players['player_2'][0]

    # Delete that first card
    del players['player_1'][0]
    del players['player_2'][0]

    # If player 1 has the higher value card, give both cards to player 1 and 
    # log it
    if p1_card > p2_card:
        players['player_1'].append(p2_card)
        players['player_1'].append(p1_card)
        result = 'player_1'
        round_log.append((p1_card, p2_card))
        return result

    # If player 2 has the higher value card, give both cards to player 2 and 
    # log it
    elif p2_card > p1_card:
        players['player_2'].append(p1_card)
        players['player_2'].append(p2_card)
        result = 'player_2'
        round_log.append((p1_card, p2_card))
        return result

    # If cards are of same value, do not give back cards and log it
    else:
        result = 'tie'
        round_log.append((p1_card, p2_card))
        return result

def tie_breaker_round(players: dict) -> str:
    # Fourth card in each list
    p1_card = players['player_1'][3]
    p2_card = players['player_2'][3]

    # Variables declared so that they can be logged for the round 
    p1_cards_removed = players['player_1'][:3]
    p2_cards_removed = players['player_2'][:3]

    # Delete the first four cards in each list
    del players['player_1'][:4]
    del players['player_2'][:4]
    
    # Log of cards removed for round
    round_log.append(((p1_cards_removed[0], p2_cards_removed[0]), (p1_cards_removed[1], p2_cards_removed[1]), (p1_cards_removed[2], p2_cards_removed[2]), (p1_card, p2_card)))

    # If player 1 has higher fourth valued card, give cards played that round and 
    # cards removed from player 1 and player 2 to player 1
    if p1_card > p2_card:
        players['player_1'].append(p1_card)
        players['player_1'].append(p2_card)
        players['player_1'].extend(p1_cards_removed)
        players['player_1'].extend(p2_cards_removed)
        result = 'player_1'
        return result

    # If player 2 has higher fourth valued card, give cards played that round and 
    # cards removed from player 2 and player 1 to player 2
    elif p2_card > p1_card:
        players['player_2'].append(p1_card)
        players['player_2'].append(p2_card)
        players['player_2'].extend(p1_cards_removed)
        players['player_2'].extend(p2_cards_removed)
        result = 'player_2'
        return result

    # If cards are of same value, do not give back cards and log it
    else:
        result = 'tie'
        return result
            
def play_game() -> str:
    players = deal()
    # While loop to play game until return values execute
    while True:
        # variable result defined and pulled from play_round(players)
        # if the result is a tie, while it is a tie, define new result variable
        # for the tie_breaker_round(players)
        result = play_round(players)
        while result == "tie":
            result = tie_breaker_round(players)
        # If length of player 1 is less than or equal to 4, return winner player 2
        if len(players['player_1']) <= 4:
            return "player_2"
        # If length of player 2 is less than or equal to 4, return winner player 1
        elif len(players['player_2']) <= 4:
            return "player_1"
