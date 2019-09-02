import json
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        data = json.load(game_state)
        """players = data["players"]
        hole_cards = players["hole"]"""
        print(data)
        return 0

    def showdown(self, game_state):
        pass

