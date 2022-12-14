# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['decks', 'ranks', 'Deck']

# %% ../nbs/01_deck.ipynb 2
import sys

sys.path.insert(1, '../nbdev_cards')
from .card import *

# %% ../nbs/01_deck.ipynb 4
decks = ["\u2665", "\u2660","\u2663", "\u2666"]
ranks = ["A"] + [str(i) for i in range(2, 12)] + ["B", "Q", "K"]

# %% ../nbs/01_deck.ipynb 5
class Deck:
    "A deck of 52 cards, not including jokers"
    def __init__(self):
        self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
        
    def __str__(self):
        return '; '.join(map(str, self.cards))
    
    def __len__(self):
        return len(self.cards)
    
    def __contains__(self, card):
        return card in self.cards
    
    __repr__ = __str__

# %% ../nbs/01_deck.ipynb 11
@patch
def pop(self:Deck, 
        idx: int = - 1): # the index of the card to remove, defaulting to the last one
    "Remove a `card` from the deck, by its index, defaulting to the last one"
    return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 13
@patch
def remove(self:Deck, 
        card:Card): # remove the passed card from the deck
    "Remove `card` from the deck"
    return self.cards.remove(card)
