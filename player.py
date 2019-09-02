from __future__ import print_function
import json


class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        try:
            players = game_state["players"]
            hole_cards = []
            for player in players:
                if player['name'] == 'DivideAndPoker':
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


    def isPair(self, cards):
        if cards[0]["rank"] == cards[1]["rank"]:
            return True
        else:
            return False


    def isSameColor(self, cards):
        if cards[0]["suit"] == cards[1]["suit"]:
            return True
        else:
            return False


    def isHighCard(self, cards):

