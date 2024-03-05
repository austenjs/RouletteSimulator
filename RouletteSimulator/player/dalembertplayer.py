import random
from typing import List

from ..bet import Bet, TWO_TO_ONE_BETS
from .player import Player

class DalembertPlayer(Player):
    def __init__(self, money: int):
        self.unit = 1
        self.last_bet = 5
        self.last_win = False
        super().__init__(money)

    def get_money(self) -> int:
        self.last_win = True
        return super().get_money()
    
    def place_bets(self) -> List[Bet]:
        money_to_spend = self.last_bet
        if self.last_bet == 5 * self.unit:
            pass
        elif self.last_win:
            money_to_spend -= self.unit
        else:
            money_to_spend += self.unit

        if money_to_spend > self.money:
            return []
        self.last_win = False
        self.last_bet = money_to_spend

        bets = []
        bet_type = random.choice(TWO_TO_ONE_BETS)
        for _ in range(money_to_spend):
            bets.append(bet_type())
        return bets
    
    def __str__(self) -> str:
        return 'Dalembert'
