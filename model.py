class Action:
    def __init__(self, name, price, benefit):
        self.name = name
        self.price = price
        self.benefit = benefit

    def calculate_profit(self):
        profit = (self.price * self.benefit) / 100
        return round(profit, 2)

    def __repr__(self):
        return f'{self.name}'
