from .bet import Bet

class DozenBet(Bet):
    '''
    A class that represent dozen bet
    '''
    def __init__(self, dozen_number: int):
        self.dozen_number = dozen_number
        if not self._validate():
            raise Exception('Dozen number must be 1, 2, or 3')

    def _validate(self) -> bool:
        return 1 <= self.dozen_number <= 3

    def check_number(self, ball_number: str) -> bool:
        if ball_number == '0':
            return False
        elif ball_number == '00':
            return False

        ball_number = int(ball_number)
        dozen_number = (ball_number - 1) // 12 + 1
        return dozen_number == self.dozen_number

    def get_payout(self) -> int:
        return 3

    def __str__(self) -> str:
        return 'DOZEN Bet'
