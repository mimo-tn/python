from classes.deck import Deck
from classes.hand import hand
from classes.player import player
bicycle = Deck()
bicycle.show_the_rule()
player_hand = hand()
player_1 = player()
player_2 = player()
player_1.creating_player()
player_2.creating_player()
for i in range(7):
    print(f'************ hand of player {player_1.name} ************')
    player_1.show_hand_player()
    player_1.play()
    print(f'************ hand of player {player_2.name} ************')
    player_2.show_hand_player()
    player_2.play()
    player_1.player1_vs_player2(player_2)
player_1.player1_vs_player2_winner(player_2)
