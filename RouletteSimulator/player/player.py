from abc import ABC, abstractclassmethod
from typing import List

from ..bet import Bet

class Player(ABC):
    def __init__(self, money: int):
        self.money = money

    def get_money(self) -> int:
        return self.money
    
    def set_money(self, money) -> None:
        self.money = money

    def obtain_money(self, money: int) -> None:
        self.money += money

    def spend_money(self, money: int) -> int:
        self.money -= money
        return money
    
    def has_money(self) -> bool:
        return self.money > 0

    @abstractclassmethod
    def place_bets(self) -> List[Bet]:
        pass
