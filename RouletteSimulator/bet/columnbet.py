from .bet import Bet

class ColumnBet(Bet):
    '''
    A class that represent column bet
    '''
    def __init__(self, col_number: int):
        self.col_number = col_number
        if not self._validate():
            raise Exception('Column number must be 1, 2, or 3')

    def _validate(self) -> bool:
        return 1 <= self.col_number <= 3

    def check_number(self, ball_number: str) -> bool:
        if ball_number == '0':
            return False
        elif ball_number == '00':
            return False

        ball_number = int(ball_number)
        col_number = ball_number % 3
        return col_number == (self.col_number % 3)

    def get_payout(self) -> int:
        return 3

    def __str__(self) -> str:
        return 'COLUMN Bet'
