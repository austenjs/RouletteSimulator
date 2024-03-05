from typing import List

from .bet import Bet

class Dealer:
    '''
    A class that represents a dealer
    '''
    def get_payouts(self, ball_number: str, bets: List[Bet]) -> int:
        '''
        Based on the winning number, distribute the payouts to the players
        '''
        payout = 0
        for bet in bets:
            if bet.check_number(ball_number):
                payout += bet.get_payout()
        return payout
