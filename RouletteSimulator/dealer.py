from typing import List

from .bet import Bet

class Dealer:
    def get_payouts(self, ball_number: str, bets: List[Bet]) -> int:
        payout = 0
        for bet in bets:
            if bet.check_number(ball_number):
                payout += bet.get_payout()
        return payout
