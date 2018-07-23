#Copyright (c) 2018 rajchelcm. Subject to the MIT License available at github.com/rajchelcm/pyDeck.

import random
from pyCard import *

class Deck(): 
    deck:[Card] = [] 

    def __init__(self, includeJokers = False):
        for s in Suit:
            if s == Suit.HEARTS or s == Suit.DIAMONDS:
                color = Color.RED
            else:
                color = Color.BLACK
            self.deck.append(Card(s, color, "A", 1))
            self.deck.append(Card(s, color, "2", 2))
            self.deck.append(Card(s, color, "3", 3))
            self.deck.append(Card(s, color, "4", 4))
            self.deck.append(Card(s, color, "5", 5))
            self.deck.append(Card(s, color, "6", 6))
            self.deck.append(Card(s, color, "7", 7))
            self.deck.append(Card(s, color, "8", 8))
            self.deck.append(Card(s, color, "9", 9))
            self.deck.append(Card(s, color, "10", 10))
            self.deck.append(Card(s, color, "J", 11))
            self.deck.append(Card(s, color, "Q", 12))
            self.deck.append(Card(s, color, "K", 13))
        if includeJokers:
            self.deck.append(Card(s, Color.RED, "JKR", 0))
            self.deck.append(Card(s, Color.BLACK, "JKR", 0))

    def __getitem__(self, index):
        return self.deck[index]

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
