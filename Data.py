# Data Class contains api for price data
from Price import Price
from typing import List
from datetime import datetime

class Data:
    def __init__(self,price_data:List[Price]):
        self.price_data = price_data

    # provide time range to retrive data
    def get_price_data(self,start_date:str,end_date:str) -> List[Price]:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        prices = [price for price in self.price_data if start_date <= price.date <= end_date]
        prices.sort(key=lambda x: x.date)
        return prices

    def group_by_month(self) -> dict:
        # to-do
        pass
