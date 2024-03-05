import random
from typing import List

from ..bet import Bet, THREE_TO_ONE_BETS
from .player import Player

class FibonacciPlayer(Player):
    '''
    A class that represent a player with Fibonacci Strategy
    '''
    def __init__(self, money: int):
        super().__init__(money)
        self.last_last_bet = 0
        self.last_bet = 1

    def obtain_money(self, money: int) -> None:
        # reset
        self.last_last_bet = 0
        self.last_bet = 1
        return super().obtain_money(money)

    def place_bets(self) -> List[Bet]:
        money_to_spend = self.last_last_bet + self.last_bet
        if money_to_spend > self.money:
            return []
        self.last_last_bet = self.last_bet
        self.last_bet = money_to_spend

        bets = []
        bet_type = random.choice(THREE_TO_ONE_BETS)
        index_number = random.randint(1, 3)
        for _ in range(money_to_spend):
            bets.append(bet_type(index_number))
        return bets

    def __str__(self) -> str:
        return 'Fibonacci'
