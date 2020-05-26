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
        self.turn: list[str] = list(self.players.keys())
        self.round += 1
        self.phase = "down"  # bid, reveal

    def get_status_of_players(self, mode="game"):
        return [{"name": player.name, "status": player.as_dict()} for player in self.players.values()]
        
    def down(self, player_name, card_num):
        try:
            if self.is_finished:
                return False
            if self.phase == "down":
                return False
            if player_name != self.turn[0]:
                return False
            cards = self.players[player_name].cards
            card_num = int(card_num)
            if cards[card_num] != 0:
                return False

            self.turn.append(self.turn.pop(0))
            cards[card_num] = 1
            return True
        except:
            return False
