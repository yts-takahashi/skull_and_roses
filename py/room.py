import websockets
from game import Game


class Room:
    def __init__(self):
        self.players: dict[str: websockets] = {}
        self.game: Game = Game()

    def admit(self, player_name: str, ws: websockets):
        self.players[player_name] = ws
    
    def exclude(self, player_name):
        self.players.pop(player_name)

    def get_players_list(self):
        return [{"name": name} for name in self.players.keys()]
        
    def game_start(self):
        # TODO not to enter the room during the game.
        self.game.start(self.players)

    def game_end(self):
        self.game.end()
