import random
from typing import List

from ..bet import Bet, TWO_TO_ONE_BETS
from .player import Player

class MartingalePlayer(Player):
    def __init__(self, money: int):
        super().__init__(money)
        self.last_Bet = 0

    def obtain_money(self, money: int) -> None:
        # reset
        self.last_Bet = 0
        return super().obtain_money(money)

    def place_bets(self) -> List[Bet]:
        money_to_spend = max(1, 2 * self.last_Bet)
        if money_to_spend > self.money:
            return []
        self.last_Bet = money_to_spend

        bets = []
        bet_type = random.choice(TWO_TO_ONE_BETS)
        for _ in range(money_to_spend):
            bets.append(bet_type())
        return bets

    def __str__(self) -> str:
        return 'Martingale'
