class UserStatus:
  def __init__(self, player_name):
    self.player_name = player_name
    self.cards = [0,0,0,0]
    self.is_passed = False
    self.win = 0