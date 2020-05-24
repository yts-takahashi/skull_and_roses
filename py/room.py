from player import Player
from game import Game
class Room:
  def __init__(self, name):
    self.players = {}
    self.name = name
    self.game:Game = Game()

  def admit(self, player:Player):
    self.players[player.name] = player
  
  def exclude(self, player_name):
    self.players.pop(player_name)

  def get_players_list(self):
    return [{"name":str(player)} for player in self.players]
    
  def game_start(self):
    # TODO not to enter the room during the game.
    self.game.start(self.players)

  def game_end(self):
    self.game.end()

  def __eq__(self, other):
    if not isinstance(other, Room):
        return NotImplemented
    return self.name == other.name

  def __hash__(self):
      return hash(self.name)  

  def __str__(self):
    return self.name
