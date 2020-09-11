from .country import country
from ...army.Army import army


class germany(country):

    Name = 'Germany'
    Life = 3000

    def __init__(self, initialMoney):
        self.Money = initialMoney
        self.life = 6000

