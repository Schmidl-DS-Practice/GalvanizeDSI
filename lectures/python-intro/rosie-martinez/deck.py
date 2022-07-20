def make_deck(suits, numbers, faces):
    '''Makes and returns a deck of cards

       Parameters
       ----------
       suits: list of strings
       numbers: list of numbers
       faces: list of strings

       Returns
       -------
       deck: list of strings
    '''
    vals = numbers + faces
    deck = [str(val) + ' of ' + suit for val in vals for suit in suits]
    return deck

print(__name__)

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
