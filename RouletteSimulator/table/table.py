from abc import ABC, abstractclassmethod
import random
from typing import List

class Table(ABC):
    @abstractclassmethod
    def roll(self) -> str:
        pass
