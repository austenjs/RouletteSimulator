from .dealer import Dealer
from .player import Player
from .table import Table

from typing import List

class Simulator:
    def __init__(self, players: List[Player], dealer: Dealer, table: Table):
        if len(players) == 0:
            raise Exception('There must be at least one player')

        self.players = players
        self.dealer = dealer
        self.table = table

    def simulate_one_game(self):
        ball_number = self.table.roll()
        for player in self.players:
            if not player.has_money():
                continue

            bets = player.place_bets()
            player.spend_money(len(bets))
            payout = self.dealer.get_payouts(ball_number, bets)
            if payout:
                player.obtain_money(payout)
