
from lib import player

class State:
    def __init__(self):
        self.players = {} # username: Player object

    def add_player(self, username):
        self.players[username] = player.Player(username)
        