import random
from typing import List

from ..bet import Bet, BlackBet, ColumnBet, RedBet
from .player import Player

CHOICES = [(BlackBet(), ColumnBet(3)), (RedBet(), ColumnBet(2))]
class PloppyPlayer(Player):
    def place_bets(self) -> List[Bet]:
        if self.money < 5:
            return []
        
        bets = []
        first_type_bet, second_type_bet = random.choice(CHOICES)
        for _ in range(3):
            bets.append(first_type_bet)
        for _ in range(2):
            bets.append(second_type_bet)
        return bets

    def __str__(self) -> str:
        return 'Ploppy'
