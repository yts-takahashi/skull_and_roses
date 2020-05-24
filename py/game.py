import random
from user_status import UserStatus
class Game:
  def __init__(self):
    self.round = 0
    self.is_finished = True

  def start(self, players):
    self.round = 1
    self.is_finished = False
    self.statuses = [UserStatus(player) for player in players]
    random.shuffle(self.statuses)

  def end(self):
    self.is_finished = True

  def get_status_of_players(self, mode="game"):
    # if mode=="game":
    #   return [{"name":str(status.player_name), "place":i, "down_cards":status.cards, "is_passed":status.is_passed, "win":status.win} for i,status in enumerate(self.statuses)]
    # else:
    # return [{"name":str(status.player_name), "place":i, "cards":status.cards, "is_passed":status.is_passed, "win":status.win} for i,status in enumerate(self.statuses)]
    # return [{"name":str(status.player_name), "place":i, "cards":status.cards, "is_passed":status.is_passed, "win":status.win} for i,status in enumerate(self.statuses)]
    return [{"name":str(status.player_name)} for i,status in enumerate(self.statuses)]
    
