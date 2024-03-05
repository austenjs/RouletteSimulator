from abc import ABC, abstractclassmethod

class Bet(ABC):
    @abstractclassmethod
    def check_number(self, ball_number: str) -> bool:
        pass

    @abstractclassmethod
    def get_payout(self) -> int:
        pass

    @abstractclassmethod
    def _validate(self) -> bool:
        pass
