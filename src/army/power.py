class Power:

    def __init__(self):
        
        self.SOPower = 1
        self.AIRpower = 4
        self.SHPower = 8


    def setPower(self ,Solpercent, Airpercent, SHpercernt):

        self.SOPower *= Solpercent / 100
        self.SHPower *= SHpercernt / 100
        self.AIRpower *= Airpercent / 100
 

    def getArmyPower(self):

        return [self.SOPower, self.AIRpower, self.SHPower]