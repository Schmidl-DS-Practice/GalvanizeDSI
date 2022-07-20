import random

def shuffle(deck):  
    random.shuffle(deck) 
     
def shuffle_and_draw(deck): 
     
    shuffle(deck) 
     
    return deck.pop() 

def make_deck(suits, numbers, faces):
    vals = numbers + faces
    deck = [str(val) + ' of ' + suit for val in vals for suit in suits]
    return deck

if __name__=='__main__':
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    numbers = list(range(2,11))
    faces = ['J', 'Q', 'K', 'A']
    vals = numbers + faces
    deck = [str(val) + ' of ' + suit for val in vals for suit in suits]
    print("Here are the first 10 cards in the deck I made after the if-name-main block!")
    print(deck[:10])
    deck2 = make_deck(suits, numbers, faces)
    if deck2 == deck:
        print("The decks are the same!")
    else:
        print("Wrong, try again.")

