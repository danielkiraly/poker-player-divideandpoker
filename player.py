from __future__ import print_function
import json


class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        try:
            players = game_state["players"]
            hole_cards = []
            for player in players:
                if player['name'] == 'DivideAndConquer':
                    hole_cards = player['hole_cards']
            self.log(hole_cards)
        except:
            self.log('handling exception')
            return 600
        return 600

    def showdown(self, game_state):
        pass

    def log(self, message):
        import sys
        print(message, file=sys.stderr)

