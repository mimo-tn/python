class Player:
    def __init__(self, dic_player):
        self.name = dic_player["name"]
        self.age = dic_player["age"]
        self.position = dic_player["position"]
        self.team = dic_player["team"]
    @classmethod
    def get_team(cls,team_list):
        new_team = []
        for list_player in team_list :
            new_team.append(list_player)
        return new_team

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

original_list = [
    player_kevin,
    player_jason,
    player_kyrie
] 

new_team = Player.get_team(original_list)

for player in new_team:
    print(player.name)