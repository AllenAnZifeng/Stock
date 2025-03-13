from datetime import datetime

class Price:
    def __init__(self, date, open_price, high, low, close, volume):
        self.date:datetime = datetime.strptime(date, "%Y-%m-%d")
        self.open = float(open_price)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = int(volume)

    def __repr__(self):
        return f"Price(date={self.date}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})"
