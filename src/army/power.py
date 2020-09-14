class Power:

    def __init__(self):
        
        self.SOPower = 1
        self.AIRpower = 4
        self.SHPower = 9


    def setPower(self ,Solpercent, Airpercent, SHpercernt):

        self.SOPower += self.SOPower * (Solpercent / 100)
        self.SHPower += self.SOPower * (SHpercernt / 100)
        self.AIRpower += self.SOPower * (Airpercent / 100)
 

    def getArmyPower(self):

        return [self.SOPower, self.AIRpower, self.SHPower]