import random
from typing import List

from ..bet import Bet, DozenBet, FourNumbersBet
from .player import Player

CHOICES = [(DozenBet(1), DozenBet(2), FourNumbersBet([26, 27, 29, 30]), FourNumbersBet([31, 32, 34, 35])),
           (DozenBet(1), DozenBet(2), FourNumbersBet([25, 26, 28, 29]), FourNumbersBet([32, 33, 35, 36])),
           (DozenBet(2), DozenBet(3), FourNumbersBet([1, 2, 4, 5]), FourNumbersBet([8, 9, 11, 12])),
           (DozenBet(2), DozenBet(3), FourNumbersBet([2, 3, 5, 6]), FourNumbersBet([7, 8, 10, 11])),
           (DozenBet(1), DozenBet(3), FourNumbersBet([13, 14, 16, 17]), FourNumbersBet([20, 21, 23, 24])),
           (DozenBet(1), DozenBet(3), FourNumbersBet([14, 15, 17, 18]), FourNumbersBet([19, 20, 22, 23]))]

class RomanovskyPlayer(Player):
    def place_bets(self) -> List[Bet]:
        if self.money < 8:
            return []
        
        bets = []
        first_type_bet, second_type_bet, third_type_bet, fourth_type_bet = random.choice(CHOICES)
        for _ in range(3):
            bets.append(first_type_bet)
            bets.append(second_type_bet)
        
        bets.append(third_type_bet)
        bets.append(fourth_type_bet)
        return bets

    def __str__(self) -> str:
        return 'Romanovsky'
