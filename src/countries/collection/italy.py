from .country import country
from ...army.Army import army


class italy(country):

    def __init__(self, initialMoney, soldiers, ships, airplanes):
        
        self.Name = 'England'
        self.Money = initialMoney
        self.Life = 6000
        self.Army = army(20, 150, 400, Soldiers= soldiers, Ships= ships, Airplanes= airplanes)
        self.Builds = []

    def special(self):

        self.Army.buyShips(12)
        self.Army.armyPower.setPower(0, 0, 30)

    