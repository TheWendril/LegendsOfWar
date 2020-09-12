from .country import country
from ...army.Army import army


class germany(country):

    def __init__(self, initialMoney):
        
        self.Name = 'Germany'

        self.Money = initialMoney
        self.Life = 6000
        self.Army = army(20, 150, 400)
        self.Builds = []

    def special():
        pass