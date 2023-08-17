class Weapon:
    def __init__(self, ammoinmagazine, ammoingeneral, amogaz):
        self.ammoinmagazine = ammoinmagazine
        self.ammoingeneral = ammoingeneral
        self.amogaz = amogaz
    def shootandreload(self, ammoinmagazine, ammoingeneral):
        self.ammoinmagazine = ammoinmagazine
        self.ammoingeneral = ammoingeneral
        if(ammoinmagazine == 0):
          print(ammoinmagazine)
          return self.shootandreload(ammoinmagazine - 1, ammoingeneral)



