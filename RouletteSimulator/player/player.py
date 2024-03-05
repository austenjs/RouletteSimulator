from abc import ABC, abstractmethod
from typing import List

from ..bet import Bet

class Player(ABC):
    '''
    An abstract class that represents a player with a certain strategy
    '''
    def __init__(self, money: int):
        self.money = money

    def get_money(self) -> int:
        '''
        Getter function
        '''
        return self.money

    def set_money(self, money) -> None:
        '''
        Setter function
        '''
        self.money = money

    def obtain_money(self, money: int) -> None:
        '''
        Player receives money from a winning bet
        '''
        self.money += money

    def spend_money(self, money: int) -> int:
        '''
        Player spends money when placing a bet
        '''
        self.money -= money
        return money

    def has_money(self) -> bool:
        '''
        Check whether player still has money to play
        '''
        return self.money > 0

    @abstractmethod
    def place_bets(self) -> List[Bet]:
        '''
        Player places bet on a roulette game
        '''
