from Price import Price
from typing import List

class Strategy:
    def __init__(self,prices:List[Price]):
        self.prices = prices

    def execute(self):
        pass