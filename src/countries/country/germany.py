import country

class germany(country.country):

    countryName = 'Germany'

    def __init__(self, initialMoney):
        
        self.Money = initialMoney
        self.life = 6000

