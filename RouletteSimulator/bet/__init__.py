from .bet import Bet
from .colorbet import BlackBet, RedBet
from .columnbet import ColumnBet
from .dozenbet import DozenBet
from .halfbet import LowBet, HighBet
from .numberbet import NumberBet, OneNumberBet, TwoNumbersBet, ThreeNumbersBet, FourNumbersBet, SixNumbersBet
from .paritybet import EvenBet, OddBet

TWO_TO_ONE_BETS = [BlackBet, RedBet, EvenBet, OddBet, HighBet, LowBet]
THREE_TO_ONE_BETS = [ColumnBet, DozenBet]
