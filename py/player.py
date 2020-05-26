class Player:
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.cards = [0, 0, 0, 0]
        self.bid = 0

    def as_dict(self, purpose="game"):
        if purpose == "game":
            cards = self.cards
            result = {
                "name": self.name,
                "win": self.win,
                "cards": {
                    "hand": cards.count(0),
                    "down": cards.count(1),
                    "up": [i for i, card in enumerate(cards) if card == 2]
                },
                "bid": self.bid
            }
            return result

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
