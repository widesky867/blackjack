# player class file, includes dealer as well
# code adapted from https://brilliant.org/wiki/programming-blackjack/
# editted to include elements of OOP as a practice
from deck import values

class player(object):

    def __init__(self, name):
        self.name = name
        self.reset_hand()

    def reset_hand(self):
        self.hand = []
        self.player_in = True

    def deal(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def getScore(self):
        tmp_value = sum(self.card_value(_) for _ in self.hand)

        num_aces = len([_ for _ in self.hand if _.value is 'ACE'])

        while num_aces > 0:
            if tmp_value > 21 and 'ACE' in values:
                tmp_value = tmp_value - 10
                num_aces = num_aces - 1
            else:
                break
        if len(self.hand) == 5 and tmp_value <= 21:
            # conditions of LUCKYSTRIKE, 5 cards and total score <= 21
            return ["LUCKYSTRIKE", tmp_value]
        elif len(self.hand) == 2 and tmp_value == 21:
            return ["BLACKJACK", 21]
        elif tmp_value <= 21:
            return [str(tmp_value), tmp_value]
        else:
            return ["BUST", 100]

    def card_value(self, card):
        # return value of a card
        value = card.value

        if value in values[0:-4]:
            return int(value)
        elif value is 'ACE':
            return 11
        else:
            return 10
