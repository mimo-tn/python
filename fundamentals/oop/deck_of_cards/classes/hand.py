from .deck import Deck
import random
class hand(Deck):
    def __init__(self):
        self.hand_of_player = []
        self.point_card_val = 0
        super().__init__()
    def random_start_hand(self):
        while(len(self.hand_of_player)<7):
            random_card = random.choice(self.cards)
            if(random_card not in self.hand_of_player):
                self.hand_of_player.append(random_card)
    def show_hand(self):
        for card in self.hand_of_player:
            card.card_info()
    def test_input_card(self, card_played):
        test = False
        for card in self.hand_of_player:
                if card_played == card.string_val +" of "+ card.suit:
                    test = True 
                    self.point_card_val = card.point_val
                    # self.card_play(card)
                    self.hand_of_player.remove(card)
        return test