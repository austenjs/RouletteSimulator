from typing import List

from .bet import Bet

class NumberBet(Bet):
    '''
    A class that represent number bet
    '''
    def __init__(self, numbers: List[str]):
        self.numbers = numbers
        if not self._validate():
            raise Exception(f'Unable to set {numbers} as bet for {self.__str__()}')

    def check_number(self, ball_number: str) -> bool:
        return ball_number in self.numbers

class OneNumberBet(NumberBet):
    '''
    A class that represent a single number bet - Also known as Straight Up Bet
    '''
    def get_payout(self) -> int:
        return 36

    def _validate(self):
        if len(self.numbers) != 1:
            return False

        number = int(self.numbers[0])
        if number < 0 or number >= 37:
            return False
        return True

    def __str__(self) -> str:
        return 'STRAIGHT UP Bet'

class TwoNumbersBet(NumberBet):
    '''
    A class that represent a two number bet - Also known as Split Bet
    '''
    def get_payout(self) -> int:
        return 18

    def _validate(self):
        if len(self.numbers) != 2:
            return False

        a, b = sorted(map(int, self.numbers))
        if a <= 0 or b >= 37:
            return False

        diff = b - a
        return diff in {1, 3}

    def __str__(self) -> str:
        return 'SPLIT Bet'

class ThreeNumbersBet(NumberBet):
    '''
    A class that represent a three number bet - Also known as Street Bet
    '''
    def get_payout(self) -> int:
        return 12

    def _validate(self):
        if len(self.numbers) != 3:
            return False

        a, b, c = sorted(map(int, self.numbers))
        if a <= 0 or c >= 37:
            return False
        elif a % 3 != 1:
            return False
        elif b % 3 != 2:
            return False
        elif c % 3 != 0:
            return False
        return a + 1 == b and b + 1 == c

    def __str__(self) -> str:
        return 'STREET Bet'

class FourNumbersBet(NumberBet):
    '''
    A class that represent a four number bet - Also known as Corner Bet
    '''
    def get_payout(self) -> int:
        return 9

    def _validate(self):
        if len(self.numbers) != 4:
            return False

        a, b, c, d = sorted(map(int, self.numbers))
        if a <= 0 or d >= 37:
            return False
        elif (a + b + c + d) % 2 != 0:
            return False
        return a + 3 == c and b + 3 == d

    def __str__(self) -> str:
        return 'CORNER Bet'

class SixNumbersBet(NumberBet):
    '''
    A class that represent a six number bet - Also known as Six Line Bet
    '''
    def get_payout(self) -> int:
        return 6

    def _validate(self):
        if len(self.numbers) != 6:
            return False

        a, b, c, d, e, f = sorted(map(int, self.numbers))
        if a <= 0 or f >= 37:
            return False
        elif (a + b + c + d + e + f) % 2 != 1:
            return False
        elif a % 3 != 1 or d % 3 != 1 or a + 3 != d:
            return False
        elif b % 3 != 2 or e % 3 != 2 or b + 3 != e:
            return False
        elif c % 3 != 0 or f % 3 != 0 or c + 3 != f:
            return False
        return a + 1 == b and b + 1 == c

    def __str__(self) -> str:
        return 'Six Line/Double Street Bet'
