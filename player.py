from __future__ import print_function
import json


class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        """data = json.load(game_state)
        players = data["players"]
        hole_cards = []
        for player in players:
            if player["name"] == "DivideAndPoker":
                hole_cards = player["hole_cards"]
        if hole_cards[0]["rank"] == hole_cards[1]["rank"]:
            return 10
        else:
            return 0"""
        return 501

    def showdown(self, game_state):
        pass

    def log(message):
        import sys
        print(message, file=sys.stderr)

