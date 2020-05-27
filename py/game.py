import random
from collections import OrderedDict
from player import Player


class Game:
    def __init__(self):
        self.round = 0
        self.is_finished = True

    def start(self, players):
        self.round = 0
        self.is_finished = False
        randomized_player_names = random.sample(list(players), len(players))
        self.players: OrderedDict[str: Player] = OrderedDict({player_name: Player(player_name) for player_name in randomized_player_names})
        self.start_round()

    def end(self):
        self.is_finished = True

    def start_round(self):
        self.turn: list[Player] = list(self.players.values())
        self.round += 1
        self.phase = "down"  # bid, reveal

    def get_status_of_players(self, mode="game"):
        return [{"name": player.name, "status": player.as_dict()} for player in self.players.values()]
    
    def can_action(self, player_name, phases):
        if self.is_finished:
            return False
        if player_name != self.turn[0].name:
            return False
        return self.phase in phases

    def down(self, player_name, card_num):
        try:
            if not self.can_action(player_name, ("down")):
                return False

            cards = self.turn[0].cards
            card_num = int(card_num)
            if cards[card_num] != 0:
                return False

            cards[card_num] = 1
            self.turn.append(self.turn.pop(0))
            return True
        except Exception:
            return False

    def bid(self, player_name, declared_number):
        try:
            if not self.can_action(player_name, ("down", "bid")):
                return False

            # Return false if there is no down card.
            if 1 not in self.turn[0].cards:
                return False

            last_player = self.turn[-1]
            declared_number = int(declared_number)
            if last_player.declared_number >= declared_number:
                return False

            self.turn[0].declared_number = declared_number
            self.turn.append(self.turn.pop(0))
            self.phase = "bid"
            return True
        except Exception:
            return False

    def pass_turn(self, player_name):
        try:
            if not self.can_action(player_name, ("bid")):
                return False
            if len(self.turn) == 1:
                return False

            self.turn.pop(0)
            if len(self.turn) == 1:
                self.phase = "reveal"
  
            return True
        except Exception:
            return False
