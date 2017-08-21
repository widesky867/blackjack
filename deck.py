# deck class
# code adapted from https://brilliant.org/wiki/programming-blackjack/
# editted to include elements of OOP as a practice

from random import shuffle

values = [_ for _ in range(2,11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADES', 'HEARTS', 'CLUBS', 'DIAMONDS']

class Deck(object):

    # initialise the card ranks and suits

    def __init__(self):
        # return a deck of cards
        self.cards = []
        self.reshuffle()

    def reshuffle(self):
        # self.deck = [[rank, suit] for rank in ranks for suit in suits]
        # shuffle(self.deck)
        for s in suits:
            for v in values:
                self.cards.append(Card(s,v))

        shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value,"of",self.suit, end=" ")
