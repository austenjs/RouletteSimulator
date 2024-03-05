import random

from .table import Table

class AmericanTable(Table):
    '''
    A class that represent an american table (0, 00, 1-36)
    '''
    def roll(self) -> str:
        ball_number = random.randint(1, 38)
        if ball_number == 37:
            return '0'
        elif ball_number == 38:
            return '00'
        return str(ball_number)
