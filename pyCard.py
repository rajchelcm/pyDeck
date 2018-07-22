#Copyright (c) 2018 rajchelcm. Subject to the MIT License available at github.com/rajchelcm/pyDeck.

from enum import Enum

#An enumeration class to represent each card color
class Color(Enum):
    RED = 1
    BLACK = 2

#An enumeration class to represent each of the suits
class Suit(Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    CLUB = "C"
    SPADES = "S"

#A card class to represent each of the attributes of a playing card
class Card:
    suit:Suit
    color:Color
    rank:str
    value:int
    def __init__(self,Suit,Color,rank,value):
        self.suit = Suit
        self.color = Color
        self.rank = rank
        self.value = value
    def __str__(self):
        return self.rank+str(self.suit.value)
    
