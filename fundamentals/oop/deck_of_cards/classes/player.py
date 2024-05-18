from .hand import hand
class player :
    def __init__(self):
        self.name = ""
        self.score = 0
        self.player_hand = hand()
        self.chosen_card = 0
    def creating_player(self):
        self.name = input('Hello What is your name player ?')
        print(f'this is your hand {self.name} good luck ')
        self.player_hand.random_start_hand()
        self.player_hand.show_hand()
    def play(self):
        test = False
        while(test == False):
            card_played = input(f'{self.name} its your turn to play choose your card')
            test = self.player_hand.test_input_card(card_played)
            if(test == False):
                print("Sorry ! you must write a card from your hand and in this form  7 of hearts")
            else:
                self.chosen_card = self.player_hand.point_card_val
        self.player_hand.show_hand()
    def show_hand_player(self):
        self.player_hand.show_hand()   
        return self
    def player1_vs_player2(self,player):
        if(self.chosen_card > player.chosen_card):
            self.score = self.score + 1
        elif(self.chosen_card < player.chosen_card):
            player.score = player.score + 1
        else:
            print('both players are equal')
        print(f'the score of {self.name} : {str(self.score)}')
        print(f'the score of {player.name} : {str(player.score)}')
        return self
    def player1_vs_player2_winner(self,player):
        if(self.score > player.score):
            print(f'Well done {self.name} you won ')
        elif(self.score < player.score):
            print(f'Well done {player.name} you won ')
        else:
            print('both players are equal')