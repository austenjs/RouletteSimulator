from .bet import Bet

class ParityBet(Bet):
    def __init__(self, parity: int):
        self.parity = parity
        if not self._validate():
            raise Exception('Only can set odd or even')
        
    def _validate(self) -> bool:
        return self.parity in {0, 1}

    def check_number(self, ball_number: str) -> bool:
        if ball_number == '0':
            return False
        elif ball_number == '00':
            return False

        ball_number = int(ball_number)
        return ball_number % 2 == self.parity

    def get_payout(self) -> int:
        return 2

class OddBet(ParityBet):
    def __init__(self):
        super().__init__(1)

class EvenBet(ParityBet):
    def __init__(self):
        super().__init__(0)
