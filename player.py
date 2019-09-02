from __future__ import print_function


class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        players = game_state["players"]
        hole_cards = []
        bet = ''
        for player in players:
            if player['name'] == 'DivideAndPoker':
                hole_cards = player['hole_cards']
                bet = player['bet']
        self.log(hole_cards[0]['rank'])
        buy_in = int(game_state['current_buy_in']) - int(bet)
        current_round = game_state['round']
        if self.isPair(hole_cards):
            return 1000
        elif self.twoHighCard(hole_cards):
            return 1000
        elif self.isHighCard(hole_cards) or self.isSameColor(hole_cards):
            return 100
        else:
            return 0


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
        highCards = ["A", "J", "Q", "K"]
        if cards[0]["rank"] in highCards or cards[1]["rank"] in highCards:
            return True
        else:
            return False


    def twoHighCard(self, cards):
        highCards = ["A", "J", "Q", "K"]
        if (cards[0]["rank"] in highCards) and (cards[1]["rank"] in highCards):
            return True
        else:
            return False


