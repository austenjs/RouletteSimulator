from enum import Enum

from .bet import Bet

class Color(Enum):
    '''
    An enum class used by ColorBet
    '''
    GREEN = 0
    RED = 1
    BLACK = 2

class ColorBet(Bet):
    '''
    A class to represents color bet (red or black)
    '''
    RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

    def __init__(self, color: Color):
        self.color = color
        if not self._validate():
            raise Exception('Can only Bet red or black color')

    def _get_color(self, number: str) -> Color:
        number = int(number)
        if number in ColorBet.RED_NUMBERS:
            return Color.RED
        if number in ColorBet.BLACK_NUMBERS:
            return Color.BLACK
        return Color.GREEN

    def _validate(self) -> bool:
        return self.color in {Color.RED, Color.BLACK}

    def check_number(self, ball_number: str) -> bool:
        ball_color = self._get_color(ball_number)
        return ball_color == self.color

    def get_payout(self) -> int:
        return 2

class RedBet(ColorBet):
    '''
    A class to represents red color bet
    '''
    def __init__(self):
        super().__init__(Color.RED)

    def __str__(self) -> str:
        return 'RED Bet'

class BlackBet(ColorBet):
    '''
    A class to represents black color bet
    '''
    def __init__(self):
        super().__init__(Color.BLACK)

    def __str__(self) -> str:
        return 'BLACK Bet'
