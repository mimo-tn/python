from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        # self.random_hand = []
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
    def show_the_rule(self):
        print("here are the rules : ")
        print("- each player randomly receives 7 cards by entering their name")
        print("- each player plays a card in their turn and the one who plays the card with more points wins one point on the score")
        print("- at the end of the game the one with the most score wins")
        return self

