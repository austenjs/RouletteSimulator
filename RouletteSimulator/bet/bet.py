from abc import ABC, abstractmethod

class Bet(ABC):
    '''
    An abstract class that represents a bet in Roulette game
    '''
    @abstractmethod
    def check_number(self, ball_number: str) -> bool:
        '''
        Check whether the ball number wins the bet
        '''

    @abstractmethod
    def get_payout(self) -> int:
        '''
        Get a certain amount of money if the bet win
        '''

    @abstractmethod
    def _validate(self) -> bool:
        '''
        Validate the arguments passed during object creation
        '''
