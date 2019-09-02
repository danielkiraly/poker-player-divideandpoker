from __future__ import print_function
import json


class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        try:
            data = json.load(game_state)
            players = data["players"]
            self.log(players)
        except:
            return 600
        return 600

    def showdown(self, game_state):
        pass

    def log(self, message):
        import sys
        print(message, file=sys.stderr)

