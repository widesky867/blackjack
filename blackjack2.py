# main file for OO blackjack
# code adapted from https://brilliant.org/wiki/programming-blackjack/
# editted to include elements of OOP as a practice

from player import player
from deck import Deck
import time

def endGame():
    if input("Continue? Yes/No \n").lower() in 'yes y'.split():
        Deck.reshuffle()
        playerOne.reset_hand()
        dealer.reset_hand()
        return True
    else:
        return False

Deck = Deck()
game = True
name = input("Welcome to Blackjack. Please input your name: ")
playerOne = player(name)
dealer = player("DEALER")

#start game
while game:
    # deal cards
    playerOne.deal(Deck).deal(Deck)
    dealer.deal(Deck).deal(Deck)

    while playerOne.player_in:
        if playerOne.getScore()[1] == 100:
            print(playerOne.getScore()[0])
            break
        elif playerOne.getScore()[0] in 'BLACKJACK':
            print("\n",playerOne.name,"currently has",playerOne.getScore()[0],"with the hand", end=" ")
            playerOne.showHand()
            print("You beat the dealer with",playerOne.getScore()[0])
            game = endGame()
            break
        elif playerOne.getScore()[0] in 'LUCKYSTRIKE':
            print("You beat the dealer with",playerOne.getScore()[0])
            game = endGame()
            break

        print("\n",playerOne.name,"currently has",playerOne.getScore()[0],"with the hand", end=" ")
        playerOne.showHand()

        if playerOne.player_in:
            if input("\nHit or stay? Hit = 1, Stay = 0\n").lower() in '1 hit'.split():
                playerOne.deal(Deck)
                # show the last card drawn (last element of the list)
                print("Drew", end=" ")
                playerOne.hand[-1].show()
                time.sleep(1)
            else:
                playerOne.player_in = False

    if playerOne.getScore()[1] <= 21:
        print("\n Dealer is at ",dealer.getScore()[0]," with the hand", end=" ")
        dealer.showHand()
        while dealer.getScore()[1] < 17:
            time.sleep(1)
            print("\nDealer draws from deck.")
            dealer.deal(Deck)
            print("Drew", end=" ")
            dealer.hand[-1].show()
        if playerOne.getScore()[1] < 100 and dealer.getScore()[1] == 100:
            print("You beat the dealer!")
        elif playerOne.getScore()[1] > dealer.getScore()[1]:
            print("You beat the dealer!")
        elif playerOne.getScore()[1] == dealer.getScore()[1]:
            print("You tied the dealer, nobody wins.")
        elif playerOne.getScore()[1] < dealer.getScore()[1]:
            print("Dealer wins with",dealer.getScore()[0])

    else:
        print("Dealer wins.")

    game = endGame()
