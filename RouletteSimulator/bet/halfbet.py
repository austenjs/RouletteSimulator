from .bet import Bet

class HalfBet(Bet):
    '''
    A class that represent high or low bet
    '''
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        if not self._validate():
            if isinstance(self, HighBet):
                raise Exception(f'{self.__str__()} must range between 19 - 36')
            elif isinstance(self, LowBet):
                raise Exception(f'{self.__str__()} must range between 1 - 18')

    def _validate(self) -> bool:
        if self.start >= self.end:
            return False
        elif self.start < 0 or self.end >= 37:
            return False
        elif self.end - self.start != 17:
            return False
        return self.start in {1, 19}

    def check_number(self, ball_number: str) -> bool:
        ball_color = int(ball_number)
        return self.start <= ball_color <= self.end

    def get_payout(self) -> int:
        return 2

class HighBet(HalfBet):
    '''
    A class that represent high bet (19 - 36)
    '''
    def __init__(self) -> None:
        super().__init__(19, 36)

    def __str__(self) -> str:
        return 'HIGH Bet'

class LowBet(HalfBet):
    '''
    A class that represent low bet (1 - 18)
    '''
    def __init__(self) -> None:
        super().__init__(1, 18)

    def __str__(self) -> str:
        return 'LOW Bet'
