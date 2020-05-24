class Player:
  def __init__(self, name, websocket):
    self.name = name
    self.websocket = websocket

  def __eq__(self, other):
    if not isinstance(other, Player):
        return NotImplemented
    return self.name == other.name

  def __hash__(self):
    return hash(self.name)  

  def __str__(self):
    return self.name

