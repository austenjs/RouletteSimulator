import random

from .table import Table

class EuropeanTable(Table):
    def roll(self) -> str:
        ball_number = random.randint(1, 37)
        if ball_number == 37:
            ball_number = 0
        return str(ball_number)
