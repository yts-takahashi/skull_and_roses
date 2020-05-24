from player import Player
class Room:
  def __init__(self, name):
    self.players = {}
    self.name = name

  def admit(self, player:Player):
    self.players[player.name] = player
  
  def exclude(self, player_name):
    self.players.pop(player_name)
    
  def __eq__(self, other):
    if not isinstance(other, Room):
        return NotImplemented
    return self.name == other.name

  def __hash__(self):
      return hash(self.name)  

  def game_start(self):
    self.round = 0
    while self.round():
      pass #TODO
  def round(self):
    return False #TODO

  def __str__(self):
    return self.name

  def get_players_list(self):
    return [{"name":str(player)} for player in self.players]