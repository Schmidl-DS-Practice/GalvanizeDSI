from deck import make_deck, shuffle, shuffle_and_draw
import random

def play_war(deck):
    
    card_1 = shuffle_and_draw(deck)
    card_2 = shuffle_and_draw(deck)
    
    print(f'''
    Card 1: {card_1}
    Card 2: {card_2}
    ''')

if __name__ == '__main__':
    
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    numbers = list(range(2,11))
    faces = ['J', 'Q', 'K', 'A']
    
    deck = make_deck(suits, numbers, faces)
    
    play_war(deck)
    
    
