from abc import ABC, abstractmethod

class Table(ABC):
    '''
    An abstract class that represent a Roulette table
    '''
    @abstractmethod
    def roll(self) -> str:
        '''
        Roll the ball and get the winning number
        '''
